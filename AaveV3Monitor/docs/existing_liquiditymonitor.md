# Existing LiquidityMonitor — Architecture Reference

> For context when building AaveV3Monitor. The LiquidityMonitor focuses on DEX liquidity depth
> vs Aave V3 collateral. This new project focuses on protocol-level utilization and cap monitoring.

## Location
`/Users/Marti/Desktop/LlamaRisk/LiquidityMonitor/`

## What It Monitors
- **DEX liquidity depth** vs Aave V3 collateral per asset per chain
- Maximum liquidatable amount before slippage exceeds the liquidation bonus
- Coverage ratio: DEX depth / total collateral (RED if <20%, AMBER if <50%)
- Stress scenario: impact of liquidating 20% of collateral
- 7-day trend in max liquidatable amount

## Tech Stack
- Python 3.9+, pandas, requests, python-dotenv
- CLI-driven (no web framework)
- Modular: config/ → data_sources/ → core/ → outputs/
- File-based cache (MD5 hashed, 1-hour TTL)
- Daily CSV snapshots for trend analysis

## File Structure
```
LiquidityMonitor/
├── run.py                  # CLI entry point
├── requirements.txt        # pandas, requests, python-dotenv
├── config/
│   ├── chains.py           # 8 chains (ETH, ARB, OP, POLY, AVAX, BASE, BSC, Mantle excluded)
│   └── assets.py           # 28 assets with addresses, decimals, liq bonuses
├── core/
│   ├── slippage_curve.py   # DEX slippage curve builder
│   ├── metrics.py          # Coverage, stress, at-risk computation
│   ├── alerts.py           # RED/AMBER/GREEN scoring (Alert dataclass reusable)
│   └── trend.py            # 7-day trend from CSV snapshots
├── data_sources/
│   ├── defillama.py        # Aave V3 collateral from DefiLlama
│   ├── paraswap.py         # DEX quotes (primary)
│   ├── kyberswap.py        # DEX quotes (fallback)
│   ├── odos.py             # DEX quotes (fallback)
│   └── cache.py            # File-based 1h TTL cache (REUSABLE)
├── outputs/
│   ├── report.py           # Markdown report generation
│   └── forum_post.py       # Governance forum post draft
├── data/
│   ├── cache/              # ~1,300+ cached API responses
│   └── history/            # Daily CSV snapshots
└── reports/                # Generated reports
```

## Reusable Patterns
1. **Alert dataclass** (`core/alerts.py`): `Alert(level, reasons)` with `.color`, `.emoji` properties
2. **Cache module** (`data_sources/cache.py`): `get(key)` / `set(key, value)` with 1h TTL
3. **Trend pattern** (`core/trend.py`): Daily CSV snapshots → N-day % change lookup
4. **CLI pattern** (`run.py`): argparse with `--report`, `--post`, `--no-cache`, `--verbose`
5. **Console table formatting**: `_fmt_usd()`, `_fmt_pct()` helpers
