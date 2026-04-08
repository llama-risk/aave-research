"""Alert thresholds for cap and utilization monitoring.

These will be refined over time as we calibrate the monitor.
"""

# ── Utilization rate thresholds ──────────────────────────────────────────────
# These are absolute thresholds; contextual scoring also checks vs uOptimal
UTILIZATION_RED = 95.0          # % — critical, near 100% = borrowers can't withdraw
UTILIZATION_AMBER = 85.0        # % — elevated

# How far above optimal to flag as AMBER (percentage points)
UTILIZATION_ABOVE_OPTIMAL_AMBER = 10.0  # pp above uOptimal

# ── Supply cap usage thresholds (total_supply / supply_cap * 100) ────────────
SUPPLY_CAP_RED = 95.0           # % — effectively at cap, new supply blocked
SUPPLY_CAP_AMBER = 85.0         # % — approaching cap

# ── Borrow cap usage thresholds (total_borrow / borrow_cap * 100) ────────────
BORROW_CAP_RED = 95.0           # % — effectively at cap, new borrows blocked
BORROW_CAP_AMBER = 85.0         # % — approaching cap

# ── Trend thresholds (pct-point change) ──────────────────────────────────────
TREND_7D_WORSENING = 5.0        # pp increase in 7d → situation getting worse
TREND_30D_WORSENING = 10.0      # pp increase in 30d → sustained deterioration

# ── Minimum thresholds (for sectioning, not removal) ────────────────────────
MIN_SUPPLY_USD_MAIN = 100_000   # $100K — reserves below this go to "Low Supply" section
