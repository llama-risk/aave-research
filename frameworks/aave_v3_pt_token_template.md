# PT Tokens Evaluation Template

:::info
This LLR Framework is meant to be applied after the initial underlying asset's analysis is completed.
:::

**Forum Discussion:** [Link]()

## Summary

:::info
Support/rejection, the key findings, rationale for setting the initial parameters. Reference of analysis on the base (underlying) asset.
:::

**Assessment of PT base asset:** [Link]()
**Considered PT asset maturities:** [PT-X-29-May-2025]()

## Asset State

### Underlying Yield Source

:::info
The source of the underlying yield, yield mechanism, yield sustainability.
:::

### Underlying Utility

:::info
The cause of interest towards the underlying asset (speculative nature/market backed reasons).
:::

### Underlying Stability

:::info
Stability risk of the underlying (de-pegs, yield fluctuations).
:::

### Total Supply

:::info
Total current supply of a PT, SY asset, supply over time.
:::

### Holders

:::info
The distribution and concentration of PT asset holders.
:::

### Liquidity

:::info
Current liquidity in the Pendle pools, evolution over time. The concentration and distribution of LPs, order book. Parameters of the main pool (`maxDiscount`, `FeeTier` etc.)
:::

| Parameter           | Value                |
|---------------------|----------------------|
| Liquidity Yield Range |       |
| Fee Tier            |                |
| Input Tokens        |         |
| Output Tokens       |         |
| Reward Tokens       |               |


## Market State

### Price and Yield

:::info
PT price and yield evolution. LP yield evolution.
:::

### Maturities

:::info
Other maturities that are available in addition to the largest pool.
:::

### Integrated Venues

:::info
Venues that integrated PT tokens: lending platforms, DEXs (if any).
:::

## Recommendations

### Aave Market Parameters

:::info
Standard market parameters, E-Mode parameters (if applicable).
:::

**Standard**
| Parameter                 | Recommendation |
|---------------------------|----------------|
| Isolation Mode            |                |
| Emode                     |                |
| Borrowable                |                |
| Borrowable in Isolation   |                |
| Collateral Enabled        |                |
| Supply Cap                |                |
| Borrow Cap                |                |
| Debt Ceiling              |                |
| LTV                       |                |
| LT                        |                |
| Liquidation Bonus         |                |
| Liquidation Protocol Fee  |                |
| Reserve Factor            |                |
| Base Variable Borrow Rate |                |
| Variable Slope 1          |                |
| Variable Slope 2          |                |
| Uoptimal                  |                |

**E-Mode**
| Parameter             | Asset Name 1 | Asset Name 2 | Asset Name 3 |
|-----------------------|--------------|--------------|--------------|
| Asset                 | [Value]      | [Value]      | [Value]      |
| Collateral            | [Yes/No]     | [Yes/No]     | [Yes/No]     |
| Borrowable            | [Yes/No]     | [Yes/No]     | [Yes/No]     |
| Max LTV               | [Value/%]    | [Value/%]    | [Value/%]    |
| Liquidation Threshold | [Value/%]    | [Value/%]    | [Value/%]    |
| Liquidation Bonus     | [Value/%]    | [Value/%]    | [Value/%]    |


### Price Feed

:::info
Underlying pricing mechanism, Dynamic linear discount rate oracle parameters (`discountRate`, `maxDiscountRate`), CAPO (if applicable).
:::

### Disclaimer

This review was independently prepared by LlamaRisk, a DeFi risk service provider funded in part by the Aave DAO. LlamaRisk serves as a member of Ethena’s Risk Committee and an independent attester of Ethena’s PoR solution. LlamaRisk did not receive compensation from the protocol(s) or their affiliated entities for this work. The information should not be construed as legal, financial, tax, or professional advice.
