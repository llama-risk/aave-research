# LlamaRisk - Monthly Community Update 

# September 2025

## Overview

LlamaRisk presents our September 2025 monthly update, summarizing key activities and outlining upcoming priorities.

## Highlights

### Recommendations and inputs

#### Asset onboarding
- [\[ARFC\] Onboard tUSDe December expiry PT tokens on Aave V3 Core Instance](https://governance.aave.com/t/arfc-onboard-tusde-december-expiry-pt-tokens-on-aave-v3-core-instance/22958/2) - Recommended halting onboarding following preliminary review of the base asset tUSDe and its PT token, citing insufficient clarity around Terminal DEX mechanics and the full bridging process. We are in the process of clarifying the details and will provide further comments shortly.
- [\[ARFC\] Onboard LsETH to Aave V3 Core Instance](https://governance.aave.com/t/arfc-onboard-lseth-to-aave-v3-core-instance/22957/2) - Supported onboarding as a collateral-only asset while highlighting risks from limited circulating supply and potentially slow price discovery under stress conditions.
- [\[Direct to AIP\] Onboard sUSDe and USDe to Aave V3 Avalanche Instance](https://governance.aave.com/t/direct-to-aip-onboard-susde-and-usde-to-aave-v3-avalanche-instance/23081/2) - Supported onboarding while highlighting the relatively low DEX liquidity and limited trading venues for both assets on Avalanche. 
- [\[ARFC\] Add MetaMask USD (mUSD) to Aave v3 Core Instance on Ethereum and Linea](https://governance.aave.com/t/arfc-add-metamask-usd-musd-to-aave-v3-core-instance-on-ethereum-and-linea/23097/2) - Supported onboarding while flagging indirect exposure to Superstate’s USTB RWA, limited sell-side liquidity on Ethereum, and **coordinated with the MetaMask team to include mUSD contracts under their bug bounty program**.

#### New chain
- [\[ARFC\] Deploy Aave v3 on Plasma](https://governance.aave.com/t/arfc-deploy-aave-v3-on-plasma/21494/6) - Supported deployment with a provisional recommendation in light of the chain’s bootstrapping phase.

#### E-modes
- [\[ARFC\] sAVAX LTV & LT Adjustment](https://governance.aave.com/t/arfc-savax-ltv-lt-adjustment/23080/2) - Supported the parameter changes and the addition of the new sAVAX/WAVAX E-mode as they introduce minimal incremental risk.
- [\[Direct to AIP\] Addition of cbBTC/Stablecoin E-Mode to Aave V3 Base Instance](https://governance.aave.com/t/direct-to-aip-addition-of-cbbtc-stablecoin-e-mode-to-aave-v3-base-instance/23174/2) - Supported the proposal as this new type of E-Mode could drive stablecoin borrowing demand and boost market competitiveness, while posing contained risks given cbBTC’s stable liquidity and strong BTC peg on Base.

#### Misc.
- [\[ARFC\] Aave Asset class Allowlist (AAcA)](https://governance.aave.com/t/arfc-aave-asset-class-allowlist-aaca/22597/9) - Shared the initial framework draft with the DAO for feedback. The AAcA provides a structured classification of assets into six groups: Stablecoins, Wrapped Assets, Staking & Restaking Derivatives, Protocol Tokens, Tokenized Financial Instruments, and Specialized & Uncategorized Assets, ensuring clarity for new assets, consistent guidance for community members and SPs, and systematic risk assessment across similar asset categories. The ARFC has later been approved by the DAO and is now in full effect.
- [\[ARFC\] Adopt The SEAL Safe Harbor Agreement](https://governance.aave.com/t/arfc-adopt-the-seal-safe-harbor-agreement/23059/5) - Supported the initiative, given the SEAL team’s strong reputation, noting it adds another layer of security for Aave, similar to points raised in our [bug bounty roundup](https://governance.aave.com/t/llamarisk-insights-bug-bounty-landscape-for-assets-listed-on-aave/23044).
- [\[Direct to AIP\] Increase rsETH Supply Cap on Aave V3 Linea Instance](https://governance.aave.com/t/direct-to-aip-increase-rseth-supply-cap-on-aave-v3-linea-instance/23073/3) - Supported the proposal as caps remain consistently maxed, reflecting strong demand and a stable peg demonstrated by wrsETH on Linea.
- [\[Direct-to-AIP\] pyUSD Parameters Optimization](https://governance.aave.com/t/direct-to-aip-pyusd-parameters-optimization/23082/2) - Supported the changes as they pose no incremental risks, noting that the lower borrow APR could increase pool utilization while slightly reducing revenue from the decreased reserve factor.
- [\[Direct to AIP\] Risk Parameter Adjustments for Aave V3 Scroll Instance](https://governance.aave.com/t/direct-to-aip-risk-parameter-adjustments-for-aave-v3-scroll-instance/23113/3) - Supported the proposal as a measured response to the current Scroll governance situation, ensuring minimal adverse impact on Aave V3 Scroll users.
- [\[Direct to AIP\] Raise sUSDe and USDe November expiry PT tokens caps on Aave V3 Core Instance](https://governance.aave.com/t/direct-to-aip-raise-susde-and-usde-november-expiry-pt-tokens-caps-on-aave-v3-core-instance/23117/4) - Supported the proposal to enable smooth rollover from September PT expiry, while noting a temporary risk of liquidity crunch; recommended enacting the AIP around the PT maturity on September 25, 2025.
- [\[ARFC\] Safety Module & Umbrella Emission Update](https://governance.aave.com/t/arfc-safety-module-umbrella-emission-update/23103/4) - Supported phasing out legacy staking modules, noting a 10 bps WETH Umbrella APR reduction from lower max emissions, and recommended close monitoring of potential user outflows. 
- [\[Risk Stewards\] WETH Borrow Rate Update](https://governance.aave.com/t/risk-stewards-weth-borrow-rate-update/23129/3) - Supported the phased reduction of the WETH Slope1 parameter, highlighting that higher utilization driven by the lower borrow rate reduces available liquidity by $0.36B.
- [Aave DAO’s State of the Union by ACI](https://governance.aave.com/t/aave-dao-s-state-of-the-union-by-aci/23124/14) - Provided feedback while broadly supporting ACI’s roadmap, and emphasized the value of improving coordination and communication through regular monthly or quarterly calls with all service providers.

### Research and analysis
- [LlamaRisk Insights: Bug Bounty Landscape for Assets listed on Aave](https://governance.aave.com/t/llamarisk-insights-bug-bounty-landscape-for-assets-listed-on-aave/23044) - Discussed the bug bounty landscape for assets listed on Aave and included planned recommendations for improving coverage, incentivization, and overall protocol security.
- [LlamaRisk Insights: Umbrella Launch](https://governance.aave.com/t/llamarisk-insights-umbrella-launch/23067) - Delivered a comprehensive performance review of Aave Umbrella Safety Module’s first three months, highlighting a 43% year-to-date reduction in cost per dollar of coverage, enhanced slashing efficiency, and $164M in inflows from non-Aave DeFi venues.
- [LlamaRisk Insights: GHO in the context of Genius Act](https://governance.aave.com/t/llamarisk-insights-gho-in-the-context-of-genius-act/23111) - Presented an analysis of the recently enacted GENIUS Act and its applicability to the GHO token.
- [\[ARFC\] Endorse the Asset Classification Framework (AAcA)](https://governance.aave.com/t/arfc-endorse-the-asset-classification-framework-aaca/23114) - Published the ARFC to formalize @bgdlabs’ AAcA proposal, establishing a collaborative framework for Aave service providers to streamline and standardize the asset onboarding process.

### Community Engagement
- [LlamaGuard NAV](https://x.com/LlamaRisk/status/1971300167363199305): Introduced a purpose-built, dynamic risk-adjusted oracle solution for Horizon, developed in collaboration with Chainlink and Aave. [Full blog available](https://www.llamarisk.com/research/llamaguard-release) detailing its architecture and functionality.
- [Horizon Weekly Highlights](https://governance.aave.com/t/horizon-weekly-highlights/23078) - Collaborating with the Horizon team on pre-launch due diligence for assets, we initiated a weekly update summarizing operations, with a focus on utilization metrics, user behavior, and parameter changes.
- [Bug Bounty Call Out](https://x.com/LlamaRisk/status/1965405009266278677) - Launched a weekly Twitter series highlighting assets onboarded on Aave with low bug bounty coverage, providing clear updates and context based on our [Bug Bounty Landscape Report](https://governance.aave.com/t/llamarisk-insights-bug-bounty-landscape-for-assets-listed-on-aave/23044).
- [Newsletter: This Week in Aave](https://x.com/aaveweekly) -  Continued delivering weekly roundups of Aave governance updates while enhancing content with deeper insights for stakeholders and users.

## Upcoming Focus Areas
- Umbrella Expansion - Recommending the next phase of asset inclusion under Umbrella to achieve optimal Safety Module coverage across Aave markets.
- [Aave V4 Preparation](https://aave.com/blog/understanding-aave-v4s-architecture) - Actively reviewing the proposed architectural changes introduced in the V4 codebase shared with DAO Service Providers and adapting our current risk frameworks to ensure a seamless transition.

We welcome community feedback and suggestions. Please share any questions, ideas, or areas where you would like increased focus from the LlamaRisk team.
