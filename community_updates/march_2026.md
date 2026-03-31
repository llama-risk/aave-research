# LlamaRisk - Monthly Community Update 

# March 2026

## Overview

LlamaRisk presents our March 2026 monthly update, summarizing key activities and outlining upcoming priorities.

## Highlights

### Recommendations and inputs

#### Asset onboarding
* [\[Direct to AIP\] Onboard USDe & sUSDe June expiry PT tokens on Aave V3 Plasma Instance](https://governance.aave.com/t/direct-to-aip-onboard-usde-susde-june-expiry-pt-tokens-on-aave-v3-plasma-instance/24304/2) - Supported the listing given the long maturity, justifying integration efforts, while highlighting the low TVL of the June maturity pool, which may grow as the April maturity rollover approaches.
* [\[Direct to AIP\] Onboard Strata srUSDe June expiry PT tokens to V3 Core Instance](https://governance.aave.com/t/direct-to-aip-onboard-strata-srusde-june-expiry-pt-tokens-to-v3-core-instance/24313/5) - Supported the listing given the long maturity and its role as a natural rollover destination for April expiry positions with significant collateral, justifying integration efforts.

#### New chain
* [\[ARFC\] Aave V4 Activation on Ethereum Mainnet](https://governance.aave.com/t/arfc-aave-v4-activation-on-ethereum-mainnet/24293/4) - Provided a consolidated analysis of the hub-and-spoke architecture configuration, liquidation parameters, collateral factors, interest rate model settings, and Add/Draw Cap recommendations.

#### GHO related
* [\[Direct-to-AIP\] Increase GHO GSM Capacity on Plasma](https://governance.aave.com/t/direct-to-aip-increase-gho-gsm-capacity-on-plasma/24327/3) - Supported minting and bridging an additional 50M GHO to the Plasma GSM driven by strong incentive-led demand, while recommending close monitoring of further GSM expansion due to its impact on the USDT0 market on Aave V3 Plasma.
* [\[ARFC\] sGHO Launch Configuration](https://governance.aave.com/t/arfc-sgho-launch-configuration/24346/4) - Supported the proposed upgrades to the staked GHO product, including the native yield via ERC-4626 savings vault, while noting the need for frontend safeguards to disable legacy deposits and guide users toward migration.

#### E-modes
* [\[Direct to AIP\] Aave V3 Mantle – Collateral Enablement, eMode Expansion, and Isolation Updates (USDT0, USDe, ETH, XAUT)](https://governance.aave.com/t/direct-to-aip-aave-v3-mantle-collateral-enablement-emode-expansion-and-isolation-updates-usdt0-usde-eth-xaut/24153/2) - Supported enabling XAUt contingent on sufficient liquidity and a live XAU/USD oracle. Recommended delaying WETH removal from isolation and enabling USDT0 as collateral outside E-Mode until liquidity improves.

#### Legal Commentary
* [\[TEMP CHECK\] Aave V4 Licensing](https://governance.aave.com/t/temp-check-aave-v4-licensing/24264/3) - Supported the proposed V4 licensing framework, including providing legal review and draft suggestions in respect of the BUSL license and the CLA.

#### Misc.
* [Raise sUSDe, USDC, and USDT Caps on Aave V3 Aptos](https://governance.aave.com/t/raise-susde-usdc-and-usdt-caps-on-aave-v3-aptos/24202/2) - Supported increasing sUSDe caps, while noting low utilization of USDC/USDT caps and that proposed increases pose no immediate risk concerns.
* [\[ARFC\] Aave <> Chainlink SVR. Multi-network expansion (Base, Arbitrum)](https://governance.aave.com/t/arfc-aave-chainlink-svr-multi-network-expansion-base-arbitrum/24241/4) - Supported expansion to Base and Arbitrum, noting $16M recaptured on Ethereum and the L2 shift from Flashbots MEV-Share to Atlas for onchain auction settlement, while highlighting that core trust assumptions remain intact with Chainlink DON-sourced pricing and Ethereum-equivalent fallback mechanisms.
* [\[ARFC\] Bug Bounty Program on Sherlock](https://governance.aave.com/t/arfc-bug-bounty-program-on-sherlock/24300/2) - Supported launching a dedicated Aave V4 bug bounty, encouraging a progressive incentive model that scales with protocol maturity and TVL growth.
* [\[ARFC\] Manual Risk Agents (manual AGRS migration)](https://governance.aave.com/t/arfc-manual-risk-agents-manual-agrs-migration/24311/2) - Expressed reservations about the proposed design and suggested restructuring Risk Stewards into a 2-of-3 multisig comprising Chaos Labs, LlamaRisk, and Aave Labs.
* [\[Direct to AIP\] Collateral Parameters Adjustment on Aave v3 MegaETH Instance](https://governance.aave.com/t/direct-to-aip-collateral-parameters-adjustment-on-aave-v3-megaeth-instance/24334/3) - Supported enabling general market collateral parameters for WETH, BTC.b, and wstETH to allow mixed-collateral borrowing beyond single E-Mode constraints, and proposed two alternative configuration approaches to optimize market structure.

### Research and analysis
* [LlamaRisk Insights: USDtb Ownership Changes](https://governance.aave.com/t/llamarisk-insights-usdtb-ownership-changes/24220) - Conducted an updated legal review of USDtb following ownership changes, highlighting a tri-party issuance framework (Ethena Labs, Pallas BVI, Anchorage Digital Bank), creation of a dedicated Reserve Trust, and clearer legal distinction between token holders and onboarded clients, with analysis on the resulting impact to the stablecoin’s risk profile.
* [Post-Mortem: Exchange Rate Misalignment on wstETH Core and Prime Instances](https://governance.aave.com/t/post-mortem-exchange-rate-misallignment-on-wsteth-core-and-prime-instances/24269/18) - Assessed root causes and identified gaps in testing and transparency across delegated risk infrastructure, proposing structural improvements including enhanced oversight and LlamaRisk co-signing authority via the RiskSteward role to prevent recurrence.
* [LlamaRisk Insights: Ethena sUSDe Dynamic Cooldown](https://governance.aave.com/t/llamarisk-insights-ethena-susde-dynamic-cooldown/24305) - Analyzed Ethena’s proposal to introduce a dynamic sUSDe unstaking cooldown, replacing the current fixed 7-day period. The proposed mechanism aims to improve the user experience while enhancing secondary-market price stability, which is critical to maintaining sUSDe’s reliability as collateral on Aave.

### Community Engagement
* [Horizon Weekly Highlights](https://governance.aave.com/t/horizon-weekly-highlights/23078/33) - Continued collaborating with the Horizon team on asset due diligence, cap adjustments, and weekly operational updates focused on utilization, user behavior, parameter changes, and a broader macro market overview. As of Week 30, Horizon TVL is around $368M, with $110M in net borrows and $219M in stablecoin supply.
* [Newsletter: This Week in Aave](https://x.com/aaveweekly) -  Continued delivering weekly roundups of Aave governance updates while enhancing content with deeper insights for stakeholders and users.

## Upcoming Focus Areas
* [SVR Dashboard](https://svr.llamarisk.com/) - Working on integrating newly expanded Aave markets on Base and Arbitrum into the SVR analytics dashboard.

We welcome community feedback and suggestions. Please share any questions, ideas, or areas where you would like the LlamaRisk team to focus more.