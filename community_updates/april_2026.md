# LlamaRisk - Monthly Community Update 

# April 2026

## Overview

LlamaRisk presents our April 2026 monthly update, summarizing key activities and outlining upcoming priorities.

## Highlights

### Recommendations and inputs

#### Asset onboarding
* [\[ARFC\] Onboard PT-USDG-28MAY2026 to Aave V3 Core Instance](https://governance.aave.com/t/arfc-onboard-pt-usdg-28may2026-to-aave-v3-core-instance/24345/2) - Supported onboarding given the long maturity horizon, which justifies integration efforts, while noting the strong liquidity available in the corresponding Pendle pool.
* [\[ARFC\] Onboard USDai & sUSDai to Aave V3 Arbitrum Instance](https://governance.aave.com/t/arfc-onboard-usdai-susdai-to-aave-v3-arbitrum-instance/23260/9) - Supported onboarding following improvements since the initial assessment, including Barker value warranties for new loans and migration from $wM to PYUSD reserve assets, while noting worsening liquidity and remaining regulatory uncertainties, and therefore recommending conservative initial parameters.
* [\[Direct-to-AIP\] Onboard USDe to the Aave V3 MegaETH Instance](https://governance.aave.com/t/direct-to-aip-onboard-usde-to-the-aave-v3-megaeth-instance/24389/2) - Supported onboarding as USDe is already well established across Aave markets, noting that its MegaETH deployment pass-throughs yield similarly to sUSDe, eliminating the need for a separate sUSDe listing for yield looping strategies.

#### New chain
* [\[ARFC\] Aave V4 Activation on Ethereum Mainnet](https://governance.aave.com/t/arfc-aave-v4-activation-on-ethereum-mainnet/24293/17) - Proposed the first and second rounds of add and draw cap increases across the Core, Prime, and Plus hubs, expanding deposit capacity by $55M and bringing the total add cap ceiling to $80M.

#### E-modes
* [\[Direct to AIP\] Aave V3 Mantle – Collateral Enablement, eMode Expansion, and Isolation Updates (USDT0, USDe, ETH, XAUT)](https://governance.aave.com/t/direct-to-aip-aave-v3-mantle-collateral-enablement-emode-expansion-and-isolation-updates-usdt0-usde-eth-xaut/24153/4) - Supported enabling XAUt contingent on adequate liquidity bootstrapping, while recommending WETH remain restricted to E-Mode due to insufficient on-chain liquidity on Mantle and coordinating with Mantle to address the liquidity shortfall before supporting broader WETH parameter changes.

#### Misc.
* [\[ARFC\] Continued Deprecation Steps of Aave V2 Markets](https://governance.aave.com/t/arfc-continued-deprecation-steps-of-aave-v2-markets/24351/2) - Supported the proposed measures to further deprecate Aave V2 markets, aiming to gradually unwind user positions in a controlled manner while minimizing avoidable liquidations for illiquid assets.
* [\[ARFC\] Manual Risk Agents (manual AGRS migration)](https://governance.aave.com/t/arfc-manual-risk-agents-manual-agrs-migration/24311/6) - Submitted a formal request to transfer ownership of the Risk Council 2/2 multisigs across all instances to Aave Labs and LlamaRisk to ensure uninterrupted operational continuity.

### Research and analysis
* [\[ARFC\] Umbrella Emission Adjustments](https://governance.aave.com/t/arfc-umbrella-emission-adjustments/24415) - Proposed updating Umbrella emissions on V3 Core following declines in underlying aToken yields and significant increases in the DAO’s first-loss deficit offset, which reduce slashing risk and justify lower incentive levels.
* [\[Direct-to-AIP\] Aave V3 Scroll Instance Deprecation](https://governance.aave.com/t/direct-to-aip-aave-v3-scroll-instance-deprecation/24432) - Proposed freezing all reserves on the V3 Scroll instance citing rapid deterioration in onchain liquidity and TVL following ether.fi Cash’s migration to OP Mainnet.
* [rsETH incident — 2026-04-18](https://governance.aave.com/t/rseth-incident-2026-04-18/24481) - Provided details to the community and stakeholders on a potential rsETH exploit and the Guardian’s precautionary freezing of affected markets across deployments, while emphasizing that Aave pools remained safe and operational. Also provided updates on subsequent Risk Steward actions, including [Slope2 reductions](https://governance.aave.com/t/rseth-incident-2026-04-18/24481/32) to maintain sustainable borrow rates.
* [rsETH Incident Report (April 20, 2026)](https://governance.aave.com/t/rseth-incident-report-april-20-2026/24580) - Published a detailed report covering the Kelp LayerZero exploit, Aave’s exposure through attacker positions, defensive actions taken by the Aave Protocol Guardian and Risk Stewards, potential bad debt scenarios, and proposed coverage plans.

### Risk Stewards
The following proposals were published by us to update risk parameters via risk stewards and AIP:
* [Risk Stewards: Change of Supply Cap on Aave V3 Plasma / 2026.04.09](https://governance.aave.com/t/risk-stewards-change-of-supply-cap-on-aave-v3-plasma-2026-04-09/24426)
* [Risk Stewards: Change of Supply Caps on Aave V3 Core & Mantle / 2026.04.09](https://governance.aave.com/t/risk-stewards-change-of-supply-caps-on-aave-v3-core-mantle-2026-04-09/24428)
* [\[Direct to AIP\] Change of Supply Caps and adjustment of E-Mode assets on Aave V3 - 07.04.26](https://governance.aave.com/t/direct-to-aip-change-of-supply-caps-and-adjustment-of-e-mode-assets-on-aave-v3-07-04-26/24396/3)
* [Risk Stewards: Change of Supply & Borrow Caps on Aave V3 Scroll / 2026.04.10](https://governance.aave.com/t/risk-stewards-change-of-supply-borrow-caps-on-aave-v3-scroll-2026-04-10/24430)
* [Risk Stewards: Change of Supply & Borrow Caps on Aave V3 / 2026.04.11](https://governance.aave.com/t/risk-stewards-change-of-supply-borrow-caps-on-aave-v3-2026-04-11/24437)
* [Risk Stewards: Change of Supply Caps on Aave V3 / 2026.04.13](https://governance.aave.com/t/risk-stewards-change-of-supply-caps-on-aave-v3-2026-04-13/24442)
* [Risk Stewards: Supply and Borrow Cap Changes on Aave V3 / 2026.04.15](https://governance.aave.com/t/risk-stewards-supply-and-borrow-cap-changes-on-aave-v3-2026-04-15/24458)
* [Risk Stewards: Supply and Borrow Cap Changes on Aave V3 / 2026.04.17](https://governance.aave.com/t/risk-stewards-supply-and-borrow-cap-changes-on-aave-v3-2026-04-17/24477)
* [Risk Stewards: Supply and Borrow Cap Adjustments on Aave V3 / 2026.04.24](https://governance.aave.com/t/risk-stewards-supply-and-borrow-cap-adjustments-on-aave-v3-2026-04-24/24739)
* [Risk Stewards: Supply Cap Change on Aave V3 / 2026.04.27](https://governance.aave.com/t/risk-stewards-supply-cap-change-on-aave-v3-2026-04-27/24774)
* [Risk Stewards: Supply Cap & PT E-Mode Adjustments on Aave V3 / 2026.04.29](https://governance.aave.com/t/risk-stewards-supply-cap-pt-e-mode-adjustments-on-aave-v3-2026-04-29/24809)

### Community Engagement
* [SVR Dashboard](https://dashboard.llamarisk.com/protocols/aave/svr) - Integrated newly expanded Aave markets on Base and Arbitrum into the SVR analytics dashboard.
* [Chaos Labs Is Leaving Aave](https://governance.aave.com/t/chaos-labs-is-leaving-aave/24386/9) - Assured the community that LlamaRisk is prepared to ensure full continuity of risk services and address any operational gaps following Chaos Labs’ departure, with further details provided in the accompanying post.
* [LlamaRisk: Ensuring Continuity of Aave's Risk Management](https://governance.aave.com/t/llamarisk-ensuring-continuity-of-aaves-risk-management/24397) - Published a detailed overview of our existing responsibilities and a two-phase transition plan, including [immediate co-ownership](https://governance.aave.com/t/llamarisk-ensuring-continuity-of-aaves-risk-management/24397/2) of Manual Risk Steward controls with Aave Labs and a future migration of Automated Risk Steward functions toward a protocol-owned CRE-based architecture.
* [Horizon Weekly Highlights](https://governance.aave.com/t/horizon-weekly-highlights/23078/35) - Continued collaborating with the Horizon team on asset due diligence, cap adjustments, and weekly operational updates focused on utilization, user behavior, parameter changes, and a broader macro market overview. As of Week 32, Horizon TVL is around $365M, with $112M in net borrows and $213M in stablecoin supply.
* [Newsletter: This Week in Aave](https://x.com/aaveweekly) -  Delivered weekly roundups of Aave governance updates while enhancing content with deeper insights for stakeholders and users.

## Upcoming Focus Areas
* [\[ARFC\] Renew LlamaRisk as Risk Service Provider - epoch 4](https://governance.aave.com/t/arfc-renew-llamarisk-as-risk-service-provider-epoch-4/24446) - Submitted our renewal proposal as Aave’s Risk Service Provider approaching one year of engagement, with focus on absorbing departing risk functions and ensuring full V3, V4, and Horizon coverage through protocol-owned CRE-based risk infrastructure.
* Numerous initiatives to support Aave V4 launch and expansion. 

We welcome community feedback and suggestions. Please share any questions, ideas, or areas where you would like the LlamaRisk team to focus more.