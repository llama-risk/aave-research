"""Historical snapshot management and trend computation."""

from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)

HISTORY_DIR = Path(__file__).parent.parent / "data" / "history"


def _load_snapshot(date_str: str) -> pd.DataFrame | None:
    """Load the latest snapshot for a given YYYY-MM-DD date.

    Supports both old format (YYYY-MM-DD.csv) and new format (YYYY-MM-DD_HHMM.csv).
    If multiple timestamped files exist for the same date, uses the latest.
    """
    # Try exact match first (legacy format)
    path = HISTORY_DIR / f"{date_str}.csv"
    if path.exists():
        try:
            return pd.read_csv(path)
        except Exception as exc:
            logger.warning("Could not read snapshot %s: %s", path, exc)

    # Find timestamped files for this date (YYYY-MM-DD_HHMM.csv)
    if not HISTORY_DIR.exists():
        return None
    candidates = sorted(HISTORY_DIR.glob(f"{date_str}_*.csv"))
    if not candidates:
        return None
    # Use the latest one
    try:
        return pd.read_csv(candidates[-1])
    except Exception as exc:
        logger.warning("Could not read snapshot %s: %s", candidates[-1], exc)
        return None


def _find_row(df: pd.DataFrame, symbol: str, chain_name: str, market_name: str) -> pd.Series | None:
    """Find a specific reserve in a snapshot DataFrame."""
    mask = (
        (df["symbol"].str.upper() == symbol.upper()) &
        (df["chain_name"].str.lower() == chain_name.lower()) &
        (df["market_name"].str.lower() == market_name.lower())
    )
    rows = df[mask]
    if rows.empty:
        return None
    return rows.iloc[0]


def get_trend(
    symbol: str,
    chain_name: str,
    market_name: str,
    metrics: list[str],
    days: int = 7,
) -> dict[str, float | None]:
    """Compute pct-point change in specified metrics over N days.

    Args:
        symbol, chain_name, market_name: Reserve identifier
        metrics: List of column names to compute trends for
                 (e.g., ["utilization_pct", "supply_cap_usage_pct"])
        days: Lookback window (7 or 30)

    Returns:
        Dict mapping metric_name → pp change (positive = increasing), or None if insufficient data
    """
    today = datetime.now(timezone.utc).date()
    result = {m: None for m in metrics}

    # Find newest and oldest available snapshots in the window
    newest_row = None
    oldest_row = None
    newest_date = None
    oldest_date = None

    for offset in range(days + 1):
        date = today - timedelta(days=offset)
        date_str = date.strftime("%Y-%m-%d")
        df = _load_snapshot(date_str)
        if df is None:
            continue
        row = _find_row(df, symbol, chain_name, market_name)
        if row is None:
            continue

        if newest_row is None:
            newest_row = row
            newest_date = date_str
        oldest_row = row
        oldest_date = date_str

    if newest_row is None or oldest_row is None or newest_date == oldest_date:
        return result

    for m in metrics:
        new_val = newest_row.get(m)
        old_val = oldest_row.get(m)
        if new_val is not None and old_val is not None and not pd.isna(new_val) and not pd.isna(old_val):
            result[m] = float(new_val) - float(old_val)  # pp change

    return result


def save_snapshot(results: list[dict], timestamp: str | None = None) -> Path:
    """Save a snapshot of all results to data/history/YYYY-MM-DD_HHMM.csv.

    Args:
        results: List of enriched reserve dicts (after metrics + alerts)
        timestamp: YYYY-MM-DD_HHMM string; defaults to now UTC

    Returns:
        Path to the written CSV file.
    """
    if timestamp is None:
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M")

    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    path = HISTORY_DIR / f"{timestamp}.csv"

    rows = []
    for r in results:
        rows.append({
            "symbol":                r.get("symbol"),
            "chain_name":            r.get("chain_name"),
            "market_name":           r.get("market_name"),
            "supply_cap":            r.get("supply_cap"),
            "total_supply":          r.get("total_supply"),
            "supply_cap_usage_pct":  r.get("supply_cap_usage_pct"),
            "borrow_cap":            r.get("borrow_cap"),
            "total_borrow":          r.get("total_borrow"),
            "borrow_cap_usage_pct":  r.get("borrow_cap_usage_pct"),
            "utilization_pct":       r.get("utilization_pct"),
            "optimal_pct":           r.get("optimal_pct"),
            "utilization_vs_optimal": r.get("utilization_vs_optimal"),
            "borrowing_enabled":     r.get("borrowing_enabled"),
            "is_frozen":             r.get("is_frozen"),
            "is_paused":             r.get("is_paused"),
            "alert_level":           r.get("alert_level"),
        })

    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)
    logger.info("Saved snapshot to %s (%d rows)", path, len(df))
    return path
