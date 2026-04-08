"""Multi-step alerting: raw classification → contextual scoring → trend context."""

from __future__ import annotations

import re
import logging
from dataclasses import dataclass, field
from pathlib import Path

from config import thresholds as T

logger = logging.getLogger(__name__)

NOTES_PATH = Path(__file__).parent.parent / "config" / "notes.md"


@dataclass
class Alert:
    level: str  # "RED" | "AMBER" | "GREEN" | "FROZEN" | "SUPPRESSED"
    reasons: list[str] = field(default_factory=list)

    @property
    def emoji(self) -> str:
        return {
            "RED":        "🔴",
            "AMBER":      "🟡",
            "GREEN":      "🟢",
            "FROZEN":     "❄️",
            "SUPPRESSED": "🔇",
        }.get(self.level, "⚪")

    def __str__(self) -> str:
        return f"{self.emoji} {self.level}"


def _load_suppressions() -> set[str]:
    """Parse config/notes.md for suppressed assets.

    Format: lines under ## Suppressions starting with "- SYMBOL/Chain/Market"
    Returns set of "SYMBOL/Chain/Market" keys (lowercased for matching).
    """
    if not NOTES_PATH.exists():
        return set()
    text = NOTES_PATH.read_text()
    suppressions = set()
    in_section = False
    for line in text.splitlines():
        if line.strip().startswith("## Suppressions"):
            in_section = True
            continue
        if in_section and line.strip().startswith("## "):
            break
        if in_section and line.strip().startswith("- ") and not line.strip().startswith("<!-- "):
            # Extract "SYMBOL/Chain/Market" before the colon
            match = re.match(r"^-\s+(\S+)", line.strip())
            if match:
                suppressions.add(match.group(1).lower())
    return suppressions


_suppressions_cache: set[str] | None = None


def _get_suppressions() -> set[str]:
    global _suppressions_cache
    if _suppressions_cache is None:
        _suppressions_cache = _load_suppressions()
    return _suppressions_cache


def is_suppressed(row: dict) -> bool:
    """Check if a reserve matches a suppression in notes.md."""
    suppressions = _get_suppressions()
    if not suppressions:
        return False
    key = f"{row['symbol']}/{row['chain_name']}/{row['market_name']}".lower()
    return key in suppressions


def score(row: dict, trend_7d: dict | None = None, trend_30d: dict | None = None) -> Alert:
    """Score a single reserve (with computed metrics) as RED/AMBER/GREEN/FROZEN/SUPPRESSED.

    Args:
        row:       Dict with all fields from metrics.compute_metrics()
        trend_7d:  Optional dict with 7d trends {metric_name: pp_change}
        trend_30d: Optional dict with 30d trends {metric_name: pp_change}
    """
    # Check suppression first
    if is_suppressed(row):
        return Alert(level="SUPPRESSED", reasons=["Suppressed via config/notes.md"])

    # Frozen/paused — separate category
    if row.get("is_frozen") or row.get("is_paused"):
        reasons = []
        if row.get("is_frozen"):
            reasons.append("Reserve is FROZEN")
        if row.get("is_paused"):
            reasons.append("Reserve is PAUSED")
        return Alert(level="FROZEN", reasons=reasons)

    # Deprecated assets (cap set to 1 to block new activity)
    # Only treat as FROZEN if both supply and borrow are deprecated/disabled
    is_dep_supply = row.get("is_deprecated_supply", False)
    is_dep_borrow = row.get("is_deprecated_borrow", False)
    borrow_enabled = row.get("borrowing_enabled", False)

    if is_dep_supply and (is_dep_borrow or not borrow_enabled):
        return Alert(level="FROZEN", reasons=["Deprecated (caps set to 1 to block new activity)"])

    reasons_red: list[str] = []
    reasons_amber: list[str] = []
    label = f"{row['symbol']} on {row['chain_name']} ({row['market_name']})"

    # ── Step A+B: Supply cap scoring ─────────────────────────────────────
    sc_pct = row.get("supply_cap_usage_pct")
    if sc_pct is not None:
        if row.get("supply_cap_reached") or sc_pct >= T.SUPPLY_CAP_RED:
            reasons_red.append(
                f"Supply cap {sc_pct:.1f}% full "
                f"({row['total_supply']:,.0f} / {row['supply_cap']:,.0f})"
            )
        elif sc_pct >= T.SUPPLY_CAP_AMBER:
            reasons_amber.append(
                f"Supply cap {sc_pct:.1f}% full "
                f"({row['total_supply']:,.0f} / {row['supply_cap']:,.0f})"
            )

    # ── Step A+B: Borrow cap scoring ─────────────────────────────────────
    bc_pct = row.get("borrow_cap_usage_pct")
    if bc_pct is not None:
        if row.get("borrow_cap_reached") or bc_pct >= T.BORROW_CAP_RED:
            reasons_red.append(
                f"Borrow cap {bc_pct:.1f}% full "
                f"({row['total_borrow']:,.0f} / {row['borrow_cap']:,.0f})"
            )
        elif bc_pct >= T.BORROW_CAP_AMBER:
            reasons_amber.append(
                f"Borrow cap {bc_pct:.1f}% full "
                f"({row['total_borrow']:,.0f} / {row['borrow_cap']:,.0f})"
            )

    # ── Step A+B: Utilization scoring ────────────────────────────────────
    util_pct = row.get("utilization_pct", 0.0)
    optimal_pct = row.get("optimal_pct", 0.0)
    util_vs_opt = row.get("utilization_vs_optimal", 0.0)

    if util_pct >= T.UTILIZATION_RED:
        reasons_red.append(
            f"Utilization {util_pct:.1f}% (optimal: {optimal_pct:.1f}%)"
        )
    elif util_pct >= T.UTILIZATION_AMBER:
        reasons_amber.append(
            f"Utilization {util_pct:.1f}% (optimal: {optimal_pct:.1f}%)"
        )
    elif util_vs_opt >= T.UTILIZATION_ABOVE_OPTIMAL_AMBER:
        reasons_amber.append(
            f"Utilization {util_pct:.1f}% is {util_vs_opt:+.1f}pp above optimal {optimal_pct:.1f}%"
        )

    # ── Step C: Trend context (only for flagged assets) ──────────────────
    if (reasons_red or reasons_amber) and trend_7d:
        for metric, change in trend_7d.items():
            if change is not None and change >= T.TREND_7D_WORSENING:
                reasons_amber.append(f"7d trend: {metric} {change:+.1f}pp (worsening)")
    if (reasons_red or reasons_amber) and trend_30d:
        for metric, change in trend_30d.items():
            if change is not None and change >= T.TREND_30D_WORSENING:
                reasons_amber.append(f"30d trend: {metric} {change:+.1f}pp (sustained)")

    if reasons_red:
        return Alert(level="RED", reasons=reasons_red + reasons_amber)
    if reasons_amber:
        return Alert(level="AMBER", reasons=reasons_amber)
    return Alert(level="GREEN", reasons=[])
