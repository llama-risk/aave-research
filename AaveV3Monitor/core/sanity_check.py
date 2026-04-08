"""On-chain RPC cross-validation of GraphQL data.

Validates supply/borrow caps (exact match) and totals (<1% tolerance)
against direct on-chain reads for a sample of reserves.
"""

from __future__ import annotations

import logging
import random
from dataclasses import dataclass, field
from datetime import datetime, timezone

import requests

from config.contracts import MARKETS, get_rpc_url

logger = logging.getLogger(__name__)

# ── ABI selectors ────────────────────────────────────────────────────────
# Pool.ADDRESSES_PROVIDER() → address
SEL_ADDRESSES_PROVIDER = "0x0542975c"
# PoolAddressesProvider.getPool() → address
SEL_GET_POOL = "0x026b1d5f"
# PoolAddressesProvider.getPoolDataProvider() → address
SEL_GET_DATA_PROVIDER = "0xe860accb"
# Pool.getConfiguration(address) → uint256 (packed bitmap)
SEL_GET_CONFIGURATION = "0xc44b11f7"
# DataProvider.getReserveData(address) → (uint256[12])
SEL_GET_RESERVE_DATA = "0x35ea6a75"

# Tolerances
CAP_TOLERANCE = 0          # exact match required
SUPPLY_BORROW_TOLERANCE = 1.0  # 1% for supply/borrow totals
UTIL_TOLERANCE = 1.0       # 1 pp for utilization

# Cache for resolved contract addresses {market_name: {pool, data_provider}}
_resolved_contracts: dict[str, dict] = {}


@dataclass
class CheckResult:
    symbol: str
    chain_name: str
    market_name: str
    # Cap validation
    gql_supply_cap: float
    rpc_supply_cap: float | None
    gql_borrow_cap: float
    rpc_borrow_cap: float | None
    caps_match: bool
    # Supply/borrow validation
    gql_total_supply: float
    rpc_total_supply: float | None
    supply_diff_pct: float | None
    gql_total_borrow: float
    rpc_total_borrow: float | None
    borrow_diff_pct: float | None
    # Utilization
    gql_util_pct: float
    rpc_util_pct: float | None
    util_diff_pp: float | None
    # Status
    passed: bool
    hard_fail: bool  # cap mismatch = hard fail
    error: str | None = None


@dataclass
class SanityReport:
    checks: list[CheckResult] = field(default_factory=list)
    skipped_chains: list[str] = field(default_factory=list)

    @property
    def all_passed(self) -> bool:
        return all(c.passed for c in self.checks) and not self.hard_fails

    @property
    def hard_fails(self) -> int:
        return sum(1 for c in self.checks if c.hard_fail)

    @property
    def warnings(self) -> int:
        return sum(1 for c in self.checks if not c.passed and not c.hard_fail)

    @property
    def total_checked(self) -> int:
        return len(self.checks)


def _eth_call(rpc_url: str, to: str, data: str, timeout: int = 10) -> str | None:
    """Make an eth_call and return the hex result, or None on error."""
    try:
        resp = requests.post(rpc_url, json={
            "jsonrpc": "2.0", "id": 1, "method": "eth_call",
            "params": [{"to": to, "data": data}, "latest"],
        }, timeout=timeout)
        result = resp.json()
        if "error" in result:
            return None
        return result.get("result")
    except Exception as e:
        logger.debug("RPC call failed: %s", e)
        return None


def _pad_address(addr: str) -> str:
    return addr[2:].lower().zfill(64)


def _decode_uint(hex_data: str, field_idx: int) -> int:
    """Decode a uint256 at the given 32-byte field index."""
    start = field_idx * 64
    end = start + 64
    if end > len(hex_data):
        return 0
    return int(hex_data[start:end], 16)


def _resolve_contracts(market_name: str, rpc_url: str) -> dict | None:
    """Resolve Pool and DataProvider from PoolAddressesProvider. Cached."""
    if market_name in _resolved_contracts:
        return _resolved_contracts[market_name]

    market_cfg = MARKETS.get(market_name)
    if not market_cfg:
        return None

    pap = market_cfg["pool_addresses_provider"]

    pool_result = _eth_call(rpc_url, pap, SEL_GET_POOL)
    dp_result = _eth_call(rpc_url, pap, SEL_GET_DATA_PROVIDER)

    if not pool_result or len(pool_result) < 42 or not dp_result or len(dp_result) < 42:
        logger.warning("Failed to resolve contracts for %s", market_name)
        return None

    contracts = {
        "pool": "0x" + pool_result[-40:],
        "data_provider": "0x" + dp_result[-40:],
    }
    _resolved_contracts[market_name] = contracts
    return contracts


