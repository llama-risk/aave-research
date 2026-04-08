"""Compute derived cap and utilization metrics for each reserve."""

from __future__ import annotations


def compute_metrics(row: dict) -> dict:
    """Add derived fields to a reserve row.

    Args:
        row: dict with raw fields from fetcher.py

    Returns:
        New dict with all original fields + computed fields.
    """
    r = dict(row)

    supply_cap = r["supply_cap"]
    total_supply = r["total_supply"]
    borrow_cap = r["borrow_cap"]
    total_borrow = r["total_borrow"]
    utilization = r["utilization_rate"]
    optimal = r["optimal_usage_rate"]

    # ── Supply cap metrics ───────────────────────────────────────────────
    # cap == 0 means uncapped
    # cap == 1 with supply >> 1 means "deprecated / effectively disabled"
    is_deprecated_supply = (supply_cap == 1 and total_supply > 1)
    r["is_deprecated_supply"] = is_deprecated_supply

    if is_deprecated_supply:
        # Deprecated: cap set to 1 to block new supply, existing supply remains
        r["supply_cap_usage_pct"] = None
        r["supply_headroom"] = None
        r["is_uncapped_supply"] = False
    elif supply_cap and supply_cap > 0:
        r["supply_cap_usage_pct"] = (total_supply / supply_cap) * 100.0
        r["supply_headroom"] = supply_cap - total_supply
        r["is_uncapped_supply"] = False
    else:
        r["supply_cap_usage_pct"] = None
        r["supply_headroom"] = None
        r["is_uncapped_supply"] = True

    # ── Borrow cap metrics ───────────────────────────────────────────────
    # cap == 0 means uncapped; cap == 1 with borrows >> 1 means disabled
    is_deprecated_borrow = (borrow_cap == 1 and total_borrow > 10)
    r["is_deprecated_borrow"] = is_deprecated_borrow

    if is_deprecated_borrow or not r.get("borrowing_enabled"):
        r["borrow_cap_usage_pct"] = None
        r["borrow_headroom"] = None
        r["is_uncapped_borrow"] = None  # N/A
    elif borrow_cap and borrow_cap > 1:
        r["borrow_cap_usage_pct"] = (total_borrow / borrow_cap) * 100.0
        r["borrow_headroom"] = borrow_cap - total_borrow
        r["is_uncapped_borrow"] = False
    else:
        r["borrow_cap_usage_pct"] = None
        r["borrow_headroom"] = None
        r["is_uncapped_borrow"] = True

    # ── USD metrics ──────────────────────────────────────────────────────
    price = r.get("price_usd", 0.0)
    r["supply_cap_usd"] = supply_cap * price if supply_cap and not is_deprecated_supply else None
    r["borrow_cap_usd"] = borrow_cap * price if borrow_cap and borrow_cap > 1 and r.get("borrowing_enabled") else None
    r["supply_headroom_usd"] = r["supply_headroom"] * price if r.get("supply_headroom") is not None else None
    r["borrow_headroom_usd"] = r["borrow_headroom"] * price if r.get("borrow_headroom") is not None else None

    # ── Utilization metrics ──────────────────────────────────────────────
    r["utilization_pct"] = utilization * 100.0
    r["optimal_pct"] = optimal * 100.0
    r["utilization_vs_optimal"] = (utilization - optimal) * 100.0  # pp above/below
    r["above_optimal"] = utilization > optimal

    return r
