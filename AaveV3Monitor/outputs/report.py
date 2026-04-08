"""Generate markdown monitoring report."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

REPORTS_DIR = Path(__file__).parent.parent / "reports"


def _fmt_pct(value) -> str:
    if value is None:
        return "—"
    return f"{value:.1f}%"


def _fmt_num(value) -> str:
    if value is None:
        return "—"
    if abs(value) >= 1e9:
        return f"{value/1e9:.2f}B"
    if abs(value) >= 1e6:
        return f"{value/1e6:.1f}M"
    if abs(value) >= 1e3:
        return f"{value/1e3:.1f}K"
    return f"{value:,.0f}"


def _short_market(name: str) -> str:
    name = name.replace("AaveV3", "")
    if name.startswith("Ethereum") and name != "Ethereum":
        return name.replace("Ethereum", "ETH ")
    return name


def write_report(results: list[dict], metadata: dict, unknown_chains: set, unknown_markets: set, sanity_report=None) -> Path:
    """Write monitoring report to reports/YYYY-MM-DD_monitor.md."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = REPORTS_DIR / f"{date_str}_monitor.md"

    counts = {}
    for r in results:
        level = r.get("alert_level", "GREEN")
        counts[level] = counts.get(level, 0) + 1

    lines = []
    lines.append(f"# Aave V3 Monitor Report — {date_str}")
    lines.append("")
    lines.append(f"**Generated:** {metadata['fetch_time'].strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append(f"**Coverage:** {metadata['total_reserves']} reserves across {metadata['total_markets']} markets")
    lines.append("")

    # Warnings
    if unknown_chains:
        lines.append(f"> **WARNING:** Unknown chain IDs detected: {unknown_chains}")
        lines.append("> Update `config/chains.py` to include these!")
        lines.append("")
    if unknown_markets:
        lines.append(f"> **WARNING:** Unknown markets detected: {unknown_markets}")
        lines.append("")

    # Data validation
    if sanity_report is not None:
        lines.append("## Data Validation (On-Chain RPC Cross-Check)")
        lines.append("")
        if sanity_report.all_passed:
            lines.append(f"**✅ PASSED** — {sanity_report.total_checked} reserves validated against on-chain RPC. All caps match exactly.")
        else:
            lines.append(f"**⚠️ {sanity_report.warnings} warning(s)** — {sanity_report.total_checked} reserves checked.")
        lines.append("")
        if sanity_report.skipped_chains:
            lines.append(f"Skipped (no RPC): {', '.join(sanity_report.skipped_chains)}")
            lines.append("")
        # Show any warnings
        for c in sanity_report.checks:
            if not c.passed and not c.hard_fail:
                parts = []
                if c.supply_diff_pct and c.supply_diff_pct > 1.0:
                    parts.append(f"supply Δ{c.supply_diff_pct:.2f}%")
                if c.borrow_diff_pct and c.borrow_diff_pct > 1.0:
                    parts.append(f"borrow Δ{c.borrow_diff_pct:.2f}%")
                lines.append(f"- ⚠️ {c.symbol}/{c.chain_name}: {', '.join(parts)}")
        lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Level | Count |")
    lines.append(f"|-------|-------|")
    for level in ["RED", "AMBER", "GREEN", "FROZEN", "SUPPRESSED"]:
        if counts.get(level, 0) > 0:
            emoji = {"RED": "🔴", "AMBER": "🟡", "GREEN": "🟢", "FROZEN": "❄️", "SUPPRESSED": "🔇"}.get(level, "")
            lines.append(f"| {emoji} {level} | {counts.get(level, 0)} |")
    lines.append("")

    # RED findings
    reds = [r for r in results if r.get("alert_level") == "RED"]
    if reds:
        lines.append("## 🔴 RED Alerts")
        lines.append("")
        for r in sorted(reds, key=lambda x: -(x.get("supply_cap_usage_pct") or 0)):
            lines.append(f"### {r['symbol']} — {r['chain_name']} ({_short_market(r['market_name'])})")
            lines.append("")
            for reason in r.get("alert_reasons", []):
                lines.append(f"- {reason}")
            lines.append("")
            # Key metrics
            lines.append(f"| Metric | Value |")
            lines.append(f"|--------|-------|")
            if r.get("supply_cap_usage_pct") is not None:
                lines.append(f"| Supply cap usage | {_fmt_pct(r['supply_cap_usage_pct'])} ({_fmt_num(r['total_supply'])} / {_fmt_num(r['supply_cap'])}) |")
            if r.get("borrow_cap_usage_pct") is not None:
                lines.append(f"| Borrow cap usage | {_fmt_pct(r['borrow_cap_usage_pct'])} ({_fmt_num(r['total_borrow'])} / {_fmt_num(r['borrow_cap'])}) |")
            lines.append(f"| Utilization | {_fmt_pct(r.get('utilization_pct'))} (optimal: {_fmt_pct(r.get('optimal_pct'))}) |")
            lines.append("")

    # AMBER findings
    ambers = [r for r in results if r.get("alert_level") == "AMBER"]
    if ambers:
        lines.append("## 🟡 AMBER Alerts")
        lines.append("")
        lines.append(f"| Asset | Chain | Market | Issue |")
        lines.append(f"|-------|-------|--------|-------|")
        for r in sorted(ambers, key=lambda x: -(x.get("supply_cap_usage_pct") or 0)):
            reasons = r.get("alert_reasons", [])
            reason_str = "; ".join(reasons[:2])
            lines.append(f"| {r['symbol']} | {r['chain_name']} | {_short_market(r['market_name'])} | {reason_str} |")
        lines.append("")

    # Supply cap table
    lines.append("## Supply Cap Usage")
    lines.append("")
    capped = [r for r in results if r.get("supply_cap_usage_pct") is not None
              and r.get("alert_level") not in ("FROZEN", "SUPPRESSED")]
    capped.sort(key=lambda x: -(x.get("supply_cap_usage_pct") or 0))
    lines.append(f"| Asset | Chain | Market | Supply | Cap | Usage% | Headroom |")
    lines.append(f"|-------|-------|--------|--------|-----|--------|----------|")
    for r in capped:
        lines.append(
            f"| {r['symbol']} | {r['chain_name']} | {_short_market(r['market_name'])} "
            f"| {_fmt_num(r['total_supply'])} | {_fmt_num(r['supply_cap'])} "
            f"| {_fmt_pct(r.get('supply_cap_usage_pct'))} | {_fmt_num(r.get('supply_headroom'))} |"
        )
    lines.append("")

    # Borrow cap table
    lines.append("## Borrow Cap Usage")
    lines.append("")
    capped_b = [r for r in results if r.get("borrow_cap_usage_pct") is not None
                and r.get("borrowing_enabled")
                and r.get("alert_level") not in ("FROZEN", "SUPPRESSED")]
    capped_b.sort(key=lambda x: -(x.get("borrow_cap_usage_pct") or 0))
    lines.append(f"| Asset | Chain | Market | Borrow | Cap | Usage% | Headroom |")
    lines.append(f"|-------|-------|--------|--------|-----|--------|----------|")
    for r in capped_b:
        lines.append(
            f"| {r['symbol']} | {r['chain_name']} | {_short_market(r['market_name'])} "
            f"| {_fmt_num(r['total_borrow'])} | {_fmt_num(r['borrow_cap'])} "
            f"| {_fmt_pct(r.get('borrow_cap_usage_pct'))} | {_fmt_num(r.get('borrow_headroom'))} |"
        )
    lines.append("")

    # Utilization table
    lines.append("## Utilization Rates")
    lines.append("")
    utilized = [r for r in results if r.get("utilization_pct", 0) > 0
                and r.get("alert_level") not in ("FROZEN", "SUPPRESSED")]
    utilized.sort(key=lambda x: -(x.get("utilization_pct") or 0))
    lines.append(f"| Asset | Chain | Market | Util% | Optimal% | Δ Optimal |")
    lines.append(f"|-------|-------|--------|-------|----------|-----------|")
    for r in utilized:
        delta = r.get("utilization_vs_optimal", 0)
        lines.append(
            f"| {r['symbol']} | {r['chain_name']} | {_short_market(r['market_name'])} "
            f"| {_fmt_pct(r.get('utilization_pct'))} | {_fmt_pct(r.get('optimal_pct'))} "
            f"| {delta:+.1f}pp |"
        )
    lines.append("")

    # Frozen
    frozen = [r for r in results if r.get("alert_level") == "FROZEN"]
    if frozen:
        lines.append("## ❄️ Frozen / Paused Reserves")
        lines.append("")
        for r in frozen:
            status = []
            if r.get("is_frozen"):
                status.append("Frozen")
            if r.get("is_paused"):
                status.append("Paused")
            lines.append(f"- **{r['symbol']}** — {r['chain_name']} ({_short_market(r['market_name'])}) — {', '.join(status)}")
        lines.append("")

    # Low supply section (USD-based)
    from config import thresholds as T
    low_supply = [r for r in results
                  if r.get("total_supply_usd", 0) > 0
                  and r.get("total_supply_usd", 0) < T.MIN_SUPPLY_USD_MAIN
                  and r.get("alert_level") not in ("FROZEN", "SUPPRESSED")]
    if low_supply:
        low_supply.sort(key=lambda x: x.get("total_supply_usd", 0))
        lines.append(f"## Low Supply Reserves (<${T.MIN_SUPPLY_USD_MAIN/1e3:.0f}K USD)")
        lines.append("")
        lines.append(f"| Asset | Chain | Market | Price | Supply (USD) | Supply (tokens) | Cap Usage |")
        lines.append(f"|-------|-------|--------|-------|-------------|----------------|-----------|")
        for r in low_supply:
            price = f"${r.get('price_usd', 0):,.2f}"
            supply_usd = f"${r.get('total_supply_usd', 0):,.0f}"
            cap_pct = _fmt_pct(r.get("supply_cap_usage_pct"))
            lines.append(
                f"| {r['symbol']} | {r['chain_name']} | {_short_market(r['market_name'])} "
                f"| {price} | {supply_usd} | {_fmt_num(r['total_supply'])} | {cap_pct} |"
            )
        lines.append("")

    # Analyst comments section
    lines.append("## Analyst Comments")
    lines.append("")
    lines.append("<!-- Add your guidance below. These comments will be considered when generating parameter change reports. -->")
    lines.append("")
    lines.append("")

    content = "\n".join(lines)
    path.write_text(content)
    logger.info("Wrote monitoring report to %s", path)
    return path
