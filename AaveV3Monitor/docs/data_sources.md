# Aave V3 Monitor — Data Sources Reference

> Compiled 2026-04-08 during initial research. These are stable APIs/contracts, not time-sensitive.

## 1. Aave V3 GraphQL API (PRIMARY — recommended)

- **Endpoint:** `https://api.v3.aave.com/graphql`
- **Auth:** None required
- **Method:** POST with `{"query": "..."}` body
- **Coverage:** All Aave V3 markets across all chains (~20 markets, ~255 reserves, 17+ chains)
- **Source:** Aave official API (likely backing the Aave App + BGD's dash.onaave.com)

### Working Query (confirmed 2026-04-08)

```graphql
{
  markets(request: { chainIds: [1, 10, 42161, 137, 43114, 8453, 100, 1088, 56, 59144, 534352, 324, 42220, 5000, 146, 1868, 57073, 9745, 4326] }) {
    name
    chain { chainId name }
    address
    totalMarketSize
    reserves {
      underlyingToken { symbol name decimals address }
      supplyInfo {
        supplyCap { amount { value } }
        supplyCapReached
        total { value }
        maxLTV { value }
        liquidationThreshold { value }
        apy { value }
        canBeCollateral
      }
      borrowInfo {
        borrowCap { amount { value } }
        borrowCapReached
        total { amount { value } }
        availableLiquidity { amount { value } }
        utilizationRate { value }
        reserveFactor { value }
        apy { value }
        optimalUsageRate { value }
      }
      isFrozen
      isPaused
    }
  }
}
```

### Fields Available

| Field | Path | Notes |
|-------|------|-------|
| Supply cap | `supplyInfo.supplyCap.amount.value` | 0 = no cap set |
| Supply cap reached | `supplyInfo.supplyCapReached` | Boolean |
| Total supply | `supplyInfo.total.value` | USD value |
| Borrow cap | `borrowInfo.borrowCap.amount.value` | 0 = no cap set |
| Borrow cap reached | `borrowInfo.borrowCapReached` | Boolean |
| Total borrow | `borrowInfo.total.amount.value` | USD value |
| Available liquidity | `borrowInfo.availableLiquidity.amount.value` | USD |
| Utilization rate | `borrowInfo.utilizationRate.value` | Decimal (0.85 = 85%) |
| Optimal usage rate | `borrowInfo.optimalUsageRate.value` | The "kink" point |
| Reserve factor | `borrowInfo.reserveFactor.value` | Decimal |
| Supply APY | `supplyInfo.apy.value` | Decimal |
| Borrow APY | `borrowInfo.apy.value` | Decimal |
| Max LTV | `supplyInfo.maxLTV.value` | Decimal |
| Liquidation threshold | `supplyInfo.liquidationThreshold.value` | Decimal |
| Can be collateral | `supplyInfo.canBeCollateral` | Boolean |
| Frozen | `isFrozen` | Boolean |
| Paused | `isPaused` | Boolean |

### Known Quirks
- Reserves with `borrowCap = 0` or `supplyCap = 0` mean "no cap set" (uncapped), NOT zero headroom
- Some cap usage % can be anomalous (e.g., >100%) for assets with very small/nominal caps — filter these
- `utilizationRate` is a decimal 0–1, not a percentage

---

## 1b. On-Chain Sanity Check (RPC Cross-Validation)

Verified 2026-04-08: GraphQL data matches on-chain exactly for caps, <0.01% for supply/borrow.

**How it works:**
1. Resolve Pool + DataProvider from PoolAddressesProvider per market
2. `Pool.getConfiguration(asset)` → decode supply/borrow caps from bitmap (bits 116-151 and 80-115)
3. `DataProvider.getReserveData(asset)` → total supply (field[2]), total borrow (field[3]+field[4])

**Function selectors:**
- `getPool()` = `0x026b1d5f`
- `getPoolDataProvider()` = `0xe860accb`
- `getConfiguration(address)` = `0xc44b11f7`
- `getReserveData(address)` = `0x35ea6a75`

**RPC endpoints:** See `config/contracts.py` for full mapping. BlockPI key is Ethereum-only. Infura covers 10 chains. Public RPCs for the rest.

**Note:** `getReserveCaps(address)` REVERTS on the current DataProvider (V3.1 change). Use `Pool.getConfiguration()` bitmap instead.

---

## 2. Aave V4/Hub GraphQL API (for future V4 monitoring)

- **Endpoint:** `https://api.aave.com/graphql`
- **Auth:** None required
- **Notes:** Uses hub/spoke terminology. Has additional fields like risk premiums. Useful when V4 launches.

---

## 3. On-Chain: UiPoolDataProvider (FALLBACK)

Each Aave V3 deployment has a `UiPoolDataProvider` contract returning all reserve data in one call.

- **Function:** `getReservesData(address poolAddressesProvider)`
- **Returns:** All reserve configs + market base currency data

### Key Addresses (Ethereum)
| Contract | Address |
|----------|---------|
| UiPoolDataProvider V3 | `0x56b7A1012765C285afAC8b8F25C69Bf10ccfE978` |
| PoolAddressesProvider V3 | `0x2f39d218133AFaB8F2B819B1066c7E434Ad94E9e` |

All addresses for all chains: **`@aave-dao/aave-address-book`** npm package or GitHub `bgd-labs/aave-address-book`
- Address book search UI: https://book.onaave.com/

---

## 4. DeFiLlama (SUPPLEMENTARY — for TVL only)

- **Endpoint:** `https://api.llama.fi/protocol/aave-v3`
- **Provides:** TVL data per chain
- **Does NOT provide:** Supply/borrow caps, utilization rates, reserve-level params
- **Already used by:** `LiquidityMonitor/data_sources/defillama.py`

---

## 5. BGD Labs / onaave.com Ecosystem

| Site | Purpose | Open Source? |
|------|---------|--------------|
| https://dash.onaave.com | Markets/reserves dashboard | **No** (Next.js SSR, no public API) |
| https://book.onaave.com | Address book search | Uses aave-address-book |
| https://vote.onaave.com | Governance voting | Yes: `bgd-labs/aave-governance-v3-interface` |
| https://adi.onaave.com | Cross-chain delivery monitoring | Yes: `bgd-labs/adi-dashboard` |
| https://permissions.onaave.com | Permissions visualization | Unknown |
| https://stake.onaave.com | Staking UI | Unknown |

### Key BGD Labs GitHub Repos
- **`bgd-labs/aave-address-book`** — Solidity + npm registry of all Aave contract addresses across chains
- **`bgd-labs/aave-helpers`** — Type-safe payloads, snapshot diffing, e2e testing
- **`bgd-labs/aave-cli`** — CLI for automating Aave interactions

### Key Aave Official Repos
- **`aave/aave-utilities`** — `@aave/contract-helpers` + `@aave/math-utils` (being deprecated)
- **`aave/aave-sdk`** — New `@aave/client` SDK wrapping the GraphQL API (early stage)

---

## 6. Chain IDs Reference

| Chain | Chain ID | In onaave.com? |
|-------|----------|----------------|
| Ethereum | 1 | Yes |
| Optimism | 10 | Yes |
| Polygon | 137 | Yes |
| Arbitrum | 42161 | Yes |
| Avalanche | 43114 | Yes |
| Base | 8453 | Yes |
| Gnosis | 100 | Yes |
| Metis | 1088 | Yes |
| BNB Chain | 56 | Yes |
| Scroll | 534352 | Yes |
| zkSync | 324 | Yes |
| Linea | 59144 | Yes |
| Sonic | 146 | Yes |
| Celo | 42220 | Yes |
| Ink | 1868 | Yes |
| MegaETH | 57073 | Yes* |
| Soneium | 9745 | Yes* |
| Mantle | 5000 | Yes |
| EtherFi | 4326 | Yes* |

*Newer chains — verify chain IDs in GraphQL response.
