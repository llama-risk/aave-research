# Aave V3 Cap & Utilization Monitor

Monitors supply caps, borrow caps, and utilization rates across **all Aave V3 instances** (19 chains, 22 markets, ~280 reserves). Flags reserves approaching cap limits or high utilization, and generates parameter change reports for governance.

## Quick Start

```bash
pip install -r requirements.txt
cp .env.example .env          # add your RPC keys (optional — only needed for sanity checks)
python run.py                 # summary: RED/AMBER alerts only
```

## Usage

```bash
python run.py                      # summary mode: RED/AMBER alerts
python run.py --verbose            # full tables: all reserves, all metrics, USD values
python run.py --report             # + write monitoring report to reports/
python run.py --param-report       # + generate cap change report to Aave_Parameter_changes/
python run.py --sanity-check       # cross-validate GraphQL data against on-chain RPC
python run.py --no-cache           # bypass 1h GraphQL cache (live data)
python run.py --chain ethereum     # filter to one chain
python run.py --red-only           # only show RED alerts
python run.py --report --param-report --no-cache   # full run
```

## What It Monitors

| Metric | RED Threshold | AMBER Threshold |
|--------|-------------|-----------------|
| Supply cap usage | >= 95% | >= 85% |
| Borrow cap usage | >= 95% | >= 85% |
| Utilization rate | >= 95% | >= 85% or >10pp above optimal |

Reserves with `cap = 1` (deprecated) are auto-classified as FROZEN, not RED.

## Output Modes

- **Summary** (default): RED/AMBER alerts only + stats footer
- **Verbose** (`--verbose`): Full supply cap, borrow cap, and utilization tables + low supply section (USD-based)
- **Monitoring report** (`--report`): Markdown report saved to `reports/`
- **Parameter change report** (`--param-report`): Governance-style cap change recommendations saved to `Aave_Parameter_changes/cap_reports/`

## Sanity Checks

With `--sanity-check` or when generating reports, the monitor cross-validates GraphQL data against on-chain RPC:

1. **Cap validation**: Reads `Pool.getConfiguration()` bitmap — caps must match exactly
2. **Supply/borrow validation**: Reads `DataProvider.getReserveData()` — <1% tolerance (interest accrual)
3. **Oracle price validation**: Calls `latestRoundData()` / `latestAnswer()` on each reserve's Chainlink oracle — prices must match within 1%, staleness >24h flagged

Requires RPC keys in `.env` (see `.env.example`). Without keys, sanity checks are skipped gracefully.

## Configuration

- **`config/thresholds.py`** — Alert thresholds (RED/AMBER cutoffs, staleness limits)
- **`config/notes.md`** — Per-asset suppressions and analyst notes (edit to silence known alerts)
- **`config/chains.py`** — Chain registry + missing-chain detection
- **`config/contracts.py`** — PoolAddressesProvider addresses per market + RPC URLs

## Data Source

Single GraphQL query to `api.v3.aave.com/graphql` — no auth required, returns all reserves across all chains in ~1-2 seconds. Data is real-time (verified against on-chain).

## Documentation

See `docs/` for deep dives:
- `data_sources.md` — API reference, query format, fallback options
- `oracle_validation.md` — Oracle types (Standard CL vs Partial CL), calling convention, cross-chain test results
- `governance_post_format.md` — Template for Chaos-Labs-style cap change posts