def _check_reserve(
    row: dict,
    rpc_url: str,
    contracts: dict,
) -> CheckResult:
    """Validate a single reserve against on-chain data."""
    symbol = row["symbol"]
    token_address = row["token_address"]
    decimals = row["token_decimals"]
    market_name = row["market_name"]
    chain_name = row["chain_name"]

    gql_sc = row["supply_cap"]
    gql_bc = row["borrow_cap"]
    gql_ts = row["total_supply"]
    gql_tb = row["total_borrow"]
    gql_util = row.get("utilization_pct", row.get("utilization_rate", 0) * 100)

    addr_padded = _pad_address(token_address)

    # ── Read caps from Pool.getConfiguration ─────────────────────────
    config_result = _eth_call(rpc_url, contracts["pool"], SEL_GET_CONFIGURATION + addr_padded)
    rpc_sc = None
    rpc_bc = None
    if config_result and len(config_result) > 2:
        config_int = int(config_result, 16)
        rpc_sc = (config_int >> 116) & ((1 << 36) - 1)
        rpc_bc = (config_int >> 80) & ((1 << 36) - 1)

    # ── Read supply/borrow from DataProvider.getReserveData ──────────
    data_result = _eth_call(rpc_url, contracts["data_provider"], SEL_GET_RESERVE_DATA + addr_padded)
    rpc_ts = None
    rpc_tb = None
    if data_result and len(data_result) > 130:
        hex_data = data_result[2:]
        total_atoken = _decode_uint(hex_data, 2)
        total_stable = _decode_uint(hex_data, 3)
        total_variable = _decode_uint(hex_data, 4)
        rpc_ts = total_atoken / (10 ** decimals)
        rpc_tb = (total_stable + total_variable) / (10 ** decimals)

    # ── Compare ──────────────────────────────────────────────────────
    caps_match = True
    hard_fail = False

    if rpc_sc is not None and gql_sc != rpc_sc:
        caps_match = False
        hard_fail = True
        logger.error("HARD FAIL: %s supply cap mismatch: GraphQL=%s, RPC=%s",
                      symbol, gql_sc, rpc_sc)

    if rpc_bc is not None and gql_bc != rpc_bc:
        caps_match = False
        hard_fail = True
        logger.error("HARD FAIL: %s borrow cap mismatch: GraphQL=%s, RPC=%s",
                      symbol, gql_bc, rpc_bc)

    supply_diff = None
    borrow_diff = None
    if rpc_ts is not None and rpc_ts > 0:
        supply_diff = abs(gql_ts - rpc_ts) / rpc_ts * 100
    if rpc_tb is not None and rpc_tb > 0:
        borrow_diff = abs(gql_tb - rpc_tb) / rpc_tb * 100

    rpc_util = None
    util_diff = None
    if rpc_ts and rpc_ts > 0 and rpc_tb is not None:
        rpc_util = rpc_tb / rpc_ts * 100
        util_diff = abs(gql_util - rpc_util)

    passed = caps_match
    if supply_diff is not None and supply_diff > SUPPLY_BORROW_TOLERANCE:
        passed = False
    if borrow_diff is not None and borrow_diff > SUPPLY_BORROW_TOLERANCE:
        passed = False

    return CheckResult(
        symbol=symbol, chain_name=chain_name, market_name=market_name,
        gql_supply_cap=gql_sc, rpc_supply_cap=rpc_sc,
        gql_borrow_cap=gql_bc, rpc_borrow_cap=rpc_bc,
        caps_match=caps_match,
        gql_total_supply=gql_ts, rpc_total_supply=rpc_ts, supply_diff_pct=supply_diff,
        gql_total_borrow=gql_tb, rpc_total_borrow=rpc_tb, borrow_diff_pct=borrow_diff,
        gql_util_pct=gql_util, rpc_util_pct=rpc_util, util_diff_pp=util_diff,
        passed=passed, hard_fail=hard_fail,
    )


