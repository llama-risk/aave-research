# LlamaRisk - Monthly Community Update 

# November 2025

## Overview

LlamaRisk presents our November 2025 monthly update, summarizing key activities and outlining upcoming priorities.

## Highlights

### Recommendations and inputs

#### Asset onboarding
- [\[Direct to AIP\] Onboard BTC.b to Aave V3 Core Instance](https://governance.aave.com/t/direct-to-aip-onboard-btc-b-to-aave-v3-core-instance/23357/2) - Recommended putting the proposal on hold as the token had not yet launched on Ethereum and was mid-migration to Lombard Finance, involving changes to its security model and new contract deployments.
- [\[Direct to AIP\] Onboard USDe & sUSDe February expiry PT tokens on Aave V3 Core Instance](https://governance.aave.com/t/direct-to-aip-onboard-usde-susde-february-expiry-pt-tokens-on-aave-v3-core-instance/23358/2) - Supported listing given the long maturity that justifies integration efforts, while noting reduced PT demand from lower sUSDe yields and limited pool liquidity, and therefore recommended conservative initial supply caps.
- [\[ARFC\] Onboard tUSDe December expiry PT tokens on Aave V3 Core Instance](https://governance.aave.com/t/arfc-onboard-tusde-december-expiry-pt-tokens-on-aave-v3-core-instance/22958/7) - Noted that the Terminal team announced the project will not launch, resulting in abandonment of PT-tUSDe onboarding, and provided analysis on the subsequent impact of this announcement on Pendle market behavior.

#### E-modes
- [\[Direct to AIP\] weETH E-Mode Risk Parameter Adjustment on Aave V3 Plasma Instance](https://governance.aave.com/t/direct-to-aip-weeth-e-mode-risk-parameter-adjustment-on-aave-v3-plasma-instance/23381/2) - Supported the proposal and its parameters as they align with the goal of mitigating volatile debt–collateral exposure and managing early-market uncertainty, while noting reduced DEX liquidity may create potential liquidation bottlenecks.
- [\[Direct to AIP\] Add WETH to the wrsETH wstETH E-Mode on Aave V3 Base Instance](https://governance.aave.com/t/direct-to-aip-add-weth-to-the-wrseth-wsteth-e-mode-on-aave-v3-base-instance/23431/2) - Supported adding WETH to the E-Mode configuration as it introduces minimal incremental risk while offering users greater flexibility to access ETH liquidity against the restaking token.
- [\[Direct to AIP\] Add WETH to the rsETH LST E-Mode on Aave Core Instance](https://governance.aave.com/t/direct-to-aip-add-weth-to-the-rseth-lst-e-mode-on-aave-core-instance/23425/2) - Supported the proposal given the strong asset correlation, available borrow capacity, and revenue opportunity, while noting that it introduces minimal incremental risk.

#### Misc.
- [\[Direct to AIP\] Reinstate Supply and Borrow Caps on Aave V3 Gnosis Instance](https://governance.aave.com/t/direct-to-aip-reinstate-supply-and-borrow-caps-on-aave-v3-gnosis-instance/23373/2) - Reviewed the proposed parameters and expressed support for the reinstated caps.
- [\[Direct to AIP\] Freeze wstETH on Plasma](https://governance.aave.com/t/direct-to-aip-freeze-wsteth-on-plasma/23400/2) - Supported freezing wstETH on Plasma, noting minimal user impact due to low supply and deposits, and highlighted Lido’s planned rollout of the CCT standard across chains, which will require consideration for Aave’s future deployments.
- [\[ARFC\] Chaos Risk Agents](https://governance.aave.com/t/arfc-chaos-risk-agents/23401/2) - Supported the proposal and clarified key details with Chaos Labs, noting that Aave Governance will retain the Hub superadmin role and manage all Agent permissions, no additional multisig is expected, automation will rely on the Aave Robot (via Chainlink) with Gelato as a fallback, and the architecture is open source for reuse by all service providers.
- [\[ARFC\] Remove USDS as collateral and increase RF across all Aave Instances](https://governance.aave.com/t/arfc-remove-usds-as-collateral-and-increase-rf-across-all-aave-instances/23426/3) - Supported the proposal to remove USDS as collateral, given its altered risk profile as Sky allocates USDS to additional protocols via Stars, increasing the risk surface of the backing collateral.

### Community Engagement
- [Horizon Weekly Highlights](https://governance.aave.com/t/horizon-weekly-highlights/23078/11) - Continued collaborating with the Horizon team on asset due diligence, cap adjustments, and weekly operational updates focused on utilization, user behavior, and parameter changes. As of Week 13, Horizon TVL surpassed $571M, with $176M in net borrows and $294M in stablecoin supply.
- [Bug Bounty Call Out](https://x.com/LlamaRisk/status/1986444578061156638) - Continued our weekly Twitter series highlighting Aave-listed assets with low bug bounty coverage, providing updates informed by our [Bug Bounty Landscape Report](https://governance.aave.com/t/llamarisk-insights-bug-bounty-landscape-for-assets-listed-on-aave/23044). A notable development: [Paxos publicly committed](https://governance.aave.com/t/arfc-onboard-usdg-to-aave-v3-core-instance/23271/4) to launching a public bug bounty in Q1 2026 covering their assets (USDG, PYUSD, PAXG, USDP) and related APIs.
- [Newsletter: This Week in Aave](https://x.com/aaveweekly) -  Continued delivering weekly roundups of Aave governance updates while enhancing content with deeper insights for stakeholders and users.


## Upcoming Focus Areas
- [Aave V4 Preparation](https://aave.com/docs/aave-v4) - Actively working on internal V4-related R&D while participating in the Office Hours for DAO Service Providers to align on technical and risk framework updates.

We welcome community feedback and suggestions. Please share any questions, ideas, or areas where you would like increased focus from the LlamaRisk team.