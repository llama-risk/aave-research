# LlamaRisk - Monthly Community Update 

# December 2025

## Overview

LlamaRisk presents our December 2025 monthly update, summarizing key activities and outlining upcoming priorities.

## Highlights

### Recommendations and inputs

#### Asset onboarding
- [\[ARFC\] Onboard Strata srUSDe PT tokens to V3 Core Instance](https://governance.aave.com/t/arfc-onboard-strata-srusde-pt-tokens-to-v3-core-instance/23481/2) - Supported onboarding while noting key risks including low secondary market liquidity, high srUSDe supply concentration in a single holder, and short residual PT maturity. The [Strata team committed](https://governance.aave.com/t/arfc-onboard-strata-srusde-pt-tokens-to-v3-core-instance/23481/4) to launching a public bug bounty program in Q1 2026.
- [\[Direct to AIP\] Onboard USDe & sUSDe April expiry PT tokens on Aave V3 Plasma Instance](https://governance.aave.com/t/direct-to-aip-onboard-usde-susde-april-expiry-pt-tokens-on-aave-v3-plasma-instance/23515/2) - Supported the listing given the long maturity justifying integration efforts, while highlighting the significantly lower TVL of the April maturity pool compared to prior expiries.
- [\[ARFC\] Onboard frxUSD to Aave V3 Core Instance on Ethereum](https://governance.aave.com/t/arfc-onboard-frxusd-to-aave-v3-core-instance-on-ethereum/23513/9) - Updated our recommendation to align parameters with the v3.6 update, limiting exposure to the wstLINK/LINK looping use case, while noting no major architectural changes since the initial analysis and high staking demand for LINK relative to the cap increases.
- [\[ARFC\] Onboard wstLINK to Aave V3 Core Instance](https://governance.aave.com/t/arfc-onboard-wstlink-to-aave-v3-core-instance/22169/13) - Updated our recommendation to align parameters with the v3.6 update limiting exposure to the wstLINK/LINK looping use case and noted no major architectural changes since our initial analysis while noting higher staking demand for LINK than the cap raises.
- [\[Direct to AIP\] Onboard syrupUSDC to Aave V3 Base Instance](https://governance.aave.com/t/direct-to-aip-onboard-syrupusdc-to-aave-v3-base-instance/23234/4) - Supported onboarding following successful supply bootstrap, with DEX liquidity fully provided by Maple, robust administrative controls including a timelock, and no new structural changes identified since our prior assessments.

#### New chain
- [\[ARFC\] Deploy Aave v3 on Mantle](https://governance.aave.com/t/arfc-deploy-aave-v3-on-mantle/20542/11) - Supported the proposed parameters, noting MNT as the only new asset for Aave, with supply and borrow cap recommendations to follow based on expected network liquidity from the Mantle team.

#### E-modes
- [\[Direct-to-AIP\] Ethena February PTs Caps and E-Modes Adjustments](https://governance.aave.com/t/direct-to-aip-ethena-february-pts-caps-and-e-modes-adjustments/23501/3) - Supported the parameter updates and inclusion of sUSDe in E-Modes to simplify position management, while recommending extending flexibility further by enabling USDe as collateral.
- [\[Direct-to-AIP\] Enhancing Market Granularity in Aave v3.6: Restricting Borrowability and Collateralization Outside of Liquid eModes](https://governance.aave.com/t/direct-to-aip-enhancing-market-granularity-in-aave-v3-6-restricting-borrowability-and-collateralization-outside-of-liquid-emodes/23592/3) - Supported the proposed parameter changes aligned with the v3.6 upgrade, enabling cleanup of legacy configurations and stricter control of volatile assets through E-Modes.

#### Legal Commentary
- [\[ARFC\] $AAVE token alignment. Phase 1 - Ownership](https://governance.aave.com/t/arfc-aave-token-alignment-phase-1-ownership/23616/61) - Delivered an independent legal risk analysis clarifying claims of “effectuated protocol ownership” within Aave. The work examined governance-approved funding, IP considerations, and the DAO’s de facto control absent a formal chain of title.

#### Misc.
- [\[Direct to AIP\] XAUt Supply Cap and Debt Ceiling Adjustment on Aave V3 Core Instance](https://governance.aave.com/t/direct-to-aip-xaut-supply-cap-and-debt-ceiling-adjustment-on-aave-v3-core-instance/23466/3) - Supported the proposed increases, noting the asset’s risk profile remains unchanged since our prior analysis, with stable DEX liquidity and a doubled onchain supply.
- [\[Direct-to-AIP\] Renewal of Umbrella Reward Allowances](https://governance.aave.com/t/direct-to-aip-renewal-of-umbrella-reward-allowances/23474/2) - Recommended adjusting USDT emissions in line with the upcoming [Umbrella Coverage Expansion ARFC](https://snapshot.box/#/s:aavedao.eth/proposal/0x838d242eeaa71d926e5acf1b1af504bcde8b7f02345445e3c7b50dac0ce1db4a) to prevent future complexity.
- [\[Direct-to-AIP\] Alter mUSD Oracle Price Implementation](https://governance.aave.com/t/direct-to-aip-alter-musd-oracle-price-implementation/23489/3) - Supported the temporary switch to a hardcoded 1 USD oracle, noting that downside price risk is borne by borrowers and that this approach remains appropriate as long as mUSD is not enabled as collateral, which could otherwise expose Aave to bad debt risk in the event of backing loss.

### Research and analysis
- [LlamaRisk Insights: GHO’s Backing and RWA Integration, A Portfolio Analysis](https://governance.aave.com/t/llamarisk-insights-gho-s-backing-and-rwa-integration-a-portfolio-analysis/23521) - Analyzed GHO’s backing and RWA integration, concluding that diversification mathematically strengthens collateral resilience against crypto cyclicality, while noting trade-offs from inorganic growth via private deals that prioritize diversification over near-term revenue.
- [LlamaRisk Insights: Umbrella Coverage Principles and Slashing Logic](https://governance.aave.com/t/llamarisk-insights-umbrella-coverage-principles-and-slashing-logic/23527) - Clarified Umbrella’s role as an on-chain backstop for realized reserve deficits rather than a blanket insurance layer, explaining how the DAO-funded Deficit Offset acts as the true first-loss protection and when Umbrella staking liquidity is expected to be utilized.

### Community Engagement
- [Horizon Weekly Highlights](https://governance.aave.com/t/horizon-weekly-highlights/23078/19) - Continued collaborating with the Horizon team on asset due diligence, cap adjustments, and weekly operational updates focused on utilization, user behavior, and parameter changes. As of Week 16, Horizon TVL surpassed $562M, with $178M in net borrows and $310M in stablecoin supply.
- [Bug Bounty Call Out](https://x.com/LlamaRisk/status/2000935153774866474) - Concluded the weekly Twitter series highlighting Aave-listed assets with low bug bounty coverage. Positive outcomes include MetaMask adding mUSD to its $50K HackerOne program and public bug bounty commitments from Paxos (USDG, PYUSD, PAXG, USDP) and StrataFi (PT-srUSDe).
- [Newsletter: This Week in Aave](https://x.com/aaveweekly) -  Continued delivering weekly roundups of Aave governance updates while enhancing content with deeper insights for stakeholders and users.


## Upcoming Focus Areas
- [Aave V4 Preparation](https://aave.com/docs/aave-v4) - Actively working on internal V4-related R&D while participating in the Office Hours for DAO Service Providers to align on technical and risk framework updates.

We welcome community feedback and suggestions. Please share any questions, ideas, or areas where you would like increased focus from the LlamaRisk team.