![17-min](https://hackmd.io/_uploads/HkRzdZ0BR.png)

# Aave explainer series - the GHO stablecoin

*This article was prepared for the Aave DAO as part of an explainer series published by LlamaRisk, which has been [appointed as an Aave risk service provider](https://app.aave.com/governance/v3/proposal/?proposalId=90). It offers an in-depth view of the GHO stablecoin, including its collateral, liquidity mechanisms, and integrations with other DeFi protocols. This series aims to provide the general public with an overview of Aave's current state, ultimately leading to the creation of a risk framework for asset onboarding and parameterization.*

## Useful links

Website: [app.aave.com](https://app.aave.com/reserve-overview/?underlyingAsset=0x40d16fc0246ad3160ccc09b8d0d3a2cd28ae6c2f&marketName=proto_mainnet_v3)
Documentation: [GHO whitepaper](https://github.com/aave/gho-core/blob/main/techpaper/GHO_Technical_Paper.pdf) | [GHO docs](https://docs.gho.xyz/)
Contracts: [GHO token](https://etherscan.io/token/0x40D16FC0246aD3160Ccc09B8D0D3A2cD28aE6C2f) | [stkGHO token](https://etherscan.io/token/0x1a88df1cfe15af22b3c4c783d4e6f7f9e0c1885d)
Dashboards: [TokenLogic metrics](https://aave.tokenlogic.com.au/gho) | [Chaos Labs dashboard](https://community.chaoslabs.xyz/aave/risk/GHO/overview)

## Summary

* GHO is a decentralized, over-collateralized stablecoin native to the Aave V3 Protocol. It is minted by users on demand by supplying assets at a minimum collateral ratio. The top collateral types currently are wstETH, sDAI, WETH, and WBTC.
*	The total GHO supply is limited by a borrow cap set by Aave Governance, 85m as of June 11th, 2024. Governance also dictates its interest rate and sets incentive programs.
*	GHO can always be redeemed by borrowers through the Aave Protocol at a fixed value of $1, effectively paying back their debt and freeing up the collateral locked when they minted GHO. This fixed rate enables arbitrage opportunities with secondary markets, helping to maintain GHO's peg to the US dollar. 
*	GHO holders can earn yield through staking into the Safety Staking Module, the Merit incentive program, and other DeFi protocols such as Gearbox, Aura, and fx Protocol. Over 65% of GHO supply is staked in the Safety Staking Module, an insurance fund protecting against shortfall events.
*	Unlike other borrowable assets on Aave, interest payments from GHO minters go directly to the Aave DAO treasury.

## Introduction

GHO is a decentralized stablecoin introduced by the Aave protocol in July 2023. It aims to operate as a fully collateralized and transparent stablecoin, with parameters managed by the Aave DAO through governance. GHO is minted by users on demand and is subject to mint cap limitations. The launch of GHO brings forth the concept of "Facilitators", smart contracts approved by Aave governance to mint and burn GHO tokens within specified limits. The initial facilitators for GHO were the Aave Protocol V3 Pool, allowing GHO minting through Aave's established borrow functionality, and the Flashmint facilitator, enabling GHO to be minted and burned within a single transaction to support various use cases within the DeFi ecosystem. As GHO is integrated into Aave's V3 liquidity pool, it benefits from the protocol's native features, such as collateralization mechanism and risk management parameters.

## GHO Mechanics

### Minting

Minting GHO follows a process similar to borrowing assets on Aave. First, a user must supply collateral at a minimum ratio, which varies depending on the asset. Unlike other assets on Aave, GHO is minted on demand; therefore, the user does not have to rely on GHO to be supplied to the protocol. Instead, new GHO tokens are created when a user mints against their collateral. The total amount of GHO that can be minted is limited by a borrow cap.

![image](https://hackmd.io/_uploads/S1PpOarHA.png)
*Source: [Aave](https://app.aave.com/reserve-overview/?underlyingAsset=0x40d16fc0246ad3160ccc09b8d0d3a2cd28ae6c2f&marketName=proto_mainnet_v3), June 11th, 2024*

Aave Governance entities regularly adjust the borrow cap according to market conditions and demand. Anyone who has been granted `RISK_ADMIN` or `POOL_ADMIN` role via the [ACL Manager V3](https://etherscan.io/address/0xc2aaCf6553D20d1e9d78E365AAba8032af9c85b0#readContract) can call `setBorrowCap()` on the [Aave Pool Configurator V3](https://etherscan.io/address/0x64b761d848206f447fe2dd461b0c635ec39ebb27) contract to change the borrow cap.

Entities that can change the borrow cap:
- GHO Steward V2 has `POOL_ADMIN` role ([Source](https://etherscan.io/tx/0xcd6558748c492c600c27fa7c7f3bf490fe12a621858e62cf97aac8032cb86fd3#eventlog))
- FreezingSteward has `RISK_ADMIN` role ([Source](https://etherscan.io/tx/0x497a000a7fdf8eb9116d50537d29c6f04e7988a93c1518ddacd73d1915439149#eventlog))
- RiskStewardV3 has `RISK_ADMIN` role ([Source](https://etherscan.io/tx/0x5e9a315d5521902fb5c2a42bd9f955bc0e40cc095753600297d1577f2659c019#eventlog))

![image](https://hackmd.io/_uploads/rJxdimzBA.png)
*An example of borrow cap change for GHO. Source: [Etherscan](https://etherscan.io/tx/0x5c12e19bb5039bdf35326f13d7506ed147e8817639cd4036eba42b1d6e5db08e#eventlog), June 11th, 2024*

### Borrow rates

GHO borrow rates function differently than other assets on Aave due to the absence of suppliers. The GHO borrow interest rate is set directly by the Aave DAO and can be periodically adjusted to maintain stability and balance supply and demand. Borrowers who stake AAVE in the [Safety Staking Module](https://hackmd.io/75TCxqvbQOCYFgyFtgorhg#Safety-Staking-Module) receive discounts on their GHO borrow rates. By staking in the Safety Module, users take on the risk of having their stake slashed to cover protocol deficits in case of a shortfall event. Aave Governance controls the discount rate configuration, incentivizing users to participate in staking, and helps secure the protocol.

![image](https://hackmd.io/_uploads/rkx8wisaNA.png)
*GHO Reserve status & configuration page. Source: [Aave](https://app.aave.com/reserve-overview/?underlyingAsset=0x40d16fc0246ad3160ccc09b8d0d3a2cd28ae6c2f&marketName=proto_mainnet_v3), June 11th, 2024*

### Burning

When a user repays a GHO borrow position or is liquidated, the GHO tokens are returned to the Aave pool and burned, effectively removing them from circulation. This process frees up the user's collateral, which can then be used to open a new borrow position or be withdrawn from the protocol.

![image](https://hackmd.io/_uploads/HyngkEGB0.png)
*An example of GHO debt repayment and subsequent burn of the token. Source: [Etherscan](https://etherscan.io/tx/0xe95b49651193f77647f0fbb464806e66c63bec0f34538217697f7ff53c7bbac6), June 8th, 2024*

### FlashMinter

Certain assets supplied to the Aave Lending Pool can be used for flash loans, allowing users to borrow assets from the pool and repay them within a single atomic transaction. However, since GHO is not supplied as an asset, performing a flash loan with GHO is not possible similarly.

To address this limitation, Aave has introduced the concept of `FlashMinting`, which provides functionality similar to flash loans and adheres to the current flash loan standard ([ERC-3156](https://eips.ethereum.org/EIPS/eip-3156)) used in the Aave protocol. With `FlashMinting`, users can access the liquidity of the FlashMinter facilitator for a single transaction, provided that the borrowed amount, along with a fee, is returned within the same transaction. As of June 2024, the `FlashMinting` fee is 0 ([Source](https://etherscan.io/address/0xb639D208Bcf0589D54FaC24E655C79EC529762B8#readContract)).

As a GHO facilitator, the `FlashMinter` contract also has a mint cap (bucket capacity). As of June 2024, it is equal to 2,000,000 GHO ([Source](https://etherscan.io/address/0x40D16FC0246aD3160Ccc09B8D0D3A2cD28aE6C2f#readContract)). The bucket capacity can only be modified by `BUCKET_MANAGER_ROLE`. 

#### Use cases

`FlashMinting` mechanism offers several useful applications:

1. **Debt swap:** One of the biggest entities using `FlashMinting` is the [ParaSwapDebtSwap](https://github.com/aave/aave-debt-swap) contract that allows a user to swap one debt position to another debt position - either partially or completely. 
2. **Arbitrage Opportunities:** Flashminting can be used for arbitrage within the Aave protocol and other DeFi platforms. This process allows the user to profit from the price difference between different liquidity pools without needing initial capital, leveraging the flashmint feature to perform the trade. The flow is as follows:
    1. Flashmint GHO.
    2. Sell GHO in a higher-priced liquidity pool.
    3. Buy back GHO from a lower-priced liquidity pool.
    4. Repay the flash-minted GHO, completing the arbitrage in one transaction block.
3. **Liquidating Unhealthy Positions:** Flashminting can also be utilized to liquidate unhealthy GHO borrow positions within the Aave protocol. If a borrower's collateral falls below the required threshold, making their position unhealthy, a liquidator can flashmint GHO to repay the borrower's debt and receive a liquidation bonus. This way, the liquidator does not need to use any of his funds to liquidate GHO debt. The flow is as follows:
    1. The liquidator flash mints GHO, using it to cover the debt of the unhealthy borrow position immediately.
    2. This repayment of the borrower's debt returns the unhealthy position to a healthy state, effectively covering the shortfall and liquidating part of the collateral.
    3. In return for repaying the debt, the liquidator receives the liquidated part of the collateral and a liquidation bonus.
    4. The liquidator then uses the collateral to repay the flash-minted GHO, completing the transaction.

These capabilities also contribute to market efficiency and stabilizing GHO's price.

## Protocol Revenue Model and Fees

Aave's revenue model for GHO differs from other borrowed assets on the platform. When users borrow assets on Aave, a portion of the interest paid is allocated to the DAO treasury as specified by the Reserve Factor parameter, while the remaining portion goes to the liquidity suppliers. However, for GHO, all interest payments made by minters are directly sent to the Aave DAO treasury.

GHO has generated 2.3M USD as of June 11th, 2024. This includes 1.5M USD of unrealized revenue, as the accrued interest by minters is paid to the Aave DAO treasury when GHO is burned.

![image](https://hackmd.io/_uploads/rkhAt6HHC.png)
*GHO Revenue dashboard. Source: [TokenLogic](https://aave.tokenlogic.com.au/gho-revenue), June 11th, 2024*

## Stability mechanisms

GHO employs various mechanisms to maintain its peg to the US Dollar. These include inherent features like the fixed oracle price, interest rate adjustments, and additional measures overseen by Aave Governance.

### Fixed Oracle price

The Aave protocol values GHO at a fixed rate of $1, regardless of market fluctuations. This fixed oracle price creates arbitrage opportunities that help stabilize GHO's market price:
* **When GHO trades above $1**: Users can mint 1 GHO (worth > $1) at $1 worth of collateral and sell it for a profit, waiting for the market price to decrease. This increases the GHO supply and reduces its price.
* **When GHO trades below $1**: Existing GHO borrower can buy GHO on the market for less than $1 and use it to repay $1 worth of debt. This decreases the GHO supply and increases its price.

Many decentralized stablecoin protocols use this mechanism to help stabilize a soft peg. However, users may need more incentive to arbitrage the peg with this mechanism alone, and the soft peg can deviate from $1 for extended periods without additional stabilization measures.

### GHO interest rate

Aave Governance can impact GHO's market price by adjusting its interest rate as a stabilization mechanism. If the market price of GHO rises above $1, Aave Governance can decrease the interest rate. This lower interest rate may incentivize more users to mint GHO, increasing its supply and driving the price back down to the peg. Conversely, if the market price of GHO falls below $1, Aave Governance can increase the interest rate. A higher interest rate encourages users to repay their GHO positions, effectively burning GHO and reducing the circulating supply. This reduction in supply can bring the price back up to the peg.

However, it is important to note that user borrowing behavior is influenced by various factors, including interest rates in the broader DeFi ecosystem, traditional finance rates, and the perceived risk associated with holding GHO. As a result, regular adjustments to the interest rate may be necessary to elicit the desired market behaviors and maintain GHO's stability. Aave Governance must carefully monitor market conditions and user behavior to ensure timely and appropriate interest rate adjustments to support GHO's peg to the US Dollar.

![image](https://hackmd.io/_uploads/BJc6P8RNR.png)
*GHO Borrow Rate. Source: [GHO Analytics](https://aave.tokenlogic.com.au/borrow-rate), June 11th, 2024*

Analyzing the historical performance of the interest rate strategy and the correlation between interest rates and the price of GHO reveals a positive correlation. Higher interest rates tend to push the price of GHO upward, thereby contributing to price stability within specific ranges. Despite occasional short-term peg stresses caused by global market volatility, such as the fluctuations observed on April 15th, 2024, the price of GHO has demonstrated resilience. It quickly rebounded and returned to the target range, indicating the sustained effectiveness of the interest rate strategy in maintaining the stablecoin's peg.

![image](https://hackmd.io/_uploads/H1cLjENS0.png)
*GHO Price vs. Borrow Rate Range- March 8th, 2024. Source: [GHO Analytics](https://aave.tokenlogic.xyz/borrow-rate), June 11th, 2024*

![image](https://hackmd.io/_uploads/By_eoNErA.png)
*GHO Price vs. Borrow Rate Range - April 8th, 2024. Source: [GHO Analytics](https://aave.tokenlogic.xyz/borrow-rate), June 11th, 2024*

GHO's borrow rate is continuously adjusted based on the market rates and overall borrow interest. To incentivize borrowing and ensure that GHO supply keeps growing, the interest rates are set to be lower than those of its counterparty stablecoins. Moreover, additional incentives that lower the borrow rate exist, namely: [Merit program](https://hackmd.io/75TCxqvbQOCYFgyFtgorhg?both#Merit-incentive-program) and borrow rate discounts for stkAave holders.

![image](https://hackmd.io/_uploads/BJi2qTBSR.png)
GHO borrow rate (orange line) vs. other stablecoins. Source: [GHO Analytics](https://aave.tokenlogic.com.au/gho), June 11th, 2024

### GHO Stability Module

Drawing inspiration from MakerDAO's Peg Stability Module (PSM), the GHO Stability Module (GSM) is a smart contract designed to facilitate the conversion between GHO and governance-approved stablecoins at a predetermined ratio. The capital for the GSM is provided by users who mint GHO by depositing approved stablecoins, such as USDT or USDC, into the GSM smart contract. When users mint GHO through the GSM, they effectively exchange their stablecoins for GHO at a predetermined ratio, as defined by the GSM's "Price Strategy". The stablecoins deposited by users accumulate in the GSM, forming a pool of capital that essentially backs the minted GHO 1:1 by the counterparty stablecoins. This accumulated pool of stablecoins serves as a reserve to maintain GHO's peg and stabilize the system. Since its introduction in late January 2024, the GSM has seen only occasional usage, with some transactions attributed to MEV activity.

![image](https://hackmd.io/_uploads/SyXqipSBA.png)
*Source: [GSM user interface](https://app.gsm.tokenlogic.xyz/), June 11th, 2024*

When GHO trades above $1, anyone (not only existing GHO borrowers) can instantly arbitrage the peg by converting USDT to GHO through the GSM and selling GHO for a profit on the exchange. This increases the GHO supply and brings its price down. Conversely, when GHO trades below $1, users can buy GHO on the market and redeem it for USDT through the GSM, reducing the GHO supply and increasing its price. Additionally, if there is liquidity in the GSM and GHO trades below $1, it can be arbitraged for the amount available in the GSM. However, the GSM offers no protection against under pegging if it is empty.

While the GSM improves stability, it also changes the risk profile of GHO. Since GHO minted through the GSM is backed by the stablecoins in the GSM, if a counterparty stablecoin depegs, it can cause GHO to depeg as well. This would effectively cause bad debt proportional to the amount of the stablecoin depeg and the amount of GHO minted from the GSM. At this time, the GSM represents a marginal proportion of the overall GHO supply and, therefore, does not represent a significant risk to the stability of GHO.

#### GSM mechanism

The GSM incorporates several key components:

1.	**Price Strategies**: The GSM supports fixed or dynamic pricing strategies to adjust the ratio between GHO and the exogenous asset. Initially, a Fixed Pricing Strategy is used, with the option to adopt dynamic strategies via future AIPs.
2.	**Debt Ceiling**: The Debt Ceiling feature allows the Aave DAO to limit exposure to specific assets backing GHO. The minting transaction will fail if the amount of exogenous assets backing minted GHO exceeds the Debt Ceiling.
3.	**Capital Allocator**: The Capital Allocator enables a portion of exogenous assets in the GSM to be used by a "fund manager" for allocation and yield generation, with the available funds determined by a configurable threshold set through governance.
4.	**Last Resort Liquidations**: In case of significantly increased risk in an exogenous asset, the Last Resort Liquidations mechanism allows the [Aave DAO](https://etherscan.io/address/0x5300A1a15135EA4dc7aD5a167152C01EFc9b192A) to control the asset and pause the GSM.
5.	**Price Bounds and Swap Freezes**: Price Bounds and Swap Freezes, managed by an external contract, can pause trading when the price of the exogenous asset deviates from the 1:1 ratio with GHO.

Currently, the GSM is implementing a Fixed Pricing Strategy, allowing USDT and USDC to be used to mint GHO. The market parameters of the GSM can be modified by Aave Governance as needed.

**Contract addresses:**
- USDT: [0x686F8D21520f4ecEc7ba577be08354F4d1EB8262](https://etherscan.io/address/0x686F8D21520f4ecEc7ba577be08354F4d1EB8262)
- USDC: [0x0d8effc11df3f229aa1ea0509bc9dfa632a13578](https://etherscan.io/address/0x0d8effc11df3f229aa1ea0509bc9dfa632a13578)
- Fixed Price Strategy (USDT): [0x4c707764cbFB4FFa078e169e6b8A6AdbE7526a2c](https://etherscan.io/address/0x4c707764cbFB4FFa078e169e6b8A6AdbE7526a2c)
- Fixed Price Strategy (USDC): [0x430BEdcA5DfA6f94d1205Cb33AB4f008D0d9942a](https://etherscan.io/address/0x430BEdcA5DfA6f94d1205Cb33AB4f008D0d9942a)
- Fee Strategy: [0x83896a35db4519BD8CcBAF5cF86CCA61b5cfb938](https://etherscan.io/address/0x83896a35db4519BD8CcBAF5cF86CCA61b5cfb938)

**GSM as of June 11th, 2024**
| Parameter | USDC GSM | USDT GSM  |
|-|-|-|
| Contract                    | Transparent Upgradeable Proxy ([Source](https://etherscan.io/address/0x0d8effc11df3f229aa1ea0509bc9dfa632a13578))                                                       | Transparent Upgradeable Proxy ([Source](https://etherscan.io/address/0x686F8D21520f4ecEc7ba577be08354F4d1EB8262))                                                        |
| Exposure Cap                | 4,000,000 USDC ([Source](https://etherscan.io/address/0x0d8effc11df3f229aa1ea0509bc9dfa632a13578#readProxyContract#F19))                                                 | 4,000,000 USDT ([Source](https://etherscan.io/address/0x686F8D21520f4ecEc7ba577be08354F4d1EB8262#readProxyContract#F19))                                                  |
| Exposure on 11th June, 2024 | 2,605,289 USDC ([Source](https://etherscan.io/address/0x0d8effc11df3f229aa1ea0509bc9dfa632a13578#readProxyContract#F17))                                                 | 1,835,753 USDT ([Source](https://etherscan.io/address/0x686F8D21520f4ecEc7ba577be08354F4d1EB8262#readProxyContract#F17))                                                  |
| Swap Fee (USDC/USDT to GHO) | 0% ([Source](https://governance.aave.com/t/arfc-gho-stewards-adjustments-gho-borrow-cap/17289/13))                                                                        | 0% ([Source](https://governance.aave.com/t/arfc-gho-stewards-adjustments-gho-borrow-cap/17289/13))                                                                        |
| Swap Fee (GHO to USDC/USDT) | 0.2% ([Source](https://governance.aave.com/t/arfc-gho-stewards-adjustments-gho-borrow-cap/17289/13))                                                                      | 0.2% ([Source](https://governance.aave.com/t/arfc-gho-stewards-adjustments-gho-borrow-cap/17289/13))                                                                      |
| Price Strategy              | Fixed 1:1 ratio ([Source](https://etherscan.io/address/0x4c707764cbFB4FFa078e169e6b8A6AdbE7526a2c#readContract#F2))                                                       | Fixed 1:1 ratio ([Source](https://etherscan.io/address/0x4c707764cbFB4FFa078e169e6b8A6AdbE7526a2c#readContract#F2))                                                       |
| Swap Freeze Price Range     | [0.99 - 1.01] ([Source](https://vote.onaave.com/proposal/?proposalId=8&ipfsHash=0xb87ef765d6082f5ac26466bc730b069c42d4ea9fe130250a26be627ac259d259))                   | [0.99 - 1.01] ([Source](https://vote.onaave.com/proposal/?proposalId=8&ipfsHash=0xb87ef765d6082f5ac26466bc730b069c42d4ea9fe130250a26be627ac259d259))                   |
| Swap Unfreeze Price Range   | [0.995 - 1.005] ([Source](https://vote.onaave.com/proposal/?proposalId=8&ipfsHash=0xb87ef765d6082f5ac26466bc730b069c42d4ea9fe130250a26be627ac259d259))                 | [0.995 - 1.005] ([Source](https://vote.onaave.com/proposal/?proposalId=8&ipfsHash=0xb87ef765d6082f5ac26466bc730b069c42d4ea9fe130250a26be627ac259d259))                 |
| Bucket Capacity             | 4,000,000 GHO ([Source](https://etherscan.io/tx/0xb1e6f2c265b07e9f070b6daa719c928cc7a2ff9e0443972ebc9d9f01719d5be8#eventlog))                                           | 4,000,000 GHO ([Source](https://etherscan.io/tx/0xb1e6f2c265b07e9f070b6daa719c928cc7a2ff9e0443972ebc9d9f01719d5be8#eventlog))                                           |
| Treasury                    | Aave Collector V2 ([Source](https://etherscan.io/address/0x0b0320cc11be5101d143adacfb9a5da34b122921#readContract#F23))                                                    | Aave Collector V2 ([Source](https://etherscan.io/address/0x0b0320cc11be5101d143adacfb9a5da34b122921#readContract#F23))                                                    |

**GSM Roles:**
- `CONFIGURATOR_ROLE`: GHO Steward V2 ( [Source](https://etherscan.io/tx/0xcd6558748c492c600c27fa7c7f3bf490fe12a621858e62cf97aac8032cb86fd3#eventlog))
- `LIQUIDATOR_ROLE`: Aave DAO ([Source](https://vote.onaave.com/proposal/?proposalId=8&ipfsHash=0xb87ef765d6082f5ac26466bc730b069c42d4ea9fe130250a26be627ac259d259))
- `SWAP_FREEZER_ROLE`: Aave DAO ([Source](https://vote.onaave.com/proposal/?proposalId=8&ipfsHash=0xb87ef765d6082f5ac26466bc730b069c42d4ea9fe130250a26be627ac259d259)), OracleSwapFreezer ([Source](https://etherscan.io/tx/0x51e776e9f4504d9102255eb8bf09e5ff42c5d10b13ddf09fa2e5c731deeef85c#eventlog))
- `TOKEN_RESCUER_ROLE`: None

**Access control:**
- `rescueTokens()` can be executed by `TOKEN_RESCUER_ROLE`
- `setSwapFreeze()` can be executed by `SWAP_FREEZER_ROLE` 
- `seize()` and `burnAfterSeize()` can be executed by `LIQUIDATOR_ROLE`
- `updateFeeStrategy()`, `updateExposureCap()`, and `updateGhoTreasury()` can be executed by `CONFIGURATOR_ROLE`
- `PRICE_STRATEGY` is immutable and set on GSM initialization

The USDT and USDC currently held in the GSM are not used to generate yield. Given the low usage of the GSM, it may be advantageous to consider using these funds to accrue yield, which could then be distributed to the Aave Treasury.

### Safety Staking Module

The Safety Staking Module (SM) plays a crucial role in maintaining GHO's stability by providing a safety net for the Aave protocol in case of shortfall events, such as ineffective liquidations that result in bad debt. If such events occur, the protocol can use the funds from the SM to restore the collateralization of GHO, ensuring that the stablecoin remains fully backed.

The SM has never been invoked, but [Aave categorizes the following risk conditions as shortfall events](https://docs.aave.com/aavenomics/safety-module) that would trigger the use of funds in the SM to cover the losses:

- **Smart contract risk**: Risk of a bug, design flaw, or potential attack surfaces on the smart contract layer.
- **Liquidation risk**: Risk of failure of an asset being used as collateral on Aave; risk of liquidators not capturing liquidation opportunities promptly; or low market liquidity of the principal asset to be repaid.
- **Oracle failure risk**: Risk of the Oracle system not properly updating the prices in case of extreme market downturn and network congestion; risk of the Oracle system not properly submitting prices, causing improper liquidations.

The primary mechanism for securing the Aave Protocol involves incentivizing AAVE, ABPT, and, more recently, GHO holders to lock their tokens into the SM of a corresponding token, a smart contract vault. For example, when GHO tokens are locked in the SM, stkGHO is minted to represent the locked GHO tokens. These locked GHO tokens are a mitigation tool in case of a shortfall event within the GHO liquidity markets on Aave.

In the event of a shortfall, each staked token can be slashed to cover the deficit, providing additional protection for the protocol. The maximum slashing threshold differs for each token: 30% for AAVE, 30% for ABPT, and 99% for GHO.

As an incentive for staking their tokens, SM stakers receive Safety Incentives. Due to the higher slashing threshold for GHO, stakers are offered a higher APY as compensation for the increased risk.

![image](https://hackmd.io/_uploads/r1QlwABBR.png)
*Source: [Aave](https://app.aave.com/staking/), June 11th, 2024*

To ensure the system's stability, a cooldown period (currently set to 20 days) is applied for users who wish to exit the SM. This cooldown prevents stakers from immediately unstaking their tokens in the event of a legitimate shortfall, during which their tokens may be slashed to cover losses.

![image](https://hackmd.io/_uploads/rkTtWzGER.png)
*Cooldown setting. Source: stkGHO contract on [Etherscan](https://etherscan.io/address/0x1a88df1cfe15af22b3c4c783d4e6f7f9e0c1885d#readProxyContract), June 11th, 2024*

**stkGHO roles and access control (all control via [Aave DAO](https://etherscan.io/address/0x1a88df1cfe15af22b3c4c783d4e6f7f9e0c1885d#readProxyContract)):**
- `CLAIM_HELPER_ROLE` can redeem rewards and unstake stkGHO on behalf of another address.
- `COOLDOWN_ADMIN_ROLE` can modify the cooldown period.
- `SLASH_ADMIN_ROLE` can slash tokens and modify the max slash percentage.
- `DISTRIBUTION_MANAGER` can modify reward distribution.

**stkGHO parameters:**
- Reward Token: AAVE ([Source](https://etherscan.io/address/0x1a88df1cfe15af22b3c4c783d4e6f7f9e0c1885d#readProxyContract#F10))
- Cooldown: 20 days ([Source](https://etherscan.io/address/0x1a88df1cfe15af22b3c4c783d4e6f7f9e0c1885d#readProxyContract#F21))
- Time window to unstake after cooldown: 2 days ([Source](https://etherscan.io/address/0x1a88df1cfe15af22b3c4c783d4e6f7f9e0c1885d#readProxyContract#F13))
- Total supply, 11th of June, 2024: 55,580,000 GHO ([Source](https://etherscan.io/address/0x1a88df1cfe15af22b3c4c783d4e6f7f9e0c1885d#readProxyContract#F35))
- No supply cap
- Reward token type is immutable

## Collateralization

Users can supply all assets accepted in the Aave Lending Pool as collateral to mint GHO. Therefore, the collateral backing GHO is a function of the assets that minters choose to deposit. The governance can only control general Aave Pool supply caps but cannot limit minting GHO from individual collateral types.

As of June 11th, 2024, GHO had a [collateral ratio](https://aave.tokenlogic.com.au/collateral) of around 260%, with a significant portion of the collateral being ETH-correlated assets. This high collateral ratio provides a substantial safety buffer for GHO, reducing the risk of the collateral value falling below the value of the minted tokens.

The below dashboard provides an overview of GHO a risk
![image](https://hackmd.io/_uploads/ByISF0SHC.png)
*GHO at Risk. Source: [ChaosLabs](https://community.chaoslabs.xyz/aave/risk/GHO/overview), June 11th, 2024*

One collateral stands out, sDAI, as the majority of it has been supplied by [one large GHO minter](https://community.chaoslabs.xyz/aave/risk/wallets/0xfcc5acd50ae590889d2a53343d35b5fb80d403c2). A liquidation of 9% of total GHO debt would happen if sDAI depegs by 10%.

## Governance

The governance of GHO involves various entities and committees making up the Aave DAO that work together to ensure the stability and growth of the stablecoin. These groups are crucial in managing GHO's market parameters and liquidity.

### Liquidity Committee

The GHO Liquidity Committee (GLC) [was created in October 2023](https://governance-v2.aave.com/governance/proposal/343/) to focus solely on the liquidity of the GHO stablecoin. After a successful initial 3-month period, it was integrated into the Aave Liquidity Committee (ALC).

The ALC's main responsibilities regarding GHO include the following:
* Providing analytics and modeling of the liquidity strategy
* Liaising with teams that support the protocols hosting GHO liquidity
* Leading and coordinating the committee's weekly activities
* Providing critical feedback and helping refine the strategy
* Verifying and signing transactions
    
The ALC's performance measures and liquidity targets for GHO can be found on the [GHO Analytics platform](https://aave.tokenlogic.xyz/liquidity-committee) provided by TokenLogic.

As of June 2024, the members of the committee are:

- [Figue](https://x.com/Figue_me) (Paladin)
- [Marc Zeller](https://x.com/lemiscate) (ACI)
- [Emilio](https://avara.xyz/) (Avara)
- [sisyphos](https://www.karpatkey.com/projects/aave) (karpatkey)
- [Matthew Graham](https://aave.tokenlogic.xyz/) (Tokenlogic)

ALC multi-sig address: [`0x205e795336610f5131be52f09218af19f0f3ec60`](https://debank.com/profile/0x205e795336610f5131be52f09218af19f0f3ec60/history)

### GHO Stewards

The GHO Stewards is an additional entity [created in April 2024](https://vote.onaave.com/proposal/?proposalId=61&ipfsHash=0x111fca5019e0bc411dc4bfa36167ad7d88c57c9ddbffb202fb1568e16dd06570) to manage GHO market parameters more flexibly, enabling GHO to scale by prevailing market conditions. The GHO Stewards determine if and how much to adjust the following parameters, subject to pre-defined and governance-accepted thresholds:

* GHO Borrow Cap
* GHO Borrow Rate
* GSM Exposure Cap
* GSM Bucket Capacity
* GSM Price Strategy
* GSM Fee Strategy
* GSM Price Range (Freeze, Unfreeze)

The GHO Stewards can increase the GHO Borrow Cap to a threshold of 50M units, with a total borrow cap of 100M, requiring additional Governance approval to increase it further. They can adjust the Borrow Rate gradually, with a maximum adjustment of 500 basis points per 2-day period, up to a maximum of 25% APR. All decisions GHO Stewards make are then published in the Governance Forum for informational purposes. Current GHO market parameters can be found on the [GHO Analytics platform](https://aave.tokenlogic.xyz/borrow-rate).

The GHO Stewards consist of members from Growth ([ACI](https://www.aavechan.com/)), Risk ([Chaos Labs](https://community.chaoslabs.xyz/aave/risk/GHO/overview)), and Finance ([TokenLogic](https://aave.tokenlogic.xyz/) + [karpatkey](https://www.karpatkey.com/projects/aave)) Service Providers and utilize a [3-of-4 multi-sig wallet](https://etherscan.io/address/0x8513e6F37dBc52De87b166980Fa3F50639694B60) for decision-making.

## Merit incentive program
 
The "Merit" program uses a merkle-tree-based periodic airdrop system designed to reward Aave-aligned user behaviors and enhance protocol competitiveness. The initiative started with a budget of 2.1M$ in WETH and 2.9M$ in GHO, totaling 5M$ for a 90-day duration in March 2024. It was then accepted by Aave's Governance to be extended for another 12 months for a total budget of $20M/year ([[ARFC] Merit is forever reward system program extension](https://governance.aave.com/t/arfc-merit-is-forever-reward-system-program-extension/17336)). The [Aave Chan Initiative](https://www.aavechan.com/) (ACI) independently proposed "Merit" while Aave Treasury finances the program. The ACI estimates that as the supply of GHO reaches ~125M, the costs of "Merit" will be offset by the interest produced by GHO.

![image](https://hackmd.io/_uploads/SJYnqRrBC.png)
*The current boost is offering 16.8% additional Safety Module staking APR. Source: [Aave](https://app.aave.com/staking/), June 11th, 2024*

![image](https://hackmd.io/_uploads/r1QyoRSrA.png)
*The current boost offsets 4.46% of the current borrow rate. Source: [Aave](https://app.aave.com/), June 11th, 2024*

## Roadmap for GHO

GHO's future development focuses on enhancing its accessibility, utility, and scaling within the DeFi ecosystem through the following initiatives:

1. **Cross-chain launch**: Transitioning GHO to a [cross-chain model](https://governance.aave.com/t/arfc-gho-cross-chain-launch/17616) aims to improve its accessibility, liquidity, and appeal to a wider user base. The GHO cross-chain launch [AIP proposal](https://github.com/bgd-labs/aave-proposals-v3/pull/350) is currently being finalized, with an expected launch on the Arbitrum chain.
2. **Chainlink Cross-Chain Interoperability Protocol (CCIP) integration**: CCIP, a standard for secure and efficient cross-chain communication, will be onboarded as a new facilitator for the GHO cross-chain launch, planned when the GHO supply reaches 100M.
3. **Merit Incentives Program**: This ongoing program rewards users who contribute to the growth and stability of the GHO ecosystem, encouraging widespread usage and promoting a robust and resilient stablecoin ecosystem.
4. **Onboarding more facilitators**: Facilitators manage the issuance and redemption of GHO, ensuring that the stablecoin remains well-backed and stable. Entities can apply to become facilitators by submitting a [designated application](https://governance.aave.com/t/arfc-gho-facilitator-onboarding-process-and-application/12929) to Aave's Governance, which will be voted on and initiated if approved. 
5. **Monitoring entities**: These entities are expected to play a crucial role in maintaining a stable GHO peg by dynamically adjusting to market conditions, aiming to ensure a sustainable increase of GHO tokens in circulation.

These initiatives are designed to facilitate the scaling of GHO, enabling increases in borrow caps and promoting broader use of the GHO stablecoin across various platforms.

## Market and Adoption

### Collateral

#### Collateral Distribution

Divided by collateral type, wstETH makes up 34% of GHO's collateral composition, followed by sDAI at 18.1%, WETH at 16.1%, WBTC at 14.1%, and AAVE at 7%. RETH, USDC, LINK, DAI, cbETH, USDT, weETH, and LUSD comprise the remaining 10.7%.

![image](https://hackmd.io/_uploads/B1zdoCSBR.png)
*GHO collateral composition. Source: [ChaosLabs](https://community.chaoslabs.xyz/aave/risk/GHO/risk), June 11th, 2024*

#### Collateral Ratio

All assets Aave accepts as collateral can be used to mint GHO. At the time of writing, GHO has a collateralization ratio above 300%.

![image](https://hackmd.io/_uploads/ryMX_1UB0.png)
*Source: [GHO Analytics](https://aave.tokenlogic.com.au/collateral), June 11th, 2024*

### Supply

At the time of writing, 85M GHO tokens were issued. The borrowing cap stands at 85M and is actively being changed by GHO Stewards. The stabilized and enduring peg of GHO allows for increasing the supply more aggressively, switching from a conservative strategy to one that focuses on scaling the supply of GHO stablecoin.

![image](https://hackmd.io/_uploads/SkSb7kUBA.png)
*Source: [GHO Analytics](https://aave.tokenlogic.com.au/gho), June 11th, 2024*

![image](https://hackmd.io/_uploads/BySVX1ISA.png)
*Current GHO supply. Source: [GHO Analytics](https://aave.tokenlogic.xyz/gho), June 11th, 2024*

### Liquidity pools

The liquidity of GHO on DEX Pools is 11.9M, with the most significant Liquidity Pools being offered on Curve and Balancer.

At the end of February, GHO liquidity on Curve experienced significant growth due to the launch of a new liquidity pool featuring the [GHO/USDe](https://curve.fi/#/ethereum/pools/factory-stable-ng-105/deposit) pair. This pool was heavily incentivized by the [Ethena Shard program](https://mirror.xyz/0xF99d0E4E3435cc9C9868D1C6274DfaB3e2721341/lJHZjwoyS7k2UqfrMeOItH_JqRlmk3yJ8_SkrISGpmA), which played a crucial role in attracting liquidity providers and boosting overall liquidity. The substantial incentives provided by the Ethena Shard program helped drive interest and participation, ensuring the pool's rapid growth and enhancing overall GHO's liquidity.

![image](https://hackmd.io/_uploads/HkRmfa6VC.png)
*Source: [GHO Analytics](https://aave.tokenlogic.com.au/liquidity-pools), June 11th, 2024*

The growing DEX volumes of GHO indicate that the stablecoin is gaining market exposure. This increase in trading activity suggests that more users are recognizing the utility and stability of GHO. Additionally, there is a rising utilization of GHO as a leveraged asset, particularly during bull market periods.
<iframe src="https://dune.com/embeds/2745351/4568568/" frameborder="0" style="width:100%;height:300px;"></iframe>

This liquidity primarily generates organic yield from LP fees, as users earn fees from trading activity within these pools. GHO is paired with other stablecoins in these liquidity pools, such as USDe, USDC, USDT, and crvUSD. The five biggest liquidity pools originate from Curve, Balancer, and Maverick protocols. Additional incentives also play a crucial role in maintaining and growing this liquidity. For example, on Curve, gauge incentives provide a significant portion of LP yield.

It is relevant to point out the differences between pairings with bluechip stablecoins like USDT and USDC versus newer ones like USDe. The GHO/USDe pool, which currently has more liquidity than the USDC and USDT pools combined, is heavily subsidized by the Ethena Shard program. While this subsidy has driven significant growth, it also raises questions about the long-term sustainability of the liquidity. If the incentives from the Ethena Shard program were to decrease, the liquidity might be less sustainable compared to pools paired with established stablecoins like USDT and USDC.

![image](https://hackmd.io/_uploads/ryz9G66NC.png)
*Source: [GHO Analytics](https://aave.tokenlogic.com.au/liquidity-pools), June 11th, 2024*

## Peg history

After the launch, the GHO stablecoin faced difficulties maintaining its peg due to several factors. Initially, the absence of a Peg Stability Module (PSM) limited the mechanisms available to stabilize the peg during periods of market volatility. While it is not definitively proven that the GSM alone is impactful, its introduction aims to enhance stability. Additionally, the initial low demand for GHO necessitated the implementation of incentives to encourage users to mint and utilize the stablecoin. In response to these challenges, Aave's governance actively monitored GHO's market performance, adjusted GHO's market parameters, and introduced the Governance Stability Module (GSM). Following these actions, Aave's governance has adopted a prudent approach to increasing the borrowing cap, opting for incremental adjustments to ensure stability and measured growth.

![image](https://hackmd.io/_uploads/HJRLHk8BC.png)
*GHO price chart and GHO's depeg that lasted until February 2024. Source: [CoinMarketCap](https://coinmarketcap.com/currencies/gho/), June 11th, 2024*

### Holder distribution

More than half of all outstanding GHO tokens are currently staked in [Aave's safety staking module](https://etherscan.io/address/0x1a88df1cfe15af22b3c4c783d4e6f7f9e0c1885d). This significant staking level offers a good risk-adjusted yield for GHO holders and provides a crucial safety net for the protocol. In a severe shortfall or market disruption, these staked tokens can be slashed by up to 99%. This high slashing threshold was decided to offer higher risk-adjusted yields, as Aave and ABPT tokens had only a 30% slashing limit and thus provided lower yields. This slashing mechanism acts as an important buffer, protecting the broader Aave ecosystem by absorbing losses and helping maintain the stability of the GHO stablecoin in case it becomes under-collateralized.

<iframe src="https://dune.com/embeds/3798243/6385884/"/
frameborder="0"
style="width:100%;height:300px;"
></iframe>

### Debt holder distribution

About 47.5% of total GHO debt is held by the top 10 borrowers (out of ~1400 total borrowers). Moreover, most of the sDAI collateral is provided by one borrower.

![image](https://hackmd.io/_uploads/SkYV8JUBC.png)
*Source: [GHO Analytics](https://aave.tokenlogic.com.au/collateral), June 5th, 2024*

## DeFi integrations

There exist different possibilities to earn yield with GHO outside of the Aave ecosystem, most notably:

![output1](https://hackmd.io/_uploads/r1CIIepV0.png)
*Source: [DefiLlama](https://defillama.com/tokenUsage?token=gho), June 5th, 2024*

- **Gearbox**: Users can supply GHO to the [Gearbox lending GHO V3 Pool](https://app.gearbox.fi/pools/0x4d56c9cba373ad39df69eb18f076b7348000ae09) and earn interest paid by borrowers who utilize the pool by borrowing liquidity at higher leverage.
- **f(x) Protocol**: Users can deposit liquidity into the Curve GHO+fxUSD pool, then stake their LP tokens in the [f(x) protocol](https://fx.aladdin.club/earn/) to earn additional rewards, such as governance tokens or other incentives provided by the platform.
- **Paladin**: Users can auto-compound stkAave rewards while earning fees from GHO borrowers through [Dullahan](https://dullahan.paladin.vote/). Borrowers can leverage lower interest rates from stkAAVE's discount power, which Paladin manages.
- **Aura Finance**: GHO can be deposited into [Aura hybrid pools](https://app.aura.finance/), allowing users to earn rewards from the pool's yield farming strategies, achieve a high boost through the protocol-owned veBAL, and accumulate additional AURA rewards.
- **Convex Finance**: LP tokens of GHO pairs on Curve and f(x) can be deposited using the [Convex Protocol](https://www.convexfinance.com/) to earn boosted LP rewards, trading fees, and claim boosted CRV without locking CRV themselves, with zero deposit and withdrawal fees.
- **Beefy Finance**: GHO can be deposited in [Beefy vaults](https://app.beefy.com/) to farm with higher yields. Users can benefit from compounded interest and additional reward tokens as Beefy optimizes yield farming using different strategies.
- **Notional Finance**: GHO can be provided for leveraged liquidity on [Notional V3](https://notional.finance/liquidity-leveraged/mainnet/CreateLeveragedNToken/GHO). Users can provide liquidity, borrow against that liquidity, and then provide more liquidity, earning the spread between the liquidity yield and the chosen borrow rate, but with a higher liquidation risk.

![image](https://hackmd.io/_uploads/SJtQv1LrA.png)
*GHO yield on DeFi protocols and liquidity pools. Source: [DeFiLlama](https://defillama.com/yields?token=GHO), June 5th, 2024*

## Conclusion

GHO, the decentralized stablecoin native to the Aave Protocol, has shown resilience and potential since its July 2023 launch despite initial challenges in maintaining its peg and slower growth. With over 80 million GHO in circulation as of June 2024, the stablecoin's design leverages Aave's V3 liquidity pool and introduces concepts like facilitators and the Safety Staking Module. GHO's stability is supported by over-collateralization, arbitrage incentives, dynamic interest rates, and the GHO Stability Module (GSM), allowing the minting of GHO with other stablecoins as backing.

The Aave DAO is crucial in steering GHO's development, with various entities monitoring and adjusting parameters to ensure stability and growth. The "Merit" Incentive program has boosted GHO's supply and utilization, making it attractive for users and liquidity providers. The high percentage of GHO staked in the Safety Module demonstrates strong user confidence in the stability of stablecoin.

Areas warranting ongoing monitoring and risk management include:

1. **Collateral risk**: Each new collateral asset or parameter change on Aave V3 can alter GHO's risk profile. The protocol must assess each asset's risks and manage the collateral pool to ensure GHO's stability.
2. **Liquidation risk**: The DAO should monitor the user's position health (e.g. [Chaos Labs dashboard](https://community.chaoslabs.xyz/aave/risk/GHO/risk)), liquidation volumes, and incentives to ensure the system can handle market stress.
3. **Stablecoin exposure**: The GSM introduces exposure to exogenous stablecoins, requiring careful monitoring and management of its debt ceiling and supporting assets. At this time, it represents a small proportion of the overall supply.
4. **Governance and parameter risks**: The Aave DAO must actively monitor and adjust GHO-specific parameters based on market conditions, price stability, and borrowing demand.
5. **Safety Module participation**: Incentivizing Aave staking in the Safety Module is crucial for its effectiveness as an insurance fund.

As GHO grows and expands through cross-chain launches and ongoing initiatives, ongoing risk monitoring, governance, and collaboration between the Aave DAO, Risk DAO contributors, and the DeFi community will be essential for its long-term success. Given GHO's resilient peg, more aggressive supply increases are expected. Currently ranking as the 21st largest stablecoin by market cap, GHO is well-positioned to become a profitable stablecoin for the Aave DAO, contributing to the ecosystem's sustainability and growth.
