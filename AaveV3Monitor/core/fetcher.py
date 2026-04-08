"""Fetch all Aave V3 reserve data from the public GraphQL API."""

from __future__ import annotations

import json
import hashlib
import logging
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

logger = logging.getLogger(__name__)

API_URL = "https://api.v3.aave.com/graphql"

# Cache config (mirrors LiquidityMonitor pattern)
CACHE_DIR = Path(__file__).parent.parent / "data" / "cache"
CACHE_TTL = 3600  # 1 hour

_cache_disabled = False


def disable_cache():
    global _cache_disabled
    _cache_disabled = True


# All known chain IDs — we request all of them and let the API return what exists
ALL_CHAIN_IDS = [
    1, 10, 56, 100, 137, 146, 324, 1088, 1868, 4326,
    5000, 8453, 9745, 42161, 42220, 43114, 57073, 59144, 534352,
]

QUERY = """
{
  markets(request: { chainIds: [%s] }) {
    name
    chain { chainId name }
    address
    totalMarketSize
    reserves {
      underlyingToken { symbol name decimals address }
      usdExchangeRate
      usdOracleAddress
      supplyInfo {
        supplyCap { amount { value } }
        supplyCapReached
        total { value }
        maxLTV { value }
        liquidationThreshold { value }
        apy { value }
        canBeCollateral
      }
      borrowInfo {
        borrowCap { amount { value } }
        borrowCapReached
        total { amount { value } }
        availableLiquidity { amount { value } }
        utilizationRate { value }
        reserveFactor { value }
        apy { value }
        optimalUsageRate { value }
      }
      isFrozen
      isPaused
    }
  }
}
""" % ", ".join(str(c) for c in ALL_CHAIN_IDS)


def _cache_get(key: str) -> tuple | None:
    """Returns (value, cache_age_seconds) or None if miss."""
    if _cache_disabled:
        return None
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    h = hashlib.md5(key.encode()).hexdigest()
    p = CACHE_DIR / f"{h}.json"
    if not p.exists():
        return None
    try:
        d = json.loads(p.read_text())
        age = time.time() - d["ts"]
        if age > CACHE_TTL:
            return None
        return d["v"], age
    except Exception:
        return None


def _cache_set(key: str, value):
    if _cache_disabled:
        return
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    h = hashlib.md5(key.encode()).hexdigest()
    p = CACHE_DIR / f"{h}.json"
    p.write_text(json.dumps({"ts": time.time(), "v": value}))


def _safe_float(val, default=None) -> float | None:
    """Safely extract a float from nested GraphQL value objects."""
    if val is None:
        return default
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        try:
            return float(val)
        except (ValueError, TypeError):
            return default
    if isinstance(val, dict):
        # Handle nested {"amount": {"value": "..."}} or {"value": "..."}
        if "value" in val:
            return _safe_float(val["value"], default)
        if "amount" in val:
            return _safe_float(val["amount"], default)
    return default


