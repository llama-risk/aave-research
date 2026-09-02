# LlamaRisk - Monthly Community Update 

# August 2026

## Overview

LlamaRisk presents our August 2026 monthly update, summarizing key activities and outlining upcoming priorities.

## Highlights

### Recommendations and inputs

#### Asset onboarding
* [\[Direct-to-AIP\] PT-USDG X Layer](https://governance.aave.com/t/direct-to-aip-pt-usdg-x-layer/25464/3) - Supported onboarding given the long maturity horizon justifying integration efforts, while noting the newly bootstrapped $5M liquidity and absence of immediate rollover demand from expiring PTs, implying that collateral adoption is expected to build gradually.
* [\[Direct to AIP\] Onboard PT-srUSDe-22OCT2026 to Aave V4 Plus Hub](https://governance.aave.com/t/direct-to-aip-onboard-pt-srusde-22oct2026-to-aave-v4-plus-hub/25498/2) - Supported onboarding while noting $4.5M liquidity and the prior maturity on the V3 Ethereum Core market, which provides a reference for expected demand and potential rollover to V4.
* [\[ARFC\] Onboard PAXG to the Global Dollar Hub in Aave V4 Ethereum](https://governance.aave.com/t/arfc-onboard-paxg-to-the-global-dollar-hub-in-aave-v4-ethereum/25340/4) - Supported onboarding PAXG as a collateral-only, non-borrowable reserve, conditional on implementing timelocks on upgrade paths, which Paxos confirmed, and noted DEX LP concentration with a single entity with the underlying custody agreement verified under NDA.
* [\[Direct-to-AIP\] Asset Listing - USDC X Layer](https://governance.aave.com/t/direct-to-aip-asset-listing-usdc-x-layer/25467/2) - Supported onboarding while noting nascent DEX liquidity following its recent deployment, which is expected to deepen as supply grows, alongside native minting and bridging via CCTP. Given the limited initial liquidity, onboarding caps were adjusted downward accordingly.
* [\[ARFC\] Onboard cirBTC on Aave v3 Core and Aave V4 Core](https://governance.aave.com/t/arfc-onboard-cirbtc-on-aave-v3-core-and-aave-v4-core/25128/5) - Provided onboarding parameters and supported onboarding conditional on Circle successfully bootstrapping the committed liquidity on Ethereum.
* [\[Direct to AIP\] Onboard PT-sUSDe-26NOV2026 to Aave V4 Plus Hub](https://governance.aave.com/t/direct-to-aip-onboard-pt-susde-26nov2026-to-aave-v4-plus-hub/25497/2) - Supported onboarding given the long maturity horizon justifying integration efforts, while noting the absence of a prior active maturity on Aave to provide a reference for rollover and initial demand.

#### Misc.
* [\[ARFC\] Upgrade PT Risk Oracle to Protocol-Owned Infrastructure on CRE](https://governance.aave.com/t/arfc-upgrade-pt-risk-oracle-to-protocol-owned-infrastructure-on-cre/25119/4) - Provided an update on the Ethereum deployment of the PT Risk Oracle stack proposed in the ARFC, covering deployed addresses, underlying Chainlink CRE workflows, and bounds for the activation AIP. Confirmed ownership remains with the Aave Ethereum Executor, with the Aave Protocol Guardian as agent admin and no LlamaRisk EOA holding any role in the stack.

### Research and analysis
* [\[ARFC\] Liquidation Protocol Fee Increase for WBTC, WETH, and wstETH on Aave V3 Ethereum Core](https://governance.aave.com/t/arfc-liquidation-protocol-fee-increase-for-wbtc-weth-and-wsteth-on-aave-v3-ethereum-core/25470) - Reviewed the LPF configuration, which determines the share of liquidation bonuses accrued to the Aave Treasury. Noted that while higher LPF increases protocol revenue, it also suppresses marginal liquidations as LPF and SVR draw from the same liquidation bonus. Under conservative assumptions, Aave’s revenue per dollar liquidated peaks near a 30% fee and falls below current levels at 40%, therefore recommending 20% as the appropriate step at this stage.

### Risk Stewards
The following proposals were published by us to update risk parameters via risk stewards:
* [Risk Stewards: Supply Cap Increases on Aave V3 / 2026.08.03](https://governance.aave.com/t/risk-stewards-supply-cap-increases-on-aave-v3-2026-08-03/25430)
* [Risk Stewards: Supply Cap Changes on Aave V3 / 2026.08.07](https://governance.aave.com/t/risk-stewards-supply-cap-changes-on-aave-v3-2026-08-07/25448)
* [Risk Stewards: Supply and Borrow Cap Reductions on Aave V3 / 2026.08.10](https://governance.aave.com/t/risk-stewards-supply-and-borrow-cap-reductions-on-aave-v3-2026-08-10/25463)
* [Risk Stewards: Supply and Borrow Cap Increases on Aave V3 / 2026.08.11](https://governance.aave.com/t/risk-stewards-supply-and-borrow-cap-increases-on-aave-v3-2026-08-11/25465)
* [Risk Stewards: IRM Changes on Aave V3 Monad / 2026.08.13](https://governance.aave.com/t/risk-stewards-irm-changes-on-aave-v3-monad-2026-08-13/25475)
* [Risk Stewards: Supply Cap Increases on Aave V3 / 2026.08.14](https://governance.aave.com/t/risk-stewards-supply-cap-increases-on-aave-v3-2026-08-14/25483)
* [Risk Stewards: PT Parameter Changes on Aave V3 / 2026.08.15](https://governance.aave.com/t/risk-stewards-pt-parameter-changes-on-aave-v3-2026-08-15/25491)
* [Risk Stewards: Supply Cap Reductions on Aave V3 / 2026.08.18](https://governance.aave.com/t/risk-stewards-supply-cap-reductions-on-aave-v3-2026-08-18/25502)
* [Risk Stewards: Supply Cap Increases on Aave V3 / 2026.08.24](https://governance.aave.com/t/risk-stewards-supply-cap-increases-on-aave-v3-2026-08-24/25523)
* [Risk Stewards: Supply Cap Increases on Aave V3 / 2026.08.25](https://governance.aave.com/t/risk-stewards-supply-cap-increases-on-aave-v3-2026-08-25/25527)
* [Risk Stewards: Stablecoin IRM Changes on Aave V3 / 2026.08.27](https://governance.aave.com/t/risk-stewards-stablecoin-irm-changes-on-aave-v3-2026-08-27/25533)
* [Risk Stewards: Supply Cap Changes on Aave V3 / 2026.08.27](https://governance.aave.com/t/risk-stewards-supply-cap-changes-on-aave-v3-2026-08-27/25537)
* [Risk Stewards: Cap and IRM Changes on Aave V3 / 2026.08.31](https://governance.aave.com/t/risk-stewards-cap-and-irm-changes-on-aave-v3-2026-08-31/25571)

#### V4 Cap Updates
We proposed additional rounds of add-and-draw cap increases across the Ethereum and Avalanche hubs, raising the total supply cap ceiling to approximately $802M to accommodate growing demand as multiple reserves approached their limits.
* [Add and Draw Cap Increases: Round 12 / 2026.08.03](https://governance.aave.com/t/arfc-aave-v4-activation-on-ethereum-mainnet/24293/40)
* [Add and Draw Cap Increases: Round 13 / 2026.08.12](https://governance.aave.com/t/arfc-aave-v4-activation-on-ethereum-mainnet/24293/42)
* [Add and Draw Cap Increases: Round 14 / 2026.08.20](https://governance.aave.com/t/arfc-aave-v4-activation-on-ethereum-mainnet/24293/45)
* [Add and Draw Cap Increases: Round 15 / 2026.08.28](https://governance.aave.com/t/arfc-aave-v4-activation-on-ethereum-mainnet/24293/47)

### Community Engagement
* [LlamaGuard PT Explainer](https://x.com/LlamaRisk/status/2087547080956887377): Published a thread explaining the mechanics of the new automated risk oracle for Pendle PT collateral on Aave, built on Chainlink CRE.

## Upcoming Focus Areas
* [Risk Stewards](https://dashboard.llamarisk.com/protocols/aave/risk-parameter-updates): Maintain day-to-day risk parameter operations across Aave V3 and V4.
* **Aave V4 Growth**: Monitor V4 adoption and propose further add and draw cap increases across Ethereum and Avalanche.
* **SVR Support**: Expand SVR analytics to support upcoming deployments on Avalanche, Polygon, and BNB Chain.
* **RWA Assessments**: Continue due diligence for new assets including tokenized stocks and provide ongoing risk support across the Horizon RWA pipeline.

We welcome community feedback and suggestions. Please share any questions, ideas, or areas where you would like the LlamaRisk team to focus more.