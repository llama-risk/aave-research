"""Generate simple parameter change report for flagged reserves."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

PARAM_REPORTS_DIR = Path(__file__).parent.parent.parent / "Aave_Parameter_changes" / "cap_reports"


def _fmt_num(value) -> str:
    if value is None:
        return "—"
    return f"{value:,.0f}"


def _fmt_pct(value) -> str:
    if value is None:
        return "—"
    return f"{value:.1f}%"


def _short_market(name: str) -> str:
    name = name.replace("AaveV3", "")
    if name.startswith("Ethereum") and name != "Ethereum":
        return name.replace("Ethereum", "ETH ")
    return name


def _recommend_cap(current_cap: float, usage_pct: float) -> float:
    """Simple heuristic for analyst review. Not a final recommendation."""
    if usage_pct >= 90:
        return round(current_cap * 1.5)
    elif usage_pct >= 85:
        return round(current_cap * 1.3)
    return current_cap


def write_param_report(results: list[dict]) -> Path | None:
    """Generate parameter change report for RED/AMBER reserves.

    Returns path to written file, or None if no flagged reserves.
    """
    flagged = [r for r in results if r.get("alert_level") in ("RED", "AMBER")]

    # Filter to reserves that actually need cap changes (not just utilization)
    supply_flagged = [r for r in flagged if r.get("supply_cap_usage_pct") is not None
                      and (r.get("supply_cap_usage_pct") or 0) >= 85]
    borrow_flagged = [r for r in flagged if r.get("borrow_cap_usage_pct") is not None
                      and (r.get("borrow_cap_usage_pct") or 0) >= 85]

    if not supply_flagged and not borrow_flagged:
        logger.info("No reserves flagged for cap changes")
        return None

    PARAM_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = PARAM_REPORTS_DIR / f"{date_str}_cap_change.md"

    lines = []
    lines.append(f"# Supply and Borrow Cap Change Recommendations — {date_str}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")

    # Bullet list of proposed changes
    all_flagged = {(r["symbol"], r["market_name"]): r for r in supply_flagged + borrow_flagged}
    for (symbol, market), r in sorted(all_flagged.items()):
        changes = []
        sc_pct = r.get("supply_cap_usage_pct")
        if sc_pct and sc_pct >= 85:
            rec = _recommend_cap(r["supply_cap"], sc_pct)
            changes.append(f"supply cap {_fmt_num(r['supply_cap'])} → {_fmt_num(rec)}")
        bc_pct = r.get("borrow_cap_usage_pct")
        if bc_pct and bc_pct >= 85:
            rec = _recommend_cap(r["borrow_cap"], bc_pct)
            changes.append(f"borrow cap {_fmt_num(r['borrow_cap'])} → {_fmt_num(rec)}")
        lines.append(f"- **{symbol}** ({r['chain_name']}, {_short_market(r['market_name'])}): {', '.join(changes)}")

    lines.append("")

    # Per-asset sections
    for (symbol, market), r in sorted(all_flagged.items()):
        lines.append(f"## {symbol} ({r['chain_name']} {_short_market(r['market_name'])})")
        lines.append("")

        sc_pct = r.get("supply_cap_usage_pct")
        bc_pct = r.get("borrow_cap_usage_pct")
        util = r.get("utilization_pct", 0)

        if sc_pct and sc_pct >= 85:
            lines.append(f"Supply cap is **{sc_pct:.1f}%** full "
                         f"({_fmt_num(r['total_supply'])} / {_fmt_num(r['supply_cap'])}).")
        if bc_pct and bc_pct >= 85:
            lines.append(f"Borrow cap is **{bc_pct:.1f}%** full "
                         f"({_fmt_num(r['total_borrow'])} / {_fmt_num(r['borrow_cap'])}).")
        if util > 0:
            lines.append(f"Utilization: {util:.1f}% (optimal: {r.get('optimal_pct', 0):.1f}%).")

        lines.append("")

    # Specification table
    lines.append("## Specification")
    lines.append("")
    lines.append("| Instance | Asset | Current Supply Cap | Recommended Supply Cap | Current Borrow Cap | Recommended Borrow Cap |")
    lines.append("|----------|-------|-------------------|----------------------|-------------------|----------------------|")

    for (symbol, market), r in sorted(all_flagged.items()):
        instance = f"{r['chain_name']} {_short_market(r['market_name'])}"
        sc = _fmt_num(r.get("supply_cap"))
        sc_rec = "—"
        sc_pct = r.get("supply_cap_usage_pct")
        if sc_pct and sc_pct >= 85:
            sc_rec = _fmt_num(_recommend_cap(r["supply_cap"], sc_pct))

        bc = _fmt_num(r.get("borrow_cap")) if r.get("borrowing_enabled") else "—"
        bc_rec = "—"
        bc_pct = r.get("borrow_cap_usage_pct")
        if bc_pct and bc_pct >= 85:
            bc_rec = _fmt_num(_recommend_cap(r["borrow_cap"], bc_pct))

        lines.append(f"| {instance} | {symbol} | {sc} | {sc_rec} | {bc} | {bc_rec} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Cap recommendations are heuristic starting points (1.3x at 85%+, 1.5x at 90%+). "
                 "Analyst review required before submission.*")
    lines.append("")

    content = "\n".join(lines)
    path.write_text(content)
    logger.info("Wrote parameter change report to %s", path)
    return path
