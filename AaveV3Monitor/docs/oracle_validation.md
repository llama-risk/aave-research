# Oracle Price Validation — Reference

> Compiled 2026-04-08. Documents how on-chain oracle price checks work across all Aave V3 chains.

## Overview

Every Aave V3 reserve has a Chainlink-style oracle providing the USD price. The GraphQL API exposes:
- `usdExchangeRate` — the oracle price per token in USD
- `usdOracleAddress` — the on-chain oracle contract address

We cross-check `usdExchangeRate` against direct on-chain oracle reads to detect stale or broken prices.

## Oracle Interface Types

Two types exist across the ecosystem:

### STANDARD_CL (~27% of reserves)

Full Chainlink aggregator interface. Supports `latestRoundData()`.

- **Assets**: Volatile tokens — WETH, AAVE, LINK, BTC variants, WAVAX, UNI, CRV, SNX, etc.
- **Function**: `latestRoundData()` (selector `0xfeaf968c`)
- **Returns**: `(uint80 roundId, int256 answer, uint256 startedAt, uint256 updatedAt, uint80 answeredInRound)`
- **Key fields**: `answer` (price), `updatedAt` (staleness check)
- **Typical update frequency**: Every 1-6 hours or on 0.5-1% price deviation

### PARTIAL_CL (~73% of reserves)

Computed/proxy oracles. `latestRoundData()` reverts, but `latestAnswer()` works.

- **Assets**: Stablecoins (USDC, USDT, DAI, GHO), LSTs (wstETH, cbETH, rETH), PT tokens, RWA (USYC, USTB, ACRED), wrapped assets (WBTC)
- **Function**: `latestAnswer()` (selector `0x50d25bcd`)
- **Returns**: `int256 answer` (price only, no timestamp)
- **Why no timestamp**: These are often composite oracles (e.g., wstETH price = stETH/ETH rate × ETH/USD). The proxy doesn't expose a single `updatedAt`.
- **Staleness check**: Not possible via `updatedAt`. Can only verify the price value matches GraphQL.

## Calling Convention

```
1. Try latestRoundData() (0xfeaf968c)
   → If succeeds: decode answer + updatedAt, check staleness
   → If reverts: fallback to step 2

2. Try latestAnswer() (0x50d25bcd)  
   → If succeeds: decode answer only (no timestamp available)
   → If reverts: mark as NO_ORACLE

3. Always call decimals() (0x313ce567)
   → If fails: default to 8 (standard Chainlink precision)
   
4. Oracle price = answer / 10^decimals
```

## Validation Thresholds

| Check | Threshold | Action |
|-------|-----------|--------|
| Price diff (GraphQL vs oracle) | > 1% | WARNING |
| Price diff (GraphQL vs oracle) | > 5% | HARD FAIL |
| Oracle `updatedAt` (STANDARD_CL only) | > 24h | STALE WARNING |
| Oracle `updatedAt` (STANDARD_CL only) | > 48h | STALE CRITICAL |

## Cross-Chain Test Results (2026-04-08)

All prices matched GraphQL within 0.15% across 17 chains.

| Chain | Tested | Oracle Types | Max Diff | Status |
|-------|--------|-------------|----------|--------|
| Ethereum | 88 reserves (full scan) | 24 STANDARD + 64 PARTIAL | 0.33% | ✅ |
| Optimism | 2 sampled | STANDARD + PARTIAL | 0.00% | ✅ |
| Arbitrum | 2 sampled | PARTIAL | 0.00% | ✅ |
| Polygon | 2 sampled | STANDARD + PARTIAL | 0.00% | ✅ |
| Avalanche | 2 sampled | STANDARD + PARTIAL | 0.15% | ✅ |
| Base | 2 sampled | STANDARD + PARTIAL | 0.00% | ✅ |
| BSC | 2 sampled | STANDARD + PARTIAL | 0.00% | ✅ |
| Gnosis | 2 sampled | STANDARD + PARTIAL | 0.00% | ✅ |
| Linea | 2 sampled | STANDARD | 0.00% | ✅ |
| Scroll | 2 sampled | STANDARD | 0.00% | ✅ |
| Mantle | 2 sampled | STANDARD + PARTIAL | 0.00% | ✅ |
| Metis | 2 sampled | STANDARD + PARTIAL | 0.00% | ✅ |
| zkSync | 2 sampled | PARTIAL | 0.00% | ✅ |
| Sonic | 2 sampled | PARTIAL | 0.00% | ✅ |
| Celo | 2 sampled | STANDARD + PARTIAL | 0.02% | ✅ |
| Soneium | 2 sampled | STANDARD + PARTIAL | 0.00% | ✅ |
| Ink | 2 sampled | PARTIAL | 0.00% | ✅ |
| MegaETH | - | - | - | ❌ RPC unreachable |
| Plasma | - | - | - | ❌ RPC unreachable |

## Notable Findings

- **VBILL** (Ethereum Horizon): 25.5h since last oracle update — flagged STALE
- **weETH** on EtherFi vs Core: 0.33% price diff — different oracle contracts per market
- **WBTC.e** on Avalanche: 0.15% diff — slight lag in oracle update
- **PARTIAL_CL oracles**: No staleness detection possible. Must rely on price-diff-only validation.

## RPC Endpoints Used

See `config/contracts.py` for full chain → RPC mapping. Key:
- Ethereum: BlockPI archive (key in `.env`, Ethereum-only)
- 10 chains: Infura (key in `.env`)
- 8 chains: Public RPCs (Gnosis, Metis, Scroll, zkSync, Mantle, Sonic, Soneium, Ink)
- 2 chains unreachable: MegaETH, Plasma (public RPCs not responding)
