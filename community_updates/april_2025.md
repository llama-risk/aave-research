# LlamaRisk - Monthly Community Update 

# April 2025

## Overview

LlamaRisk presents our April 2025 monthly update, summarizing key activities and outlining upcoming priorities.

## Highlights

### Recommendations and inputs

#### Asset onboarding
- [\[ARFC\] Onboard tETH to Aave v3 Prime Instance](https://governance.aave.com/t/arfc-onboard-teth-to-aave-v3-prime-instance/21873/5) - Supported the onboarding while noting centralization risks, absence of a timelock, and limited yet sufficient liquidity.
- [\[ARFC\] Onboard sUSDe July expiry PT tokens on Aave V3 Core Instance](https://governance.aave.com/t/arfc-onboard-susde-july-expiry-pt-tokens-on-aave-v3-core-instance/21878/3) - Supported onboarding given the relatively long maturity horizon, which justifies integration effort and offers extended utility over single-maturity assets.
- [\[ARFC\] Add EURC to Sonic V3 Instance](https://governance.aave.com/t/arfc-add-eurc-to-sonic-v3-instance/21835/4) - Recommended onboarding conditional on the deployment of a Chainlink EURC price feed, while noting that the EURC on Sonic is a bridged version not natively issued by Circle.
- [\[ARFC\] Add EURC to Aave V3 Core Instance](https://governance.aave.com/t/arfc-add-eurc-to-aave-v3-core-instance/21837/3) - Supported onboarding while highlighting the absence of Circle CCTP support for EURC and the reliance on EOAs for admin roles, with unclear use of MPC wallets
- [\[ARFC\] Add EURe to Linea V3 Instance](https://governance.aave.com/t/arfc-add-eure-to-linea-v3-instance/21840/3) - Did not recommend onboarding due to critically low DEX liquidity, high token concentration, and minimal on-chain supply on Linea.
- [\[ARFC\] Onboard eUSDe PT Tokens to Aave v3 Core Instance](https://governance.aave.com/t/arfc-onboard-eusde-pt-tokens-to-aave-v3-core-instance/21767/4) - Offered tentative support citing short remaining maturity and declining yield driven by reduced interest in the speculative Ethereal points program.
- [\[ARFC\] Onboard MNT, mETH, cmETH as collateral assets on Aave v3 Mantle Instance](https://governance.aave.com/t/arfc-onboard-mnt-meth-cmeth-as-collateral-assets-on-aave-v3-mantle-instance/21772/2) - Supported onboarding MNT while advising against mETH and cmETH due to low liquidity.
- [\[ARFC\] Onboard eUSDe to Aave v3 Core Instance](https://governance.aave.com/t/arfc-onboard-eusde-to-aave-v3-core-instance/21766/2) - Supported onboarding while flagging limited documentation, unverified implementation of features, low liquidity, inactive bug bounty, and a risk profile likely to evolve as more functionalities go live.
- [ARFC: Onboarding wETH to Aave V3 Celo Instance](https://governance.aave.com/t/arfc-onboarding-weth-to-aave-v3-celo-instance/21750/2) - Recommended onboarding while noting constrained liquidity and supply due to Celo’s recent transition into an Ethereum L2.
- [\[ARFC\] Onboard USDtb to Aave v3 Core Instance](https://governance.aave.com/t/arfc-onboard-usdtb-to-aave-v3-core-instance/21746/2) - Supported onboarding while highlighting low DEX liquidity relative to on-chain supply and high concentration among Ethena-associated wallets.
- [\[ARFC\] Add EURC to Avalanche V3 Instance](https://governance.aave.com/t/arfc-add-eurc-to-avalanche-v3-instance/21734/3) - Supported onboarding while noting lack of Circle CCTP support, use of EOAs for admin roles, and highly concentrated DEX liquidity on Avalanche.
- [\[ARFC\] Onboard sUSDS to Aave V3 Base Instance](https://governance.aave.com/t/arfc-onboard-susds-to-aave-v3-base-instance/21741/3) - Supported onboarding while referencing [prior analysis on the unstaked version](https://governance.aave.com/t/temp-check-onboard-usds-and-susds-to-aave-v3/18806/8) and associated risks.
- [\[ARFC\] Onboard lisUSD to Aave V3 BNB Instance](https://governance.aave.com/t/arfc-onboard-lisusd-to-aave-v3-bnb-instance/21571/2) - Recommended onboarding as a borrowable asset with conservative parameters, highlighting concerns around centralized governance and limited legal clarity.
- [\[ARFC\] Add AAVE token to Aave V3 Base Instance](https://governance.aave.com/t/arfc-add-aave-token-to-aave-v3-base-instance/21105/5) - Supported onboarding based on sufficient liquidity and market maturity of AAVE on Base.

#### New chain
- [\[ARFC\] Aave V3 Deployment on Aptos Mainnet](https://governance.aave.com/t/arfc-aave-v3-deployment-on-aptos-mainnet/21823/3) - Supported deployment and provided asset onboarding recommendations tailored to Aptos market conditions.

#### GHO related
- [\[ARFC\] GHO Savings Upgrade](https://governance.aave.com/t/arfc-gho-savings-upgrade/21680/3) - Supported the revised proposal to implement sGHO & ASR mechanism and provided analysis focusing on critical areas like DAO funding sustainability, the ASR-borrow rate balance, reliance on a single market’s yield, peg stability, and architectural complexity of the proposed architecture.

#### E-modes
- [\[ARFC\] Remove USDe Debt Ceiling and Introduce USDe Stablecoins E-mode](https://governance.aave.com/t/arfc-remove-usde-debt-ceiling-and-introduce-usde-stablecoins-e-mode/21876/2) -  Supported removal of the debt ceiling citing USDe’s safe usage profile and effective redemptions during periods of market stress.
- [\[ARFC\] LRT and wstETH Unification](https://governance.aave.com/t/arfc-lrt-and-wsteth-unification/21739/2) - Supported the proposed parameter changes and E-mode configurations, while conducting an in-depth analysis of potential slashing risks across these LST assets.

#### Legal Commentary
- [\[ARFC\] Horizon’s RWA Instance](https://governance.aave.com/t/arfc-horizon-s-rwa-instance/21898/4) - Expressed support for the initiative.
- [\[Temp Check\] Horizon’s RWA Instance](https://governance.aave.com/t/temp-check-horizon-s-rwa-instance/21740/13) - Expressed availability to assist Aave Labs with confidential design aspects, while raising legal and regulatory questions to enhance clarity for the DAO.
- [Update on FDUSD Uncertainty and Relevant Guardian Activity](https://governance.aave.com/t/update-on-fdusd-uncertainty-and-relevant-guardian-activity/21669/2) - Delivered timely legal insights and summarized developments following Justin Sun’s insolvency allegations against FDUSD.

#### Misc.
- [\[ARFC\] Interest Rate Curve Risk Oracle](https://governance.aave.com/t/arfc-interest-rate-curve-risk-oracle/21900/2) - Provided our support to the proposal while highlighting the need to carefully manage the risks of centralized risk oracle logic against operational gains. 
- [\[ARFC\] Aave <> Bored Ghosts Developing. Phase 5](https://governance.aave.com/t/arfc-aave-bored-ghosts-developing-phase-5/21803/7) - Expressed strong support for @bgdlabs' continued service to the Aave ecosystem.
- [\[ARFC\] Further Deprecate sUSD on Aave V3 Optimism](https://governance.aave.com/t/arfc-further-deprecate-susd-on-aave-v3-optimism/21770/2) - Supported deprecation measures due to sUSD's diminished peg stability following recent changes to Synthetix's pool 420.
- [\[ARFC\] Onboard Pendle PT tokens to Aave V3 Core Instance](https://governance.aave.com/t/arfc-onboard-pendle-pt-tokens-to-aave-v3-core-instance/20541/8) - Supported @bgdlabs’ dynamic linear discount rate oracle proposal for accurate pricing of Pendle’s Principal Tokens (PTs).
- Signed emergency transactions related to [rsETH precautionary freezing 30/04/2025](https://governance.aave.com/t/rseth-precautionary-freezing-30-04-2025/21925).

### Research and analysis
- [LlamaRisk's Insights: The Pectra Upgrade](https://governance.aave.com/t/llamarisks-insights-the-pectra-upgrade/21829) - Delivered detailed analysis on how Ethereum’s upcoming Pectra upgrade may alter the risk landscape for LSTs and LRTs.
- [\[ARFC\] Aave Umbrella - activation](https://governance.aave.com/t/arfc-aave-umbrella-activation/21521/22) - Shared insights into our Umbrella methodology to recommend parameters and manage risk in collaboration with other members of the Aave Finance Committee (AFC).

### Community Engagement
- [Newsletter: This Week in Aave](https://x.com/aaveweekly) - Continued delivering weekly roundups of Aave governance updates while enhancing content with deeper insights for stakeholders and users.

## Upcoming Focus Areas
- [\[ARFC\] Renew LlamaRisk as Risk Service Provider - epoch 3](https://governance.aave.com/t/arfc-renew-llamarisk-as-risk-service-provider-epoch-3/21666) - Following the successful renewal, we aim to continue centering our services to Aave DAO around in-depth and actionable risk assessments. The key strategic initiatives include Umbrella parameterization, SVR, RWA collaboration, and sGHO rollout support.
- [LlamaRisk Risk Metrics Dashboard](https://score.llamarisk.com/) - Launched the initial version under [Operation Spring Cleaning](https://www.llamarisk.com/research/spring-cleaning), enabling users to track, analyze, and compare risk metrics across assets and chains.
- In the final stages of deploying a dashboard to monitor and analyze the performance of Chainlink’s SVR mechanism within Aave.
- Completed initial peer review and are now finalizing backtesting our methodology for Umbrella liquidity targets.

We welcome community feedback and suggestions. Please share any questions, ideas, or areas where you would like increased focus from the LlamaRisk team.
