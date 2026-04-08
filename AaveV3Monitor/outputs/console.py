"""Console output: summary (default) and verbose modes."""

from __future__ import annotations

from config import thresholds as T


def _fmt_pct(value, na="—") -> str:
    if value is None:
        return f"{na:>7}"
    return f"{value:6.1f}%"


def _fmt_num(value, na="—") -> str:
    if value is None:
        return f"{na:>12}"
    if abs(value) >= 1e9:
        return f"{value/1e9:>9.2f}B"
    if abs(value) >= 1e6:
        return f"{value/1e6:>9.1f}M"
    if abs(value) >= 1e3:
        return f"{value/1e3:>9.1f}K"
    return f"{value:>12,.0f}"


def _short_market(market_name: str) -> str:
    """Shorten market names for display: AaveV3EthereumLido → Lido, AaveV3Base → Base."""
    name = market_name.replace("AaveV3", "")
    # For sub-markets on Ethereum
    if name.startswith("Ethereum") and name != "Ethereum":
        return name.replace("Ethereum", "ETH ")
    return name


def print_summary(results: list[dict], metadata: dict, unknown_chains: set, unknown_markets: set):
    """Print compact summary showing only RED/AMBER alerts + stats."""
    fetch_time = metadata["fetch_time"]
    data_age = metadata.get("data_age_seconds", 0)
    print()
    print("━" * 90)
    print(f"  Aave V3 Monitor — {fetch_time.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"  {metadata['total_reserves']} reserves across {metadata['total_markets']} markets")
    if data_age > 0:
        mins = int(data_age // 60)
        secs = int(data_age % 60)
        print(f"  Data freshness: cached ({mins}m {secs}s old) — use --no-cache for live data")
    else:
        print(f"  Data freshness: LIVE (just fetched from API)")
    print(f"  Cache TTL: 1 hour — data can be up to 60 minutes stale without --no-cache")
    print("━" * 90)

    # Warnings
    if unknown_chains:
        print(f"\n  ⚠️  UNKNOWN CHAIN IDs detected: {unknown_chains}")
        print("     → Update config/chains.py to include these!")
    if unknown_markets:
        print(f"\n  ⚠️  UNKNOWN MARKETS detected: {unknown_markets}")
        print("     → Update config/chains.py KNOWN_MARKETS!")

    # Count by level
    counts = {}
    for r in results:
        level = r.get("alert_level", "GREEN")
        counts[level] = counts.get(level, 0) + 1

    # Print RED alerts
    reds = [r for r in results if r.get("alert_level") == "RED"]
    if reds:
        print(f"\n  🔴 RED ALERTS ({len(reds)})")
        print(f"  {'Asset':<18} {'Chain':<12} {'Market':<14} {'Issue'}")
        print("  " + "─" * 86)
        for r in sorted(reds, key=lambda x: -(x.get("supply_cap_usage_pct") or 0)):
            reasons = r.get("alert_reasons", [])
            reason_str = reasons[0] if reasons else ""
            print(f"  {r['symbol']:<18} {r['chain_name']:<12} {_short_market(r['market_name']):<14} {reason_str}")
            for reason in reasons[1:]:
                print(f"  {'':<18} {'':<12} {'':<14} {reason}")

    # Print AMBER alerts
    ambers = [r for r in results if r.get("alert_level") == "AMBER"]
    if ambers:
        print(f"\n  🟡 AMBER ALERTS ({len(ambers)})")
        print(f"  {'Asset':<18} {'Chain':<12} {'Market':<14} {'Issue'}")
        print("  " + "─" * 86)
        for r in sorted(ambers, key=lambda x: -(x.get("supply_cap_usage_pct") or 0)):
            reasons = r.get("alert_reasons", [])
            reason_str = reasons[0] if reasons else ""
            print(f"  {r['symbol']:<18} {r['chain_name']:<12} {_short_market(r['market_name']):<14} {reason_str}")
            for reason in reasons[1:]:
                print(f"  {'':<18} {'':<12} {'':<14} {reason}")

    # Frozen
    frozen = [r for r in results if r.get("alert_level") == "FROZEN"]
    if frozen:
        print(f"\n  ❄️  FROZEN/PAUSED ({len(frozen)})")
        for r in frozen:
            print(f"     {r['symbol']:<15} {r['chain_name']:<12} {_short_market(r['market_name'])}")

    # Footer
    suppressed = counts.get("SUPPRESSED", 0)
    print()
    print(
        f"  🔴 {counts.get('RED', 0)} RED  "
        f"🟡 {counts.get('AMBER', 0)} AMBER  "
        f"🟢 {counts.get('GREEN', 0)} GREEN  "
        f"❄️  {counts.get('FROZEN', 0)} FROZEN"
        f"  |  {metadata['total_reserves']} reserves"
    )
    if suppressed:
        print(f"  ({suppressed} suppressed via config/notes.md)")
    print("━" * 90)
    print()


def print_verbose(results: list[dict], metadata: dict, unknown_chains: set, unknown_markets: set):
    """Print full comprehensive output with all tables."""
    # Print summary first
    print_summary(results, metadata, unknown_chains, unknown_markets)

    # ── Supply Cap Table ─────────────────────────────────────────────────
    # Only reserves with supply caps (not uncapped)
    capped_supply = [r for r in results
                     if r.get("supply_cap_usage_pct") is not None
                     and r.get("alert_level") not in ("FROZEN", "SUPPRESSED")]
    capped_supply.sort(key=lambda x: -(x.get("supply_cap_usage_pct") or 0))

    print("  ┌─ SUPPLY CAP USAGE " + "─" * 70)
    print(f"  │ {'Alert':<6} {'Asset':<16} {'Chain':<10} {'Market':<14} "
          f"{'Supply':>12} {'Cap':>12} {'Usage%':>7} {'Headroom':>12}")
    print("  │ " + "─" * 85)
    for r in capped_supply:
        alert = r.get("alert_obj")
        emoji = alert.emoji if alert else "🟢"
        print(f"  │ {emoji:<5} {r['symbol']:<16} {r['chain_name']:<10} "
              f"{_short_market(r['market_name']):<14} "
              f"{_fmt_num(r['total_supply'])} {_fmt_num(r['supply_cap'])} "
              f"{_fmt_pct(r.get('supply_cap_usage_pct'))} {_fmt_num(r.get('supply_headroom'))}")
    print(f"  └─ {len(capped_supply)} capped reserves\n")

    # ── Borrow Cap Table ─────────────────────────────────────────────────
    capped_borrow = [r for r in results
                     if r.get("borrow_cap_usage_pct") is not None
                     and r.get("borrowing_enabled")
                     and r.get("alert_level") not in ("FROZEN", "SUPPRESSED")]
    capped_borrow.sort(key=lambda x: -(x.get("borrow_cap_usage_pct") or 0))

    print("  ┌─ BORROW CAP USAGE " + "─" * 69)
    print(f"  │ {'Alert':<6} {'Asset':<16} {'Chain':<10} {'Market':<14} "
          f"{'Borrow':>12} {'Cap':>12} {'Usage%':>7} {'Headroom':>12}")
    print("  │ " + "─" * 85)
    for r in capped_borrow:
        alert = r.get("alert_obj")
        emoji = alert.emoji if alert else "🟢"
        print(f"  │ {emoji:<5} {r['symbol']:<16} {r['chain_name']:<10} "
              f"{_short_market(r['market_name']):<14} "
              f"{_fmt_num(r['total_borrow'])} {_fmt_num(r['borrow_cap'])} "
              f"{_fmt_pct(r.get('borrow_cap_usage_pct'))} {_fmt_num(r.get('borrow_headroom'))}")
    print(f"  └─ {len(capped_borrow)} borrowable capped reserves\n")

    # ── Utilization Table ────────────────────────────────────────────────
    utilized = [r for r in results
                if r.get("utilization_pct", 0) > 0
                and r.get("alert_level") not in ("FROZEN", "SUPPRESSED")]
    utilized.sort(key=lambda x: -(x.get("utilization_pct") or 0))

    print("  ┌─ UTILIZATION RATES " + "─" * 68)
    print(f"  │ {'Alert':<6} {'Asset':<16} {'Chain':<10} {'Market':<14} "
          f"{'Util%':>7} {'Optimal%':>9} {'Δ Optimal':>10}")
    print("  │ " + "─" * 70)
    for r in utilized:
        alert = r.get("alert_obj")
        emoji = alert.emoji if alert else "🟢"
        delta = r.get("utilization_vs_optimal", 0)
        delta_str = f"{delta:+.1f}pp" if delta else "   0.0pp"
        print(f"  │ {emoji:<5} {r['symbol']:<16} {r['chain_name']:<10} "
              f"{_short_market(r['market_name']):<14} "
              f"{_fmt_pct(r.get('utilization_pct'))} {_fmt_pct(r.get('optimal_pct'))} "
              f"{delta_str:>10}")
    print(f"  └─ {len(utilized)} active reserves\n")

    # ── Low Supply Section (USD-based) ──────────────────────────────────
    low_supply = [r for r in results
                  if r.get("total_supply_usd", 0) > 0
                  and r.get("total_supply_usd", 0) < T.MIN_SUPPLY_USD_MAIN
                  and r.get("alert_level") not in ("FROZEN", "SUPPRESSED")]
    if low_supply:
        low_supply.sort(key=lambda x: x.get("total_supply_usd", 0))
        print(f"  ┌─ LOW SUPPLY (<${T.MIN_SUPPLY_USD_MAIN/1e3:.0f}K USD) " + "─" * 51)
        print(f"  │ {'Asset':<16} {'Chain':<10} {'Market':<14} "
              f"{'Price':>10} {'Supply (USD)':>14} {'Supply (tkn)':>14} {'Cap%':>7}")
        print("  │ " + "─" * 82)
        for r in low_supply:
            cap_pct = _fmt_pct(r.get("supply_cap_usage_pct"))
            price = f"${r.get('price_usd', 0):,.2f}" if r.get("price_usd", 0) < 100 else f"${r.get('price_usd', 0):,.0f}"
            supply_usd = f"${r.get('total_supply_usd', 0):,.0f}"
            print(f"  │ {r['symbol']:<16} {r['chain_name']:<10} "
                  f"{_short_market(r['market_name']):<14} "
                  f"{price:>10} {supply_usd:>14} {_fmt_num(r['total_supply'])} {cap_pct}")
        print(f"  └─ {len(low_supply)} low-supply reserves\n")
