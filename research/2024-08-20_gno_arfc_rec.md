As discussed, we are providing our review of GNO, and potential removal from isolation mode:

## Recommendation summary

Due to elevated market risk, GNO remains in isolation mode on Aave V3's Gnosis instance. Despite [evident demand for GNO as collateral](https://governance.aave.com/t/arfc-chaos-labs-risk-stewards-increase-supply-and-borrow-caps-on-aave-v3-08-09-2024/18585) and potential revenue from GNO-based LST collateral, insufficient on-chain liquidity and market depth currently preclude recommending removal from isolation mode. The primary concern is that GNO's liquidity on both Ethereum mainnet and Gnosis Chain is inadequate to withstand a large liquidation event without potentially compromising Aave protocol health. Other risks related to GNO as collateral have been satisfactorily mitigated. Reevaluation of GNO's isolation status may be warranted if liquidity conditions improve materially.

[details="Full analysis below"]
## Collateral Risk Assessment

### 1. Asset Fundamental Characteristics

#### 1.1 Asset Overview

GNO functions as the governance token for Gnosis DAO, which develops and maintains a suite of blockchain infrastructure products, including a Layer 1 blockchain, payments application, multi-signature wallet, bridge, venture fund, and experimental UBI scheme. GNO does not serve as gas for the Gnosis Chain.

