# LlamaRisk - Monthly Community Update 

# February 2026

## Overview

LlamaRisk presents our February 2026 monthly update, summarizing key activities and outlining upcoming priorities.

## Highlights

### Recommendations and inputs

#### Asset onboarding
* [\[Direct to AIP\] Onboard BTC.b to Aave V3 Core Instance](https://governance.aave.com/t/direct-to-aip-onboard-btc-b-to-aave-v3-core-instance/23357/5) - Supported onboarding following the successful migration to Lombard’s security model, noting protocol-supplied DEX liquidity, low onchain supply, and the presence of robust administrative safeguards, including a timelock and active bug bounty.
* [\[Direct to AIP\] Onboard sUSDe and USDe to Aave V3 Base Instance](https://governance.aave.com/t/direct-to-aip-onboard-susde-and-usde-to-aave-v3-base-instance/24121/2) - Supported onboarding contingent on improved liquidity conditions, while noting the absence of a timelock and low onchain supply on Base.
* [\[ARFC\] Deploy Aave V3 to MegaETH: cUSD & stcUSD](https://governance.aave.com/t/arfc-deploy-aave-v3-to-megaeth/23517/50) - Provisionally supported onboarding subject to improved liquidity depth, noting the absence of a native cUSD/USD feed (temporarily relying on USDC/USD given >95% USDC reserves) and the lack of a bad-debt handling mechanism for loaned reserves, which could overstate cUSD value in a backing loss scenario.


#### New chain
* [\[ARFC\] Deploy Aave v3 on X Layer](https://governance.aave.com/t/arfc-deploy-aave-v3-on-x-layer/23175/10) - Supported the initial parameter setup and onboarding of a strategic subset of native "xAssets," while limiting the broader market to stablecoin borrowing (USDT0, USDG, GHO) via specialized E-Modes.
    * [xSOL](https://governance.aave.com/t/arfc-deploy-aave-v3-on-x-layer/23175/11) - Supported onboarding of xSOL, an OKX-managed wrapper, while highlighting centralized management via MPC-based access controls and noting that the SOL/USD price feed remains under development.
    * [xOKSOL](https://governance.aave.com/t/arfc-deploy-aave-v3-on-x-layer/23175/12) - Supported onboarding of xOKSOL, the first Solana-based LST on Aave, while highlighting limited liquidity and the absence of a SOL/USD oracle feed, which remains a prerequisite for onboarding.
    * [xETH](https://governance.aave.com/t/arfc-deploy-aave-v3-on-x-layer/23175/16) - Supported onboarding with conservative supply caps and risk limits, highlighting high supply concentration in OKX-linked addresses and low DEX TVL, and emphasizing the need for greater non-OKX holder dispersion and diversified liquidity over time.
    * [xBETH](https://governance.aave.com/t/arfc-deploy-aave-v3-on-x-layer/23175/17) - Supported onboarding of xBETH, a yield-bearing wrapper of OKX’s internal BETH with a monotonic exchange rate updated on a 24-hour cadence, while highlighting limited DEX liquidity and residual risks tied to validator performance on OKX’s Prysm stack, off-chain slashing coverage commitments, and redemption timelines (13 days to several weeks).

#### E-modes
* [\[ARFC\] Introduction of Segregated Bluechip Collateral E-Modes on Aave v3](https://governance.aave.com/t/arfc-introduction-of-segregated-bluechip-collateral-e-modes-on-aave-v3/23924/2) - Supported the proposal as it offers a distinct value proposition for risk-averse borrowers aiming to eliminate rehypothecation risk; recommended aligning LTV/LT with Isolated Bluechip E-Modes, standardizing a 5% LB across segregated BTC markets, and gating sWETH supply cap increases based on core WETH utilization to preserve looping stability.

#### Legal Commentary
* [\[Direct to AIP\] Onboard BTC.b to Aave V3 Core Instance](https://governance.aave.com/t/direct-to-aip-onboard-btc-b-to-aave-v3-core-instance/23357/4) - Provided clarification on Lombard’s terms and compliance controls, including treatment of mixer exposure as an AML/sanctions trigger.

#### Misc.
* [\[ARFC\] Revenue-indexed deficit offsets for Umbrella](https://governance.aave.com/t/arfc-revenue-indexed-deficit-offsets-for-umbrella/24000/2) - Supported the goal of aligning the DAO's first-loss committment with realized profitability from liquidation events and reserve revenue.
* [Chaos Labs Risk Stewards - Supply and Borrow Caps Reduction Across Low Demand Assets on Aave V3 - 10.02.26](https://governance.aave.com/t/chaos-labs-risk-stewards-supply-and-borrow-caps-reduction-across-low-demand-assets-on-aave-v3-10-02-26/24037/2) - Recommended a precautionary reduction of FBTC’s supply and borrow caps due to low secondary market liquidity and increasing concentrated debt exposure from a single borrower.
* [\[Direct-to-AIP\] Increase WBTC Liquidation Bonus and EURS Reserve Factor on Polygon V3](https://governance.aave.com/t/direct-to-aip-increase-wbtc-liquidation-bonus-and-eurs-reserve-factor-on-polygon-v3/24029/2) - Supported the parameter updates given EURS illiquidity on Polygon leading to persistent bad debt, and endorsed increasing WBTC’s liquidation bonus to better compensate liquidators for cross-chain liquidity costs.
* [\[ARFC\] Umbrella Risk Oracles](https://governance.aave.com/t/arfc-umbrella-risk-oracles/23897/4) - Established a collaboration model for the Umbrella Risk Oracle, extending its scope to update `targetLiquidity` in line with jointly aligned monthly recommendations.


### Research and analysis
* [Unlocking Yield: Aave V4's Reinvestment Controller](https://governance.aave.com/t/unlocking-yield-aave-v4s-reinvestment-controller/24002) - Presented a data-driven framework to deploy idle protocol liquidity, noting that Aave averaged $1.16B in idle USDT in 2025, and outlining how allocating this float to low-risk yield strategies (e.g., money market funds or short-term Treasuries) could enhance deposit rates and create a sustainable revenue stream for the DAO.
* [LlamaRisk Insights: Institutional Legal Setup for Reinvestment Controller](https://governance.aave.com/t/llamarisk-insights-institutional-legal-setup-for-reinvestment-controller/24087) - As a follow-up to our V4 Reinvestment Controller research, outlined practical pathways for Aave DAO to access regulated off-chain products (e.g., fund subscriptions and institutional lending), including considerations for establishing a legal entity to act as the DAO’s contracting agent.
* [Retro: WETH utilization spike and Slope2 Risk Oracle performance](https://governance.aave.com/t/retro-weth-utilization-spike-and-slope2-risk-oracle-performance/24101) - Published a report analyzing Slope2 oracle behavior during two volatility-driven WETH utilization spikes on Aave V3 Ethereum Core, and requested a detailed post-mortem and greater transparency from ChaosLabs regarding delegated rate-setting mechanisms.
* [LlamaRisk Insights: Custom Stablecoins — A Retail Opportunity for Aave](https://governance.aave.com/t/llamarisk-insights-custom-stablecoins-a-retail-opportunity-for-aave/24107) - Analyzed the emergence of institution-issued custom stablecoins and outlined how Aave, particularly through V4’s Hub-and-Spoke architecture, can leverage issuer distribution networks to position itself as a scalable yield and savings layer for institutional-grade stablecoin ecosystems.

### Community Engagement
* [Horizon Weekly Highlights](https://governance.aave.com/t/horizon-weekly-highlights/23078/28) - Continued collaborating with the Horizon team on asset due diligence, cap adjustments, and weekly operational updates focused on utilization, user behavior, and parameter changes. As of Week 26, Horizon TVL is around $446M, with $99M in net borrows and $304M in stablecoin supply.
* [Newsletter: This Week in Aave](https://x.com/aaveweekly) -  Continued delivering weekly roundups of Aave governance updates while enhancing content with deeper insights for stakeholders and users.

## Upcoming Focus Areas
* [Aave V4 Preparation](https://aave.com/docs/aave-v4) - Actively working on internal V4-related R&D while participating in the Office Hours for DAO Service Providers to align on technical and risk framework updates.

We welcome community feedback and suggestions. Please share any questions, ideas, or areas where you would like the LlamaRisk team to focus more.