def fetch_all_reserves() -> tuple[pd.DataFrame, dict]:
    """Fetch all Aave V3 reserves across all chains.

    Returns:
        (df, metadata) where:
        - df: DataFrame with one row per reserve
        - metadata: dict with fetch_time, chain_ids_found, market_names_found,
                     total_markets, total_reserves
    """
    cache_key = "aave_v3_graphql:all_reserves"
    cached = _cache_get(cache_key)
    data_age_seconds = 0.0  # 0 = fresh fetch

    if cached is not None:
        raw, data_age_seconds = cached
        logger.info("Using cached GraphQL response (%.0fs old)", data_age_seconds)
    else:
        logger.info("Fetching from %s ...", API_URL)
        resp = requests.post(
            API_URL,
            json={"query": QUERY},
            headers={"Content-Type": "application/json"},
            timeout=30,
        )
        resp.raise_for_status()
        raw = resp.json()

        if "errors" in raw:
            raise RuntimeError(f"GraphQL errors: {raw['errors']}")

        _cache_set(cache_key, raw)
        logger.info("Fetched and cached GraphQL response")

    fetch_time = datetime.now(timezone.utc)
    markets = raw["data"]["markets"]

    rows = []
    chain_ids_found = set()
    market_names_found = set()

    for market in markets:
        chain_id = int(market["chain"]["chainId"])
        chain_name = market["chain"]["name"]
        market_name = market["name"]
        market_address = market.get("address", "")
        total_market_size = _safe_float(market.get("totalMarketSize"), 0.0)

        chain_ids_found.add(chain_id)
        market_names_found.add(market_name)

        for r in market.get("reserves", []):
            token = r.get("underlyingToken") or {}
            supply = r.get("supplyInfo") or {}
            borrow = r.get("borrowInfo") or {}

            # Extract supply cap — "0" or 0 means uncapped
            supply_cap_raw = _safe_float(supply.get("supplyCap"), 0.0)
            borrow_cap_raw = _safe_float(borrow.get("borrowCap"), 0.0)

            # Determine if borrowing is enabled (borrow cap > 1 or has borrows)
            total_borrow = _safe_float(borrow.get("total"), 0.0)
            total_supply = _safe_float(supply.get("total"), 0.0)
            borrowing_enabled = borrow_cap_raw > 1 or total_borrow > 0

            # USD price from Aave oracle
            price_usd = _safe_float(r.get("usdExchangeRate"), 0.0)
            oracle_address = r.get("usdOracleAddress", "")

            rows.append({
                "chain_id":              chain_id,
                "chain_name":            chain_name,
                "market_name":           market_name,
                "market_address":        market_address,
                "symbol":                token.get("symbol", "???"),
                "token_name":            token.get("name", ""),
                "token_address":         token.get("address", ""),
                "token_decimals":        int(token.get("decimals", 18)),
                # Price
                "price_usd":             price_usd,
                "oracle_address":        oracle_address,
                # Supply
                "supply_cap":            supply_cap_raw,
                "supply_cap_reached":    supply.get("supplyCapReached", False),
                "total_supply":          total_supply,
                "total_supply_usd":      total_supply * price_usd,
                "max_ltv":               _safe_float(supply.get("maxLTV"), 0.0),
                "liquidation_threshold": _safe_float(supply.get("liquidationThreshold"), 0.0),
                "supply_apy":            _safe_float(supply.get("apy"), 0.0),
                "can_be_collateral":     supply.get("canBeCollateral", False),
                # Borrow
                "borrow_cap":            borrow_cap_raw,
                "borrow_cap_reached":    borrow.get("borrowCapReached", False),
                "total_borrow":          total_borrow,
                "total_borrow_usd":      total_borrow * price_usd,
                "available_liquidity":   _safe_float(borrow.get("availableLiquidity"), 0.0),
                "utilization_rate":      _safe_float(borrow.get("utilizationRate"), 0.0),
                "reserve_factor":        _safe_float(borrow.get("reserveFactor"), 0.0),
                "borrow_apy":            _safe_float(borrow.get("apy"), 0.0),
                "optimal_usage_rate":    _safe_float(borrow.get("optimalUsageRate"), 0.0),
                "borrowing_enabled":     borrowing_enabled,
                # Status
                "is_frozen":             r.get("isFrozen", False),
                "is_paused":             r.get("isPaused", False),
            })

    df = pd.DataFrame(rows)

    metadata = {
        "fetch_time":          fetch_time,
        "data_age_seconds":    data_age_seconds,
        "chain_ids_found":     chain_ids_found,
        "market_names_found":  market_names_found,
        "total_markets":       len(markets),
        "total_reserves":      len(rows),
    }

    logger.info(
        "Parsed %d reserves across %d markets (%d chains)",
        len(rows), len(markets), len(chain_ids_found),
    )

    return df, metadata