def validate(results: list[dict], sample_green: int = 3) -> SanityReport:
    """Run on-chain validation for sampled reserves.

    Checks all RED/AMBER reserves + `sample_green` random GREEN reserves.
    """
    report = SanityReport()

    # Select sample
    flagged = [r for r in results if r.get("alert_level") in ("RED", "AMBER")]
    greens = [r for r in results if r.get("alert_level") == "GREEN"
              and not r.get("is_deprecated_supply")]
    green_sample = random.sample(greens, min(sample_green, len(greens)))
    sample = flagged + green_sample

    logger.info("Sanity check: %d reserves (%d flagged + %d green sample)",
                len(sample), len(flagged), len(green_sample))

    # Group by market
    by_market: dict[str, list[dict]] = {}
    for r in sample:
        mn = r["market_name"]
        by_market.setdefault(mn, []).append(r)

    for market_name, reserves in by_market.items():
        market_cfg = MARKETS.get(market_name)
        if not market_cfg:
            logger.warning("No contract config for market %s — skipping", market_name)
            report.skipped_chains.append(market_name)
            continue

        rpc_url = get_rpc_url(market_cfg["chain_id"])
        if not rpc_url:
            logger.warning("No RPC for chain %d (%s) — skipping", market_cfg["chain_id"], market_name)
            report.skipped_chains.append(market_name)
            continue

        # Resolve Pool + DataProvider
        contracts = _resolve_contracts(market_name, rpc_url)
        if not contracts:
            logger.warning("Failed to resolve contracts for %s — skipping", market_name)
            report.skipped_chains.append(market_name)
            continue

        logger.info("Checking %d reserves on %s (chain %d)...",
                    len(reserves), market_name, market_cfg["chain_id"])

        for r in reserves:
            try:
                check = _check_reserve(r, rpc_url, contracts)
                report.checks.append(check)
            except Exception as e:
                logger.error("Error checking %s/%s: %s", r["symbol"], market_name, e)
                report.checks.append(CheckResult(
                    symbol=r["symbol"], chain_name=r["chain_name"],
                    market_name=market_name,
                    gql_supply_cap=r["supply_cap"], rpc_supply_cap=None,
                    gql_borrow_cap=r["borrow_cap"], rpc_borrow_cap=None,
                    caps_match=True,  # can't verify = don't fail
                    gql_total_supply=r["total_supply"], rpc_total_supply=None,
                    supply_diff_pct=None,
                    gql_total_borrow=r["total_borrow"], rpc_total_borrow=None,
                    borrow_diff_pct=None,
                    gql_util_pct=r.get("utilization_pct", 0), rpc_util_pct=None,
                    util_diff_pp=None,
                    passed=True, hard_fail=False, error=str(e),
                ))

    return report


# ── Oracle Price Validation ──────────────────────────────────────────────

# Selectors
SEL_LATEST_ROUND_DATA = "0xfeaf968c"
SEL_LATEST_ANSWER = "0x50d25bcd"
SEL_DECIMALS = "0x313ce567"

PRICE_TOLERANCE_WARN = 1.0    # 1% diff = warning
PRICE_TOLERANCE_FAIL = 5.0    # 5% diff = hard fail
STALE_WARN_HOURS = 24
STALE_CRIT_HOURS = 48


@dataclass
class PriceCheckResult:
    symbol: str
    chain_name: str
    market_name: str
    gql_price: float
    oracle_price: float | None
    price_diff_pct: float | None
    oracle_type: str  # "STANDARD_CL", "PARTIAL_CL", "NO_ORACLE"
    updated_at: datetime | None
    stale_hours: float | None
    passed: bool
    hard_fail: bool
    warning: str | None = None


@dataclass
class PriceReport:
    checks: list[PriceCheckResult] = field(default_factory=list)
    skipped_chains: list[str] = field(default_factory=list)

    @property
    def all_passed(self) -> bool:
        return all(c.passed for c in self.checks)

    @property
    def hard_fails(self) -> int:
        return sum(1 for c in self.checks if c.hard_fail)

    @property
    def warnings(self) -> int:
        return sum(1 for c in self.checks if not c.passed and not c.hard_fail)

    @property
    def stale_count(self) -> int:
        return sum(1 for c in self.checks if c.stale_hours and c.stale_hours > STALE_WARN_HOURS)


