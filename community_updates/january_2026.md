# LlamaRisk - Monthly Community Update 

# January 2026

## Overview

LlamaRisk presents our January 2026 monthly update, summarizing key activities and outlining upcoming priorities.

## Highlights

### Recommendations and inputs

#### Asset onboarding
- [\[Direct to AIP\] Onboard USDe & sUSDe May expiry PT tokens on Aave V3 Core Instance](https://governance.aave.com/t/direct-to-aip-onboard-usde-susde-may-expiry-pt-tokens-on-aave-v3-core-instance/23882/2) - Supported the listing given the long maturity justifying integration efforts, while highlighting the significantly lower TVL of the April maturity pool compared to prior expiries.

#### New chain
- [\[ARFC\] Deploy Aave v3 on Mantle](https://governance.aave.com/t/arfc-deploy-aave-v3-on-mantle/20542/14) - Supported the proposed caps and analyzed the liquidity conditions for the proposed assets, while highlighting that ongoing liquidity bootstrapping efforts are not yet sufficient to fully support the current cap levels for few select assets.
- [\[ARFC\] Deploy Aave V3 to MegaETH](https://governance.aave.com/t/arfc-deploy-aave-v3-to-megaeth/23517/32) - Supported launching with conservative initial parameters, recommending a limited asset set and restricting borrowing to E-Modes enabled by the v3.6 upgrade, allowing flexible collateral isolation and structuring the market around USDm and USDT0 as blue-chip stablecoins.
    - [USDm](https://governance.aave.com/t/arfc-deploy-aave-v3-to-megaeth/23517/33) - Supported onboarding of USDm, a white-label stablecoin powered by Ethena, while highlighting the multiple layers of infrastructural dependency involved.
    - [BTC.b](https://governance.aave.com/t/arfc-deploy-aave-v3-to-megaeth/23517/34) - Supported onboarding of the Lombard-acquired BTC wrapper with conservative initial parameters until liquidity depth sufficiently matures.

#### E-modes
- [\[Direct to AIP\] Enable XAUt e-Mode on Aave v3.6 Core Instance](https://governance.aave.com/t/direct-to-aip-enable-xaut-e-mode-on-aave-v3-6-core-instance/23879/2) - Supported enabling a dedicated XAUt E-Mode, transitioning from isolation mode to a targeted E-Mode with tightly scoped borrowables under the v3.6 upgrade.
- [\[Direct to AIP\] Addition of Isolated Bluechip Collateral E-Modes on Aave v3](https://governance.aave.com/t/direct-to-aip-addition-of-isolated-bluechip-collateral-e-modes-on-aave-v3/23926/2) - Supported introducing segregated E-Modes for WETH, cbBTC, and WBTC to contain borrowing risk within bluechip assets, while noting potential UX friction from added E-Mode choices that should be mitigated at the UI level.

#### Misc.
- [\[ARFC\] Umbrella Risk Oracles](https://governance.aave.com/t/arfc-umbrella-risk-oracles/23897/2) - Supported automating and dynamically calibrating Umbrella parameters, while noting the proposal’s focus on emissions optimization diverges from our DAO-ratified Umbrella methodology centered on external risk factors to Aave. Proposed a collaborative path using our methodology to anchor coverage targets with the oracle framework adjusting emissions.
- [\[ARFC\] Deficit Realization Risk Oracle: Forcing Timely Bad-Debt Recognition via Dust-Collateral Cleanup](https://governance.aave.com/t/arfc-deficit-realization-risk-oracle-forcing-timely-bad-debt-recognition-via-dust-collateral-cleanup/23896/2) - Supported the creation of a risk oracle to automate cleanup of economically insolvent but mechanically non-deficit positions, enabling timely bad-debt recognition and allowing Umbrella to provide coverage without delay.
- [\[Direct to AIP\] MKR and USDtb Oracle adjustments](https://governance.aave.com/t/direct-to-aip-mkr-and-usdtb-oracle-adjustments/23911/2) - Supported updating MKR oracle configurations as liquidity migration to SKY increased volatility and manipulation risk in the legacy feed, and endorsed a fixed 1 USD oracle for USDtb since it is not enabled as collateral and to mitigate transient volatility from thin liquidity.

### Research and analysis
- [Hubs & Spokes in Aave V4: A Risk-Centric Analysis](https://governance.aave.com/t/hubs-spokes-in-aave-v4-a-risk-centric-analysis/23907) - Published a risk-focused deep dive on the Hubs & Spokes architecture in V4, mapping the theoretical infrastructure design space available to the protocol. The analysis illustrates how liquidity, risk segmentation, and asset integration can be structured using four distinct architectural models and Hub-to-Spoke credit lines, highlighting the trade-offs across different configurations.


### Community Engagement
- [Horizon Weekly Highlights](https://governance.aave.com/t/horizon-weekly-highlights/23078/24) - Continued collaborating with the Horizon team on asset due diligence, cap adjustments, and weekly operational updates focused on utilization, user behavior, and parameter changes. As of Week 16, Horizon TVL surpassed $550M, with $151M in net borrows and $335M in stablecoin supply.
- [Newsletter: This Week in Aave](https://x.com/aaveweekly) -  Continued delivering weekly roundups of Aave governance updates while enhancing content with deeper insights for stakeholders and users and in addition provided a [2025 annual recap](https://x.com/aaveweekly/status/2008538944821235997) covering the key upgrades, governance decisions, and growth moments that shaped the protocol.


## Upcoming Focus Areas
- [Aave V4 Preparation](https://aave.com/docs/aave-v4) - Actively working on internal V4-related R&D while participating in the Office Hours for DAO Service Providers to align on technical and risk framework updates.

We welcome community feedback and suggestions. Please share any questions, ideas, or areas where you would like increased focus from the LlamaRisk team.