Key characteristics: GNO is [an ERC20 deployed in August 2020](https://gnosisscan.io/tx/0xab6c24241a46dfa12bf0e33fb7edb4e9af0b46d6163416963c18c18d38dbfe71), offering ~10% APY staking rewards. It is usable for securing the Gnosis Chain through staking, with primary networks being the Gnosis Chain and Ethereum mainnet. Gnosis pays special attention to at-home stakers and [plans to have a node in every country by the end of 2025](https://docs.gnosischain.com/node/).

Initially, some discussion was about [onboarding GNO in April 2022 to Aave V2](https://governance.aave.com/t/arc-add-gno-to-aave-v2/7966), but this still needs to proceed. Instead, when Aave V3 was deployed to Gnosis, [GNO was onboarded in isolation mode](https://governance.aave.com/t/arfc-aave-v3-deployment-on-gnosischain/14695) with conservative initial parameters. Since then, [one attempt has been made to remove the asset from isolation](https://governance.aave.com/t/arfc-update-gno-risk-parameters-on-aave-v3-gnosis-pool/15613), though this did not proceed due to high market concentration. [Parameter changes](https://governance.aave.com/t/arfc-chaos-labs-risk-stewards-increase-supply-and-borrow-caps-on-aave-v3-08-09-2024/18585) have [nonetheless since](https://governance.aave.com/t/arfc-update-gno-risk-parameters-on-aave-v3-gnosis-pool/15613) been [made](https://governance.aave.com/t/arfc-chaos-labs-risk-parameter-updates-gno-on-v3-gnosis/17340).

#### 1.2 Architecture 

As a governance token central to multiple verticals, GNO's architecture is relatively straightforward. It was initially distributed via [a reverse Dutch auction in 2017](https://www.forbes.com/sites/rogeraitken/2017/04/24/gnosis-prediction-market-scores-12-5m-in-record-breaking-crypto-auction/). The token's primary functions are governance and staking, with occasional allocations for ecosystem airdrops. [Karpatkey's upcoming KPK token will reward GNO holders.](https://forum.gnosis.io/t/gip-92-should-gnosis-dao-spin-off-karpatkey-dao-and-deploy-the-kpk-token/8115/7) This limited set of use cases results in reduced architectural complexity and associated risks.

![image|1248x1350, 50%](upload://j9INkY3BSA02xAA2DTfQxc4t7Q5.png)
Source: LlamaRisk

#### 1.3 Tokenomics

GNO has a total supply of 3,000,000 GNO, of which 2,589,589 circulate. This total supply was set with an [onchain vote in 2022](https://snapshot.org/#/gnosis.eth/proposal/0xdeadb69e1c18ea78e6592664d2be34f7705ebb040c0b1788514b39bd9a2e2096). [Large holders on mainnet](https://etherscan.io/token/0x6810e776880c02933d47db1b9fc05908e5386b96#balances) include a bridge to Gnosis Chain, Gnosis DAO's treasury, a Balancer vault and a Binance deposit address. On the Gnosis Chain, large holders include Spark, Aave, a Balancer pool, and a Gnosis treasury.

### 2. Market Risk

Market risk presents the most significant concern for removing GNO from isolation mode on Aave.

#### 2.1 Liquidity

On Ethereum mainnet, approximately $400k GNO/WETH trade is possible below 10% slippage. On the Gnosis Chain, about $1.2m GNO/WETH trade is possible below 10% slippage. Current liquidity levels are insufficient to facilitate efficient liquidations without potentially incurring bad debt for the protocol.

![image|841x402](upload://h3kfjydYucgW9C9a6pDxU9u9Arm.png)
Source: DeFiLlama.com/liquidity, August 19th, 2024

![image|834x401](upload://9WP5JIYVwkKNCcsPNiqEEDEQYs5.png)
Source: DeFiLlama.com/liquidity, August 19th, 2024

#### 2.2 Volatility

GNO exhibits significant price volatility, with a historical range from $14 in 2021 to $600 in 2022. The range has been $100 - $440 in the past year. This volatility is consistent with its role as a governance token for an active DAO.

#### 2.3 Exchange Listings

GNO is listed on reputable centralized and decentralized exchanges with limited depth (approximately $50k at 2% slippage on centralized exchanges).

#### 2.4 Growth

GNO's fixed supply means market capitalization is directly correlated with price. The token has steadily grown over its lifetime, with progressively higher price floors across market cycles.

### 3. Technological Risk

#### 3.1 Smart Contract Risk

As an ERC20 token, GNO itself presents minimal, smart contract risk. Associated infrastructure (staking, governance) has undergone [9 audits](https://docs.gnosischain.com/about/specs/security-audit), with the most recent in 2021. Given the [most recent hard fork on Gnosis Chain was in January 2024](https://docs.gnosischain.com/about/specs/hard-forks/dencun), an updated comprehensive audit may be prudent. Gnosis Chain maintains a [$2M bug bounty program](https://immunefi.com/bug-bounty/gnosischain/information/).

#### 3.2 Price Feed Risk

GNO's Aave market on Gnosis Chain utilizes a [GNO/USD Chainlink oracle](https://data.chain.link/feeds/xdai/mainnet/gno-usd) with 0.5% deviation threshold and 24-hour heartbeat, providing robust price data.

#### 3.3 Dependency Risk

Primary dependencies include Gnosis Chain network stability and activity and Gnosis DAO governance decisions. While these dependencies exist, they do not present outsized risks compared to similar governance tokens.

### 4. Counterparty Risk

#### 4.1 Governance and Regulatory Risk

Gnosis DAO has demonstrated responsible governance practices. However, potential regulatory developments (e.g., MiCA in Europe) could impact key contributors' operations, posing a "known unknown" risk to the ecosystem.

### 4.2 Access Control Risk

GNO on [the xDAI bridge owns Gnosis Chain](https://gnosisscan.io/address/0xf6A78083ca3e2a662D6dd1703c939c8aCE2e268d). This bridge [a 3/7 multisig owns contract](https://gnosisscan.io/address/0x583788f490a278DB2a8d6D7226264b4985f75678). On mainnet, [the contract is immutable.](https://etherscan.io/token/0x6810e776880c02933d47db1b9fc05908e5386b96#readContract) Given that that GNO on Gnosis Chain has been bridged from this contract, the total access control risk is low.

**Note**: This assessment follows the LLR-Aave Framework, a comprehensive methodology for asset onboarding and parameterization in Aave V3. This framework is continuously updated and [available here](https://github.com/llama-risk/aave-research/blob/main/frameworks/aave_v3_framework.md).
[/details]

## Aave V3 Specific Parameters

Llama Risk recommends keeping GNO on Aave V3's Gnosis Chain instance the same (isolated mode, 60k supply cap, 6.5k borrow cap).