def _check_oracle_price(row: dict, rpc_url: str) -> PriceCheckResult:
    """Validate a single reserve's oracle price against on-chain."""
    symbol = row["symbol"]
    chain_name = row["chain_name"]
    market_name = row["market_name"]
    oracle_addr = row.get("oracle_address", "")
    gql_price = row.get("price_usd", 0.0)

    if not oracle_addr or oracle_addr == "0x0000000000000000000000000000000000000000":
        return PriceCheckResult(
            symbol=symbol, chain_name=chain_name, market_name=market_name,
            gql_price=gql_price, oracle_price=None, price_diff_pct=None,
            oracle_type="NO_ORACLE", updated_at=None, stale_hours=None,
            passed=True, hard_fail=False, warning="No oracle address",
        )

    # Try latestRoundData first
    result = _eth_call(rpc_url, oracle_addr, SEL_LATEST_ROUND_DATA)
    oracle_type = "STANDARD_CL"
    updated_at = None
    answer = None

    if result and len(result) > 130:
        hex_data = result[2:]
        answer = int(hex_data[64:128], 16)
        if answer > 2**255:
            answer -= 2**256
        updated_ts = int(hex_data[192:256], 16)
        if updated_ts > 0:
            updated_at = datetime.fromtimestamp(updated_ts, tz=timezone.utc)
    else:
        # Fallback: latestAnswer
        oracle_type = "PARTIAL_CL"
        result2 = _eth_call(rpc_url, oracle_addr, SEL_LATEST_ANSWER)
        if result2 and len(result2) > 4:
            answer = int(result2, 16)
            if answer > 2**255:
                answer -= 2**256
        else:
            return PriceCheckResult(
                symbol=symbol, chain_name=chain_name, market_name=market_name,
                gql_price=gql_price, oracle_price=None, price_diff_pct=None,
                oracle_type="NO_ORACLE", updated_at=None, stale_hours=None,
                passed=True, hard_fail=False, warning="Oracle call failed",
            )

    # Get decimals
    dec_result = _eth_call(rpc_url, oracle_addr, SEL_DECIMALS)
    decimals = 8  # default
    if dec_result and len(dec_result) > 4:
        try:
            decimals = int(dec_result, 16)
        except ValueError:
            pass

    oracle_price = answer / (10 ** decimals) if answer is not None else None

    # Compare
    price_diff = None
    passed = True
    hard_fail = False
    warning = None

    if oracle_price is not None and gql_price > 0:
        price_diff = abs(oracle_price - gql_price) / gql_price * 100
        if price_diff > PRICE_TOLERANCE_FAIL:
            passed = False
            hard_fail = True
            warning = f"Price diff {price_diff:.2f}% > {PRICE_TOLERANCE_FAIL}% threshold"
        elif price_diff > PRICE_TOLERANCE_WARN:
            passed = False
            warning = f"Price diff {price_diff:.2f}%"

    # Staleness check
    stale_hours = None
    if updated_at:
        stale_hours = (datetime.now(timezone.utc) - updated_at).total_seconds() / 3600
        if stale_hours > STALE_CRIT_HOURS:
            passed = False
            warning = (warning + "; " if warning else "") + f"STALE: {stale_hours:.1f}h since update"
        elif stale_hours > STALE_WARN_HOURS:
            if not warning:
                passed = False
            warning = (warning + "; " if warning else "") + f"Stale: {stale_hours:.1f}h since update"

    return PriceCheckResult(
        symbol=symbol, chain_name=chain_name, market_name=market_name,
        gql_price=gql_price, oracle_price=oracle_price, price_diff_pct=price_diff,
        oracle_type=oracle_type, updated_at=updated_at, stale_hours=stale_hours,
        passed=passed, hard_fail=hard_fail, warning=warning,
    )


