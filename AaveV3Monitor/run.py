#!/usr/bin/env python3
"""Aave V3 Cap & Utilization Monitor — main CLI.

Usage:
    python run.py                      # summary mode: RED/AMBER alerts only
    python run.py --verbose            # full tables for all reserves
    python run.py --report             # + write monitoring markdown report
    python run.py --param-report       # + generate parameter change report
    python run.py --no-cache           # bypass 1h cache
    python run.py --chain ethereum     # filter to one chain
    python run.py --red-only           # only show RED alerts
"""

import argparse
import logging
import sys
from pathlib import Path

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).parent))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-7s %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("run")

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)


def parse_args():
    p = argparse.ArgumentParser(description="Aave V3 Cap & Utilization Monitor")
    p.add_argument("--verbose", "-v", action="store_true",
                   help="Full comprehensive output (all reserves, all metrics)")
    p.add_argument("--report", action="store_true",
                   help="Write monitoring markdown report")
    p.add_argument("--param-report", action="store_true",
                   help="Generate parameter change report for flagged assets")
    p.add_argument("--no-cache", action="store_true",
                   help="Bypass 1-hour disk cache")
    p.add_argument("--chain", type=str, default=None,
                   help="Filter to one chain (e.g., 'ethereum', 'base')")
    p.add_argument("--red-only", action="store_true",
                   help="Only show RED alerts")
    p.add_argument("--sanity-check", action="store_true",
                   help="Run on-chain RPC validation (standalone)")
    p.add_argument("--skip-sanity", action="store_true",
                   help="Skip sanity check when generating reports (dev speed)")
    p.add_argument("--debug", action="store_true",
                   help="Debug logging")
    return p.parse_args()


def main():
    args = parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    # ── Step 1: Fetch data ───────────────────────────────────────────────
    from core.fetcher import fetch_all_reserves, disable_cache
    if args.no_cache:
        disable_cache()

    logger.info("Fetching Aave V3 reserve data...")
    df, metadata = fetch_all_reserves()

    # ── Step 2: Check coverage ───────────────────────────────────────────
    from config.chains import check_coverage
    unknown_chains, unknown_markets = check_coverage(
        metadata["chain_ids_found"],
        metadata["market_names_found"],
    )
    if unknown_chains:
        logger.warning("⚠️  UNKNOWN CHAIN IDs: %s — update config/chains.py!", unknown_chains)
    if unknown_markets:
        logger.warning("⚠️  UNKNOWN MARKETS: %s — update config/chains.py!", unknown_markets)

    # ── Step 3: Filter by chain if requested ─────────────────────────────
    if args.chain:
        chain_filter = args.chain.lower()
        df = df[df["chain_name"].str.lower().str.contains(chain_filter)]
        logger.info("Filtered to chain '%s': %d reserves", args.chain, len(df))

    # ── Step 4: Compute metrics ──────────────────────────────────────────
    from core.metrics import compute_metrics
    results = [compute_metrics(row) for _, row in df.iterrows()]

    # ── Step 5: Score alerts ─────────────────────────────────────────────
    from core.alerts import score
    from core.trend import get_trend

    trend_metrics = ["utilization_pct", "supply_cap_usage_pct", "borrow_cap_usage_pct"]

    for r in results:
        # Score with trends (only computed for non-GREEN after initial score)
        alert = score(r)

        # If flagged, compute trends
        trend_7d = None
        trend_30d = None
        if alert.level in ("RED", "AMBER"):
            trend_7d = get_trend(
                r["symbol"], r["chain_name"], r["market_name"],
                trend_metrics, days=7,
            )
            trend_30d = get_trend(
                r["symbol"], r["chain_name"], r["market_name"],
                trend_metrics, days=30,
            )
            # Re-score with trend context
            alert = score(r, trend_7d=trend_7d, trend_30d=trend_30d)

        r["alert_level"] = alert.level
        r["alert_reasons"] = alert.reasons
        r["alert_obj"] = alert
        r["trend_7d"] = trend_7d
        r["trend_30d"] = trend_30d

    # ── Step 6: Filter if --red-only ─────────────────────────────────────
    display_results = results
    if args.red_only:
        display_results = [r for r in results if r.get("alert_level") == "RED"]

    # ── Step 7: Console output ───────────────────────────────────────────
    from outputs.console import print_summary, print_verbose
    if args.verbose:
        print_verbose(display_results, metadata, unknown_chains, unknown_markets)
    else:
        print_summary(display_results, metadata, unknown_chains, unknown_markets)

    # ── Step 8: Save daily snapshot ──────────────────────────────────────
    from core.trend import save_snapshot
    save_snapshot(results)

    # ── Step 9: Sanity check ─────────────────────────────────────────────
    sanity_report = None
    needs_sanity = args.sanity_check or (
        (args.report or args.param_report) and not args.skip_sanity
    )

    price_report = None
    if needs_sanity:
        from core.sanity_check import (
            validate, print_sanity_report,
            validate_prices, print_price_report,
        )
        logger.info("Running on-chain sanity check...")
        sanity_report = validate(results)
        print_sanity_report(sanity_report)

        logger.info("Running oracle price validation...")
        price_report = validate_prices(results)
        print_price_report(price_report)

        if sanity_report.hard_fails:
            print("  ❌ ABORTING report generation — fix cap mismatches first!")
            print("     Run with --no-cache to refresh GraphQL data, or investigate on-chain.")
            sys.exit(1)
        if price_report.hard_fails:
            print("  ❌ ABORTING report generation — oracle price mismatch detected!")
            sys.exit(1)

    # ── Step 10: Write reports ───────────────────────────────────────────
    if args.report:
        from outputs.report import write_report
        path = write_report(results, metadata, unknown_chains, unknown_markets,
                           sanity_report=sanity_report)
        print(f"  📄 Report written to: {path}")

    if args.param_report:
        from outputs.param_change import write_param_report
        path = write_param_report(results)
        if path:
            print(f"  📄 Parameter change report written to: {path}")
        else:
            print("  ℹ️  No reserves flagged for cap changes — no param report generated")


if __name__ == "__main__":
    main()
