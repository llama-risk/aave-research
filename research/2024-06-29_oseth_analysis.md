## Summary

We recently published a [comprehensive review of StakeWise Staked ETH (osETH)](https://www.llamarisk.com/research/collateral-risk-oseth) and present here a summary of our findings, with specific considerations regarding its current listing on Aave V3.

Our assessment of osETH is predominantly favorable. The primary area for improvement remains liquidity, with a significant portion of the supply currently held in EigenLayer. We also recommend that StakeWise implement more advanced access control capabilities and enhance protocol security measures for adverse conditions, particularly through refined pausing mechanisms.

A weakness noted in our comprehensive assessment regarding the absence of a Chainlink feed is not applicable in this context. Aave utilizes a combination of Chainlink's ETH/USD feed, StakeWise v3's exchange rate mechanism (updated via keepers), and the Correlated-assets price oracle (CAPO) adapter. This is generally sound, although it presents certain tradeoffs compared to using market price. We intend to explore these tradeoffs in future research.

In conclusion, we consider osETH a well-developed liquid staking token that has reached sufficient maturity for listing on Aave. The current parameters, including ETH-correlated e-mode and caps, appear appropriate given the present liquidity and market conditions.

## II - Market Risk Assessment

#### Liquidity

51.71% of osETH tokens are deposited in EigenLayer, making liquidity heavily dependent on EigenLayer's operational status and execution of its roadmap. This concentration could impact the osETH peg on secondary markets despite active liquidity incentives. StakeWise's efforts to distribute liquidity and maintain a stable profile enhance confidence in its market resilience.

![image|2000x1129](upload://othy5MqFBatMDj5SdP0AyDyxzAN.png)
Source: [Nansen, June 28th, 2024](https://app.nansen.ai/token-god-mode?tokenAddress=0xf1c9acdc66974dfb6decb12aa385b9cd01190e38&chain=ethereum&tab=token-distribution)

#### Volatility

Initial volatility stabilized with a positive depeg, indicating a high demand for osETH. On the 15th of May, we observed an outlier with a positive depeg of +2.8%, which quickly resolved in the following days. StakeWise uses a system that automatically chooses between protocol withdrawals and market swaps to maximize withdrawal output. The 10% overcollateralized ETH buffer protects against validator issues, maintaining the osETH peg without liquidations so far. However, the long-term efficacy of the redemption and liquidation mechanisms remains unproven under more adverse conditions.

![image|1000x600](upload://d7CCG2Jg3Tdn1u1wU0h8XAq6DmP.png)
Source: [OsTokenVaultController contract](https://etherscan.io/address/0x2A261e60FB14586B474C208b1B7AC6D0f5000306#code) and [CoinGecko](https://www.coingecko.com/en/coins/stakewise-staked-eth/historical_data) - from April 1st to June 28th, 2024

## III - Technological Risk

### 3.1 Smart Contract Risk Assessment

#### Audits

Three audits on the V3 codebase and previous audits have provided valuable insights. The public, well-documented, modular codebase includes a bug bounty on Immunefi. No security breaches or successful Immunefi claims have occurred.

- [Halborn](https://github.com/stakewise/v3-core/blob/main/audits/05-2023-Halborn.pdf) (2023-05): 5 findings including one high risk.
- [Halborn](https://github.com/stakewise/v3-core/blob/main/audits/08-2023-Halborn.pdf) (2023-08): 3 findings including one medium.
- [SigmaPrime](https://github.com/stakewise/v3-core/blob/main/audits/08-2023-Sigma-Prime.pdf) (2023-08): 21 findings including two critical risks, five high risks, and one medium risk.

### 3.2 Price Feed Considerations

Aave's integration of StakeWise v3's osETH utilizes StakeWise's osETH/ETH exchange rate, Chainlink's ETH/USD feed, and Aave's Correlated-assets price oracle (CAPO) adapter.

StakeWise v3's exchange rate mechanism provides the base osETH/ETH rate. Every 12 hours, off-chain oracles update this rate through the Keeper contract. The update process requires a 6/11 majority consensus among oracles and caps rate changes at approximately 22% APR. This mechanism captures accrued staking rewards and maintains the osETH/ETH relationship.

Aave combines this rate with Chainlink's ETH/USD feed to calculate the osETH/USD value. The CAPO adapter then applies range price protection to the resulting rate. This layered approach addresses the nature of osETH as an asset correlated with ETH but is subject to divergence due to staking rewards or market conditions. The system enables Aave to use osETH as collateral while addressing risks specific to liquid staking derivatives. It provides the price accuracy required for Aave's collateralization and liquidation processes.

A [osETH/USD RedStone pricefeed](https://app.redstone.finance/#/app/token/osETH) also exists, although we deem it suitable for isolated lending markets only as we consider it less secure than Chainlink.

### 3.3 Dependencies

StakeWise V3 relies on two off-chain services, the Operator and the Oracle. The decentralized, but not open-source, Oracle reduces centralization concerns. Smart contract checks and a role-based access control system prevent balance and reward manipulation. Operator off-chain services are operated by each vault admin, along with the infrastructure needed to operate their validators.

## IV - Counterparty Risk

### 4.1 Governance and Regulatory Risk Assessment

#### Regulatory risks

Incorporated in a UAE-free zone, StakeWise enjoys business flexibility but often has opaque ownership structures. The UAE's VARA still needs to regulate non-custodial staking, offering regulatory latitude. User interaction terms emphasize limiting liability and disclaiming warranties concerning osETH and protocol use.

### 4.2 Access Control

StakeWise V3 is decentralized and permissionless, with limited team control over deployed contracts. A [4/7 multisig](https://etherscan.io/address/0x144a98cb1CdBb23610501fE6108858D9B7D24934) with known public entities as signers control most contracts, except for the staking vaults which vault admins control. Known entities also operate Offchain Oracles, but the private Oracle code and unknown execution client diversity pose risks.

## IV - Aave V3 Specific Parameters

Here are the current parameters for osETH:

| Parameter                 | Recommendation |
|---------------------------|----------------|
| Isolation Mode            | No               |
| Emode                     | Enabled with ETH  |
| Borrowable                | Yes               |
| Borrowable in Isolation   | No               |
| Collateral Enabled        | Yes               |
| Stable Borrowing          | No               |
| Supply Cap                | 10,000              |
| Borrow Cap                | 1,000 (1/10 of supply cap) |
| Debt Ceiling              | NA               |
| LTV                       | 72.5%               |
| LT                        | 75%               |
| Liquidation Bonus         | 7.5%               |
| Liquidation Protocol Fee  | 10%               |
| Reserve Factor            | 15%               |
| Base Variable Borrow Rate | 0%               |
| Variable Slope 1          | 7%               |
| Variable Slope 2          | 300%               |
| Uoptimal                  | 45%               |

The current parameters appear to remain optimal for an LSD such as osETH, based on the available data and established methodologies.

Analysis of osETH liquidity reveals that the primary pool is BalancerV2 osETH/ETH, containing 10,500 ETH, constituting 55% of the pool's total assets. Alternative pools offer insignificant liquidity. The current supply cap of 10,000 aligns closely with the recommendation derived from the recommended methodology, which proposes setting the supply cap at twice the liquidity within the liquidation bonus, expressed as a percentage of price impact.

The E-mode parameters for osETH against ETH are consistent with those of comparable Liquid Staking Derivatives (LSDs) such as stETH and rETH. Considering the observed stability of the osETH/ETH peg, these parameters are deemed appropriate. The absence of a debt ceiling is justified by the StakeWise protocol's maturity and degree of decentralization.

#### Note: This assessment follows the LLR-Aave Framework, a comprehensive methodology for asset onboarding and parameterization in Aave V3. This framework is continuously updated and [available here](https://github.com/llama-risk/aave-research/blob/main/frameworks/aave_v3_framework.md).