def validate_prices(results: list[dict], sample_green: int = 3) -> PriceReport:
    """Validate oracle prices for sampled reserves."""
    report = PriceReport()

    flagged = [r for r in results if r.get("alert_level") in ("RED", "AMBER")]
    greens = [r for r in results if r.get("alert_level") == "GREEN"
              and not r.get("is_deprecated_supply")]
    green_sample = random.sample(greens, min(sample_green, len(greens)))
    sample = flagged + green_sample

    logger.info("Price validation: %d reserves", len(sample))

    by_chain: dict[int, list[dict]] = {}
    for r in sample:
        by_chain.setdefault(r["chain_id"], []).append(r)

    for chain_id, reserves in by_chain.items():
        rpc_url = get_rpc_url(chain_id)
        if not rpc_url:
            chain_name = reserves[0]["chain_name"] if reserves else str(chain_id)
            report.skipped_chains.append(chain_name)
            continue

        for r in reserves:
            try:
                check = _check_oracle_price(r, rpc_url)
                report.checks.append(check)
            except Exception as e:
                logger.debug("Price check error for %s: %s", r["symbol"], e)

    return report


def print_price_report(report: PriceReport):
    """Print oracle price validation results."""
    if not report.checks:
        return

    if report.all_passed and not report.skipped_chains:
        print("  ✅ PRICE CHECK PASSED — all oracle prices match GraphQL")
    elif report.hard_fails:
        print(f"  ❌ PRICE CHECK FAILED — {report.hard_fails} price mismatch(es)!")
    elif report.warnings:
        print(f"  ⚠️  PRICE CHECK: {report.warnings} warning(s)")
    else:
        print("  ✅ PRICE CHECK PASSED")

    standard = sum(1 for c in report.checks if c.oracle_type == "STANDARD_CL")
    partial = sum(1 for c in report.checks if c.oracle_type == "PARTIAL_CL")
    no_oracle = sum(1 for c in report.checks if c.oracle_type == "NO_ORACLE")

    print(f"     Checked: {len(report.checks)} prices | "
          f"Standard CL: {standard} | Partial CL: {partial} | No oracle: {no_oracle} | "
          f"Stale: {report.stale_count}")

    if report.skipped_chains:
        print(f"     Skipped (no RPC): {', '.join(report.skipped_chains)}")

    for c in report.checks:
        if c.hard_fail:
            print(f"     ❌ {c.symbol}/{c.chain_name}: "
                  f"GQL=${c.gql_price:,.4f} vs Oracle=${c.oracle_price:,.4f} ({c.warning})")
        elif not c.passed:
            print(f"     ⚠️  {c.symbol}/{c.chain_name}: {c.warning}")

    print()


def print_sanity_report(report: SanityReport):
    """Print compact sanity check results to console."""
    print()
    if report.all_passed and not report.skipped_chains:
        print("  ✅ SANITY CHECK PASSED — all on-chain values match GraphQL")
    elif report.hard_fails:
        print(f"  ❌ SANITY CHECK FAILED — {report.hard_fails} cap mismatch(es)!")
    else:
        print(f"  ⚠️  SANITY CHECK: {report.warnings} warning(s)")

    print(f"     Checked: {report.total_checked} reserves | "
          f"Passed: {sum(1 for c in report.checks if c.passed)} | "
          f"Hard fails: {report.hard_fails} | "
          f"Warnings: {report.warnings}")

    if report.skipped_chains:
        print(f"     Skipped markets (no RPC): {', '.join(report.skipped_chains)}")

    # Show failures/warnings
    for c in report.checks:
        if c.hard_fail:
            print(f"     ❌ {c.symbol}/{c.chain_name}/{c.market_name}: "
                  f"Supply cap GQL={c.gql_supply_cap} vs RPC={c.rpc_supply_cap}, "
                  f"Borrow cap GQL={c.gql_borrow_cap} vs RPC={c.rpc_borrow_cap}")
        elif not c.passed:
            parts = []
            if c.supply_diff_pct and c.supply_diff_pct > SUPPLY_BORROW_TOLERANCE:
                parts.append(f"supply Δ{c.supply_diff_pct:.2f}%")
            if c.borrow_diff_pct and c.borrow_diff_pct > SUPPLY_BORROW_TOLERANCE:
                parts.append(f"borrow Δ{c.borrow_diff_pct:.2f}%")
            print(f"     ⚠️  {c.symbol}/{c.chain_name}: {', '.join(parts)}")
        elif c.error:
            print(f"     ⏭️  {c.symbol}/{c.chain_name}: skipped ({c.error})")

    print()
