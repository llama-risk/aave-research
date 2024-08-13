# Summary

LlamaRisk supports deploying a new Ethena Aave v3 instance on Ethereum, with sUSDe and USDe as collateral-only assets, USDC and FRAX as borrowable assets, and a GHO facilitator. We've conducted due diligence on these assets ([PYUSD - Apr 2024](https://www.llamarisk.com/research/pegkeeper-onboarding-pyusd), [FRAX/sFRAX - Dec 2023](https://www.llamarisk.com/research/collateral-risk-sfrax)) and find that the initial parameters proposed are suitable. Bundling a GHO facilitator with this market represents a good opportunity, allowing USDe and sUSDe to become new collateral types. We propose safe initial mint caps of 4M GHO alongside parameters for DAO consideration, jointly discussed with @ChaosLabs.

We note that further assets, such as DAI and USDT, could be introduced and more exotic collateral types, such as Ethena's Pendle PT tokens and rsUSDe. These could alter this instance's risk profile, and consideration for onboarding will warrant a thorough examination.

## Motivation

The proposed dedicated instance for Ethena's sUSDe and USDe aims to enhance leveraged borrowing efficiency within the Aave ecosystem. Currently, both assets are in *Isolation Mode* on mainnet, limiting their utility while mitigating potential risks to the protocol. This dedicated instance allows for more aggressive parameters by isolating potential risks associated with these assets.

Moreover, introducing a GHO facilitator within this instance and including USDe and sUSDe as new collateral types for GHO will contribute to the expansion and diversification of the GHO stablecoin ecosystem.

## Current State of Ethena

After growing to $3.6B of TVL, Ethena protocol has slightly declined this past month. The TVL at the time of writing is now $3.1B, which is rational given current market conditions and associated lower funding rates. In addition to BTC and ETH perpetuals, Ethena introduced SOL as a perpetual futures trading asset. This will help further diversify the risk and increase scaling opportunities regarding open interest.

Ethena has also recently introduced an initial phase of governance, onboarding risk providers to govern different risk parameters, such as reserve fund capitalization, liquid redemption buffer, take rates, collateral allocation between different CEX, etc. LlamaRisk is also part of this risk council and has covered different pain points of the protocol in a dedicated [Ethena research](https://www.llamarisk.com/research/asset-risk-usde-addendum1). The council will be working on these issues to ensure the stability and lower risk of the protocol.

The [ongoing Sats campaign](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde#:~:text=May%209th%2C%202024-,Sats%20Campaign,-Ethena%27s%20Season%202), part of Ethena's Season 2 initiatives, incentivizes a wide array of DeFi activities. These include ENA/USDe locking, liquidity provisioning, Pendle locks, depositing and borrowing on money markets (among which depositing USDe on Aave V3), and Layer 2 activities. However, it is notable that USDe holders are not encouraged to stake for sUSDe or provide sUSDe liquidity during the current campaign.

### USDe liquidity

The main liquidity for USDe resides in Curve and Uniswap V3 Liquidity Pools. The overall size of the liquidity is $245M with a USDe portion of ~$100M (3.3% of TVL). USDe is mostly paired with other stablecoins like FRAX, USDC, USDT, and GHO. The liquidity has remained stable, with minor drawdowns during adverse market conditions (e.g., market stress on August 5th, 2024). 

![image|1679x598, 75%](upload://3K0PveDJWUPvuYJAC11tUq1avPN.png)
Source: USDe liquidity on DEX. Source: [Dune Analytics](https://dune.com/queries/3816028/6417876), August 13th, 2024

### sUSDe liquidity

1.4B sUSDe is outstanding, representing approximately 45% of the total USDe supply. However, the liquidity situation for sUSDe is significantly worse than that of USDe. The liquidity-to-supply ratio for sUSDe is below 1%, with total sUSDe liquidity remaining under 10M for an extended period - the lowest level since April 2024.

![image|730x308, 100%](upload://44rOJXmV40fl1ImwRXgsSSbG0yl.png)
Source: sUSDe liquidity on DEX. Source: [Dune Analytics](https://dune.com/queries/3824232/6432357), August 13th, 2024

It's important to note that sUSDe can be unstaked with a current cooldown period of 7 days. This feature reduces the need for immediate liquidity for users who wait through this period, potentially earning additional yield due to sUSDe trading at a discount. Historically, this discount has been modest (maximum of -400 bps), but vigilance is required for potential Ethena scenarios, as capped oracles would be used. If sUSDe begins trading at larger discounts, there's a risk that discounted sUSDe could be deposited as collateral at a par value while other stablecoins are borrowed as exit liquidity.

![image|1222x594, 75%](upload://em3deKq3I3pvoQIZAB4PQUFQESf.png)
Source: Historical sUSDe discount. Source: [Dune Analytics](https://dune.com/queries/3878521/6523232), August 13th, 2024

Given that the points program incentivizes the USDe liquidity provision while sUSDe liquidity does not, this indicates a problem of non-sustainable liquidity. Therefore, there remains a risk that liquidity could also thin out for USDe in case the points 
program is terminated.

## Current state of GHO

After an extended conservative growth period, GHO has entered a more aggressive scaling phase. It is a great opportunity to open up new collateral assets for GHO, and the isolated Ethena instance would facilitate that. USDe and sUSDe would be onboarded as new collateral types since they are isolated assets on the main market, and therefore, GHO is not borrowable using them.

![image|1029x680](upload://rr5nqymQEoAmZS2IEXAevEypgQa.png)

Source: [Chaos Labs GHO Dashboard](https://community.chaoslabs.xyz/aave/risk/GHO/risk), August 11th, 2024

It's important to recognize that 25% of all GHO liquidity currently resides in the USDe/GHO pair on Curve, which remains substantial while down from a previous high of around 50%. Although the existing USDe/GHO pairing has not posed significant risks thus far, introducing additional dependencies between GHO and USDe warrants attention. In particular, the potential for unintended consequences, such as those arising from a USDe de-peg, should be monitored to ensure the continued stability of GHO.

## Aave V3 Specific Parameters

We discussed and aligned unified parameter recommendations with @ChaosLabs; they will be provided shortly.

We recommend implementing stablecoins e-mode (90% LTV/93% LT) for this instance. Supply caps for USDe and sUSDe have been chosen conservatively according to liquidity, redeemability, and the fact that Aave will use the internal rate + CAPO.

For the GHO facilitator, we recommend a starting cap of 4M GHO and a borrow rate set 0.5 percentage points lower than the main market GHO facilitator to incentivize borrowing.
