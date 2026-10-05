# LlamaRisk - Monthly Community Update 

# September 2026

## Overview

LlamaRisk presents our September 2026 monthly update, summarizing key activities and outlining upcoming priorities.

## Highlights

### Recommendations and inputs

#### Asset onboarding
* [\[ARFC\] Onboard HINC (Neuberger Securitize High Income Tokenized Fund) to Aave Horizon](https://governance.aave.com/t/arfc-onboard-hinc-neuberger-securitize-high-income-tokenized-fund-to-aave-horizon/25500/7) - Supported onboarding with a 55% LTV, 67% LT, and a GHO E-Mode, conditional on Securitize placing the `MASTER` upgrade role behind a timelock and formalizing response-time and settlement SLAs with KPK, Lhava, and Fission as liquidators, both of which will be verified before activation.
* [\[Direct to AIP\] Onboard BTC.b to Aave V4 Core Instance on Ethereum](https://governance.aave.com/t/direct-to-aip-onboard-btc-b-to-aave-v4-core-instance-on-ethereum/25532/2) - Supported onboarding as a collateral-only reserve, conditional on Lombard segregating BTC custody between BTC.b and LBTC, which are currently backed by a pooled custody structure. The asset benefits from a 1-day timelock on upgrades and $7.9M DEX liquidity, albeit supplied almost entirely by the Lombard team. A full risk assessment was [provided separately](https://governance.aave.com/t/btc-b-on-aave-ethereum/25652/2).
* [\[ARFC\] Onboard EURCV to Aave V4 Core Instance on Ethereum](https://governance.aave.com/t/arfc-onboard-eurcv-to-aave-v4-core-instance-on-ethereum/25624/3) - Conditionally supported onboarding of the Societe Generale-Forge Euro stablecoin pending the launch of a bug bounty program, while noting issuer-reported reserve attestations and a peg comparable to EURC since its introduction. A full risk assessment was [provided separately](https://governance.aave.com/t/eur-coinvertible-eurcv-on-aave-ethereum/25655/2).
* [\[Direct to AIP\] Onboard USDe to Aave V4 Core Instance on Avalanche](https://governance.aave.com/t/direct-to-aip-onboard-usde-to-aave-v4-core-instance-on-avalanche/25576/2) - Supported onboarding as a collateral-only reserve on a new Ethena Ecosystem Spoke with conservative initial caps given the $0.5M DEX liquidity, and flagged the OFT timelock whitelist allowing `setPeer` to bypass the 24-hour delay and the absence of a separate pauser mechanism. At the time of review, a timelock on USDe was missing on some prominent networks like Solana and Plasma, with Ethena working to extend coverage across the remaining networks over the coming weeks. A full risk assessment was [provided separately](https://governance.aave.com/t/ethena-usde-on-aave-avalanche-assessments/25669/2).
* [Coinbase B20 Equities on Base Assessments](https://governance.aave.com/t/coinbase-b20-equities-on-base-assessments/25690/2) - Provided a technical review of the seven tokenized stocks proposed for the Aave V4 Base Equities Hub, each representing certificates over shares held in segregated custody under an ADGM bare trust and offered under an FSRA-approved prospectus. Noted that secondary holders, including liquidators, are treated as unvested holders without redemption rights until completing the issuer’s vesting process, with no dedicated liquidator path, requiring seized collateral to be sold or hedged. Also highlighted that issuer contract roles resolve to EOAs without multisig or timelock controls, while the corporate action multiplier can be changed instantly and the issuer pauses the price feed around such events.
* [\[ARFC\] Onboard mWIN (Midas / Wellington Management) to Aave Horizon](https://governance.aave.com/t/arfc-onboard-mwin-midas-wellington-management-to-aave-horizon/25536/8) - Supported onboarding with a 67% LTV, 72% LT, and an initial 80 mWIN supply cap, identifying credit spread widening on the CLO-heavy book as the primary risk, with Wellington agreeing to a 4-year spread duration cap following our suggestion. Holder concentration also remains high during the bootstrapping phase, with the top three investors holding about 73% of supply. The [market risk analysis](https://governance.aave.com/t/arfc-onboard-mwin-midas-wellington-management-to-aave-horizon/25536/9) found the manager's worst forward scenario of -2.54% understates the tail, as the model book's March 2020 backtest drew down 13.32%, roughly 17% on the live book's higher spread duration, with defaults adding little relative to mark-to-market losses. The daily NAV recognizes drawdowns within one business day, unlike the 66-day write-down lag seen on Midas' mF-ONE, so parameters were set more conservatively than operational evidence alone would allow.
* [\[ARFC\] Onboard syrupUSDC to Aave V4 on Arc](https://governance.aave.com/t/arfc-onboard-syrupusdc-to-aave-v4-on-arc/25721/2) - Supported onboarding as a collateral-only reserve on a new Maple Spoke with a 20% Collateral Risk to price syrupUSDC's credit exposure against the shared Core Hub USDC liquidity. The main residual risk is the minting role on Arc, which lacks a timelock, though Maple has committed to placing it behind one. A full risk assessment was [provided separately](https://governance.aave.com/t/syrup-usdc-syrupusdc-on-aave-arc-assessments/25729/2).

#### New chain
* [\[ARFC\] Deploy Aave V4 on Arc](https://governance.aave.com/t/arfc-deploy-aave-v4-on-arc/25170/10) - Provided risk assessments for the initial listing assets, with access control across all asset and bridge contracts relying on EOAs under Circle's key management program and no timelocks on upgrades, consistent with Circle's model on other networks.
    * [USDC](https://governance.aave.com/t/circle-usd-usdc-on-aave-arc-assessments/25645/3) - Can be natively minted on Arc and bridged via CCTP, with transfers capped at 10M USDC each.
    * [EURC](https://governance.aave.com/t/circle-eur-eurc-on-aave-arc-assessments/25646/3) - Issued natively alongside CCTPx bridging, with rate limits of 862K EURC per transfer and 4.31M EURC per six hours.
    * [cirBTC](https://governance.aave.com/t/circle-wrapped-bitcoin-cirbtc-on-aave-arc-assessments/25647/3) - Minting is permissioned through Circle Mint, and cross-chain transfers over CCTPx are limited to 9 cirBTC per transfer and 135 cirBTC per six hours.
    * [WETH](https://governance.aave.com/t/wrapped-ether-weth-on-aave-arc-assessments/25648/3) - Bridged via CCTPx with backing escrowed on Ethereum, while noting unclaimed owner and pauser slots and an implementation the CCTS owner can replace in a single action.
* [\[ARFC\] Deploy Aave V4 on Base](https://governance.aave.com/t/arfc-deploy-aave-v4-on-base/25427/5) - Proposed initial parameters for a dedicated Equities Hub listing the Magnificent Seven tokenized stocks in Coinbase B20 form as collateral against USDC, with collateral factors and a 5.5% liquidation bonus sized around 24/5 price feeds and weekend gaps, and caps bound by issuer mint allowance and perpetual open interest. A full technical review was [provided separately](https://governance.aave.com/t/coinbase-b20-equities-on-base-assessments/25690/2).

#### Misc.
* [\[ARFC\] Upgrade PT Risk Oracle to Protocol-Owned Infrastructure on CRE](https://governance.aave.com/t/arfc-upgrade-pt-risk-oracle-to-protocol-owned-infrastructure-on-cre/25119/5) - Provided an update on the deployment of the PT Risk Oracle stack on Aave V3 Plasma for PT-sUSDe-22OCT2026, byte-equivalent to the Certora-audited Ethereum deployment, with agent registration remaining a governance action and the Aave Protocol Guardian retaining a per-agent kill switch.

### Research and analysis
* [\[ARFC\] Unified Handling of the Isolated Flag in Aave V3.7 E-Modes](https://governance.aave.com/t/arfc-unified-handling-of-the-isolated-flag-in-aave-v3-7-e-modes/25621) - Published a proposal establishing a single rule for the Aave v3.7 E-Mode `isolated` flag: an E-Mode should be isolated only when it allows borrowing an asset that has general borrowing disabled. On this basis, proposed isolating 15 E-Modes, mostly wstETH and ETHx looping categories, and de-isolating 3 E-Modes whose borrowable assets all have general markets. Of the ~$777M debt in affected E-Modes, only ~$445K is backed by outside collateral, and existing positions keep their terms but cannot be increased.
* [\[ARFC\] Revision of ETH & BTC Collateral Efficiency on Aave](https://governance.aave.com/t/arfc-revision-of-eth-btc-collateral-efficiency-on-aave/25649) - Proposed raising LTV and LT for the ETH and BTC collateral families on Aave V3 Ethereum Core, Arbitrum, and Base, including WETH to 81%/84% and WBTC and cbBTC to 81%/85% on Core, and collateral factors on the Aave V4 Main Spoke to 81-85%. Thresholds were calibrated to the 99.9th percentile of 1-hour price excursions, based on measured liquidation processing across the February and October 2025 stress events.

### Risk Stewards
The following proposals were published by us to update risk parameters via risk stewards:
* [Risk Stewards: Stablecoin IRM Changes on Aave V3 / 2026.09.02](https://governance.aave.com/t/risk-stewards-stablecoin-irm-changes-on-aave-v3-2026-09-02/25586)
* [Risk Stewards: Cap and IRM Changes on Aave V3 / 2026.09.04](https://governance.aave.com/t/risk-stewards-cap-and-irm-changes-on-aave-v3-2026-09-04/25594)
* [Risk Stewards: Cap and IRM Changes on Aave V3 / 2026.09.07](https://governance.aave.com/t/risk-stewards-cap-and-irm-changes-on-aave-v3-2026-09-07/25601)
* [Risk Stewards: Cap and IRM Changes on Aave V3 / 2026.09.09](https://governance.aave.com/t/risk-stewards-cap-and-irm-changes-on-aave-v3-2026-09-09/25611)
* [Risk Stewards: IRM Changes on Aave V3 / 2026.09.11](https://governance.aave.com/t/risk-stewards-irm-changes-on-aave-v3-2026-09-11/25627)
* [Risk Stewards: Cap and IRM Changes on Aave V3 / 2026.09.15](https://governance.aave.com/t/risk-stewards-cap-and-irm-changes-on-aave-v3-2026-09-15/25641)
* [Risk Stewards: Cap and IRM Changes on Aave V3 / 2026.09.16](https://governance.aave.com/t/risk-stewards-cap-and-irm-changes-on-aave-v3-2026-09-16/25653)
* [Risk Stewards: Cap and IRM Changes on Aave V3 / 2026.09.18](https://governance.aave.com/t/risk-stewards-cap-and-irm-changes-on-aave-v3-2026-09-18/25668)
* [Risk Stewards: Supply and Borrow Cap Changes on Aave V3 / 2026.09.22](https://governance.aave.com/t/risk-stewards-supply-and-borrow-cap-changes-on-aave-v3-2026-09-22/25685)
* [Risk Stewards: Cap and IRM Changes on Aave V3 / 2026.09.28](https://governance.aave.com/t/risk-stewards-cap-and-irm-changes-on-aave-v3-2026-09-28/25718)

#### V4 Cap Updates
We proposed additional rounds of add-and-draw cap increases across the Ethereum, Avalanche, and Arc hubs, raising the total supply cap ceiling to approximately $1.99B to accommodate growing demand as multiple reserves approached their limits.
* [Add and Draw Cap Increases: Round 16 / 2026.09.04](https://governance.aave.com/t/arfc-aave-v4-activation-on-ethereum-mainnet/24293/49)
* [Add and Draw Cap Increases: Round 17 / 2026.09.16](https://governance.aave.com/t/arfc-aave-v4-activation-on-ethereum-mainnet/24293/51)
* [Add and Draw Cap Increases: Round 18 / 2026.09.25](https://governance.aave.com/t/arfc-aave-v4-activation-on-ethereum-mainnet/24293/52)

### Community Engagement
* [LlamaGuard PT Dashboard](https://dashboard.llamarisk.com/products/actions/pt/pt-srusde-22oct2026): Launched the first protocol-owned risk oracle on Aave, built by LlamaRisk on the Chainlink Runtime Environment (CRE) and owned by Aave, which dynamically manages Pendle PT collateral risk, starting with Aave V3 Ethereum ahead of expansion to all Aave PT markets.
* [Aave V4 Base Dashboard](https://dashboard.llamarisk.com/protocols/aave/v4/topology?chain=8453): Added support for the Aave V4 Base deployment, mapping the Equities Hub and its per-asset credit lines and tracking all seven tokenized stocks, including during market closures.
* [Tokenized Stock Lending on Aave V4 Base](https://x.com/LlamaRisk/status/2104658014435254507): Published an analysis of the first weekend of tokenized stock lending following its September 25 launch, with findings including that most borrowing activity occurred while equity markets were closed, the first liquidation took place before the weekend, and more.

## Upcoming Focus Areas
* [Risk Stewards](https://dashboard.llamarisk.com/protocols/aave/risk-parameter-updates): Maintain day-to-day risk parameter operations across Aave V3 and V4.
* [SVR Support](https://dashboard.llamarisk.com/protocols/aave/svr): Expand SVR analytics to support upcoming deployments on Avalanche, Polygon, and BNB Chain.
* **LlamaGuard PT Support**: Expand the LlamaGuard PT risk oracle to Aave PT markets on other networks.
* **RWA Assessments**: Continue due diligence for new assets including tokenized stocks and provide ongoing risk support across the Horizon RWA pipeline.

We welcome community feedback and suggestions. Please share any questions, ideas, or areas where you would like the LlamaRisk team to focus more.
