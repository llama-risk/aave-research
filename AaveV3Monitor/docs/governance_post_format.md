# Aave Governance Cap Change Post — Format Reference

> Extracted 2026-04-08 from Chaos Labs posts. Use as template for our own parameter change reports.

## Sources
- [Direct to AIP example (2026-04-07)](https://governance.aave.com/t/direct-to-aip-change-of-supply-caps-and-adjustment-of-e-mode-assets-on-aave-v3-07-04-26/24396)
- [Risk Stewards example (2026-03-19)](https://governance.aave.com/t/chaos-labs-risk-stewards-change-of-supply-and-borrow-caps-on-aave-v3-18-03-26/24312)

## Title Conventions

Two execution paths:
- **Risk Stewards (no vote):** `"[Risk Org] Risk Stewards - Change of Supply and Borrow Caps on Aave V3 - DD.MM.YY"`
- **Direct to AIP (vote):** `"[Direct to AIP] Change of Supply Caps and [other changes] on Aave V3 - DD.MM.YY"`

## Document Structure

### 1. Summary
- Bullet list of proposed changes (one per asset/action)
- Reference to risk simulations
- Boilerplate: "All cap increases are backed by [Org]'s risk simulations, which consider user behavior, on-chain liquidity, and price impact..."

### 2. Per-Asset Sections (H2 per asset)

Each asset follows this template:

```markdown
## [ASSET_SYMBOL] ([Chain] [Market])

[Opening paragraph: current cap status, utilization %, supply growth over 7 days, demand drivers]

[IMAGE: supply utilization snapshot]

### Supply Distribution
[Concentration analysis: top supplier %, health factor distribution, strategies used (looping, leverage, etc.)]

[IMAGE: horizontal bar chart — wallets, supply amount, health factor, collateral composition]

### Borrow Distribution (only if borrow cap is being changed)
[Same structure as supply distribution for the borrow side]

[IMAGE: borrow distribution chart]

### Liquidity
[DEX depth assessment: specific DEX names, pool TVLs, slippage at test sell size]
"A sell of X tokens would incur Y% slippage"

[IMAGE: liquidity/price impact chart]

### Recommendation
[1-2 sentence conclusion: "Given adequate liquidity and healthy position distribution, we recommend increasing the supply cap from X to Y."]
```

### 3. Specification Table

Always this format:

| **Instance** | **Asset** | **Current Supply Cap** | **Recommended Supply Cap** | **Current Borrow Cap** | **Recommended Borrow Cap** |
|---|---|---|---|---|---|
| Ethereum Core | WETH | 500,000 | 600,000 | 450,000 | 540,000 |
| Mantle | sUSDe | 240,000,000 | 320,000,000 | - | - |

- Dash (`-`) for unchanged/not-applicable fields
- Numbers are comma-formatted (not abbreviated)

### 4. Standard Footer

```markdown
### Next Steps
We will move forward and implement these updates via the Risk Steward process.

### Disclosure
[Org] has not been compensated by any third party for publishing this recommendation.

### Copyright
Copyright and related rights waived via CC0.
```

## Data Points Per Asset

| Data Point | Source |
|-----------|--------|
| Current cap (supply/borrow) | GraphQL API `supplyCap` / `borrowCap` |
| Current supply/borrow total | GraphQL API `total.value` |
| Cap utilization % | Computed: total / cap * 100 |
| Supply growth (7-day) | Historical snapshots |
| Top supplier concentration | On-chain (UiPoolDataProvider or subgraph) |
| Health factor ranges | On-chain positions |
| Strategies (looping, leverage) | On-chain analysis |
| DEX liquidity depth | LiquidityMonitor or DEX aggregator quotes |
| Slippage at test sell | LiquidityMonitor or Paraswap/Odos quotes |

## Chart Types

1. **Supply utilization snapshot** — table/card showing current vs cap
2. **Supply distribution** — dark horizontal bar chart (wallets, amounts, HF, collateral)
3. **Borrow distribution** — same format
4. **Liquidity / price impact** — slippage curve chart
