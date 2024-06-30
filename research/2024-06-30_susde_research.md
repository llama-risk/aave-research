# Additional notes on Ethena and sUSDe

LlamaRisk has recently published an [Asset Risk Assessment of Ethena's USDe/sUSDe](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde) and [specific considerations](https://governance.aave.com/t/arfc-onboard-usde-to-aave-v3-on-ethereum/17690/3?u=llamarisk) for Aave. Complementing the insights provided by BGD Labs, we have conducted further research on Ethena's reserve fund depletion, which raises concerns about the protocol's ability to maintain stability during periods of market stress. This analysis and an update on the sUSDe liquidity provision are provided to help inform the DAO about risks involving recently onboarded sUSDe and guide future parameter changes.

## Summary

- Our reserve fund decay simulations, detailed in this report, indicate that current reserves are inadequate, with a moderate risk of depletion under adverse conditions. Our research considers scenarios such as sustained negative funding rates, devaluation of insurance fund's LP positions in case of a USDe depeg, and losses from forced unwinding at higher slippage during volatile markets.
- The primary risk is persistent funding rates of -50% or worse, occurring only 2.5% of the time in historical data. Adding BTC perpetuals, which have shown fewer severe negative rates than ETH, helps mitigate this risk. However, the current insurance fund remains inadequate for worst-case scenarios.
-   The liquidity situation of sUSDe has been deteriorating, and it is currently trading at a discount on the secondary market compared to its exchange rate. USDe and sUSDe liquidity sustainability is questionable and primarily driven by Ethena incentive programs. Cessation of these incentives, as seen with sUSDe, could significantly reduce liquidity. This may also affect GHO, as the largest portion of its liquidity resides in the Curve GHO/USDe liquidity pool.
-   Governance and transparency concerns persist. Despite Ethena's 2024 roadmap and ENA tokenomics updates, the promised governance mechanisms still need to be implemented. Since our initial assessment, there has been no significant progress in establishing active community governance. The lack of a functioning governance forum and the absence of ENA token holder voting capabilities raise questions about decentralized decision-making and protocol management
-   While Ethena holds backing assets with reputable custodians and adheres to various licensing requirements, vigilance is necessary regarding MiCA license implications and regulatory ambiguity around sUSDe.
-   The off-chain and non-transparent management of USDe collateralization raises significant concerns. The code and structure governing this critical aspect of the protocol have never been published. As a result, Ethena's overall risk profile is heavily influenced by its internal systems, collateral management practices, and interactions with centralized exchanges, making it challenging for users and auditors to assess the protocol's risk factors fully.
-   Centralization risks persist. A hack on a major integrated exchange like Binance could compromise user assets, disrupt USDe liquidity, and undermine confidence in the stablecoin. The reliance on a Trusted Party also introduces a potential point of failure or vulnerability.

## Insurance Fund

Chaos Labs conducted a backtest from January 2021 to November 2023 in their [report](https://chaoslabs.xyz/resources/chaos_Labs_ethena_perpetual_assessment_risk_report.pdf) on perpetual futures liquidity and funding rates. They found a maximum collateral drawdown of 4.3% during negative perpetual funding rates in the September 2022 Ethereum merge. Based on this, their initial recommendation in November 2023, just before Ethena went live and was initially supposed to be backed by ETH perpetual only, was for:

>"An initial $33m insurance fund to ensure full coverage in all conditions as it grows to $1bn supply" (p. 42).

Further discussion with Chaos Labs confirmed that this report would need to be updated to reflect changes in both market maturity and Ethena protocol scale. However, the $44m covering over $3.5b USDe is vastly inadequate, a claim substantiated by the simulation of various adverse scenarios later in this research.

The fund's composition may exacerbate this issue, with a significant allocation to USDe/USDT liquidity provision on Uniswap V3 and sDAI deposits. This endogenous backing creates potential circular dependencies that could compromise the fund's effective value in a de-peg scenario. Additional simulations exploring various scenarios of reserve fund depletion have been conducted to examine these concerns further.

## Deteriorating sUSDe liquidity

The supply of sUSDe has grown 5x since the beginning of May 2024. However, the liquidity situation has deteriorated both in absolute and supply-relative terms. The liquidity-to-supply ratio is below 1%, and total sUSDe liquidity is below 10m - the lowest since April 2024.

![image|2000x745](upload://ts97reri8uCPppwg7GXTQZF2Qqq.png)
Source: [Dune dashboard](https://dune.com/queries/3824232/6432357)

While the exact cause of this trend cannot be determined, several potential factors may have contributed to the current situation:

- Ethena protocol no longer incentivizes sUSDe liquidity provision via the Sats program, contrary to USDe liquidity.
- Much of sUSDe (~1b out of 1.5b) resides in Morpho and Pendle protocols, partially due to the [Sats program incentives](https://app.ethena.fi/liquidity).
- A sharp increase in sUSDe supply has diluted the yield distributed to sUSDe holders. 

This situation warrants ongoing vigilance and analysis. The liquidity constraints may have already influenced sUSDe pricing in secondary markets, where it has begun trading at a marginal discount, as illustrated in the following chart:

![image|2000x990](upload://mEMeE6esq2JDN5zXG6B9aizCKTA.png)
Source: [Dune dashboard](https://dune.com/queries/3878521/6523232)

## Incentive program

The [ongoing Sats campaign](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde#:~:text=May%209th%2C%202024-,Sats%20Campaign,-Ethena%27s%20Season%202), part of Ethena's Season 2 initiatives, incentivizes a wide array of DeFi activities. These include ENA/USDe locking, liquidity provisioning, Pendle locks, depositing and borrowing on money markets, and Layer 2 activities. However, it is notable that USDe holders are not encouraged to stake for sUSDe during the current campaign.

While the diverse DeFi integrations provide numerous opportunities for token holders to farm points, they are not immune to liquidity risk. This vulnerability is partly due to different withdrawal limitations imposed by protocols that are part of the incentives program and their specific redemption mechanics. Many USDe and sUSDe holders leverage their positions through high loan-to-value (LTV) lending pools. Consequently, even a minor de-pegging event could trigger a major liquidation cascade. Without sufficient liquidity to absorb the selling pressure, both assets could further de-peg, potentially leading to a downward spiral.

## Update Ethena 2024 roadmap

A recently published [update to ENA tokenomics](https://mirror.xyz/0xF99d0E4E3435cc9C9868D1C6274DfaB3e2721341/2U7m0_wfns4lotPJZV7nCkpB908sUmqqhrR3sWdtknw) reveals implementations aligned with the [Ethena 2024 roadmap](https://mirror.xyz/0x29a99F7Fe080F72223dAd48D5E1E86670a984326/odrjQynMr3PrtRhCzHa2k7tcdNIpibJLyRe7yXY944Q). Cross-chain transfer of USDe and sUSDe is planning to be facilitated through a LayerZero DVN network, secured by staked ENA. Starting June 26th, users can restake on Symbiotic, expanding options beyond [Ethena.fi](https://app.ethena.fi/liquidity) and [Pendle Finance](https://app.pendle.finance/trade/points/0x9c73879f795cefa1d5239de08d1b6aba2d2d1434?chain=ethereum). ENA and sUSDe stakers on Symbiotic are planning to receive:

- Highest Ethena multiplier (30x per ENA per day)
- Symbiotic points
- Mellow points
- Potential future LayerZero RFP allocations

Specific point calculation details are yet to be disclosed.

Ethena Chain also plans to use USDe as a gas token, with restaked ENA enhancing security for various DeFi applications and infrastructure solutions. This plan will leverage Symbiotic's permissionless, asset-agnostic restaking layer, attracting ERC-20 tokens representing staked assets or liquidity positions from different blockchains.

As the USDe ecosystem grows, ENA's utility as a security asset is expected to increase. Users receiving ENA via airdrop (e.g., from the portion of Shard Campaign airdrop subject to vesting conditions) are now required to lock a minimum of 50% of the claimable ENA from the distribution received into Ethena locking, PT-ENA on Pendle, or Symbiotic Restaking, promoting long-term user alignment.

## Legal & regulatory aspect

As part of our research, we have examined legal, regulatory, and custody aspects. Our findings are as follows:

- Ethena's backing assets are held with reputable custodians. Each of them adheres to different licensing or registration requirements as discussed [here](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde#:~:text=participation%20is%20facilitated.-,Custody%20Risk,-Ethena%27s%20USDe%20backing).
- [Trusted Third-Party Agreements](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde#:~:text=for%20derivatives%20trades.-,Trusted%20Third%2DParty%20Agreements,-Ethena%20has%20entered) create a reliable system for transaction management, safeguarding MPC (multi-party computation) signatory partitions and disaster recoveries.
- Collateral assets are made transparent by providing [custodian legal attestations](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde#:~:text=Proof%20of%20Collateral%20Assets). Ethena has also expressed its intention to later publish an on-chain proof-of-reserves for improved transparency.
- An entity, Ethena Italia S.r.l., that operates the website www.ethena.fi holds a VASP (Virtual Asset Service Provider) registration issued by [Italian Authorities](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde#:~:text=Regulatory%20stances%20towards%20Ethena), affirming its status as a recognized service provider within the Italian jurisdiction.
- Vigilance regarding the implications of [MiCA license for Ethena](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde#:~:text=Assessing%20the%20potential%20impact%20of%20evolving%20regulations%20on%20USDe%27s%20usability%20as%20collateral) is advised. 
- sUSDe potentially falls out from the scope of the current laws and regulations in the EU, as there is no clear qualification of liquid staking tokens as discussed [here](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde#:~:text=Additional%20considerations%20for%20sUSDe).
- Season 2 of the incentives program is ongoing; however, [governance model](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde#:~:text=monitoring%20and%20measurement.-,Governance%20Structure,-As%20of%20the) around ENA has not progressed since the token airdrop.

## Reserve fund decay simulations

To assess the robustness of Ethena's reserve fund under various market conditions, we conducted a series of simulations modeling the fund's behavior during periods of sustained market stress. These simulations test the fund's resilience and identify potential vulnerabilities in the protocol's risk management strategy.

Our approach uses simplified constant rates to model escalating market stress scenarios, focusing on persistent negative funding rates of 5%, 10%, 25%, 50%, and 100% annualized APR. While these scenarios assume independent conditions for clarity of analysis, it's important to note that real market dynamics often involve correlated factors that could compound reserve fund decay. This methodology allows us to isolate and examine individual stress factors, though we acknowledge that market conditions are typically more complex and interrelated.

The following simulations provide insights into potential fund depletion rates under various adverse market conditions, offering a foundation for assessing the current reserve fund structure and size adequacy.

### Summary of scenarios

|#| Description |
|:----|:---- |
|1| Base case - sustained negative funding rates |
|2| Base case combined with USDe depegging, leading to devaluation of the insurance fund's Uniswap V3 liquidity positions |
|3| Base case combined with unwinding of Ethena's position during the volatile market and associated slippage losses|
|4| Scenario 2 & 3 combined|

### Funding rate assumptions

The historical funding rate data covers the four major CEXs where Ethena holds perpetual positions: Binance, Bybit, OKX, and Deribit.

![image|1535x301](upload://xSkxQm7qskYVVcBGljTxGjxfsRo.png)
Source: [Ethena Dashboard](https://app.ethena.fi/dashboards/positions), 29th of June, 2024.

As Ethena uses both BTC and ETH Perpetual Contracts, the funding rates for both assets are analyzed separately. Both contract pairs are denominated in USDT (the most liquid pairs). Historical data spans from October 2019 to May 2024.

![image|1211x622](upload://p3SEwp3F5WQ8WBCrY0GpDaUccaq.png)

![image|1199x627](upload://yLRbPbZb0MMfUkuzX7i4CoU7R3S.png)

As of late June 2024, the supply of USDe is 3.6B, and the current level of the reserve fund is $45M, comprising USDT, sDAI in a Maker Vault, and positions in a Uniswap V3 USDT/USDe pool.

![image|764x98](upload://ppkcF4FAKleI9A6xjT7Kyu22JJN.png)
Source: [Debank](https://debank.com/profile/0x2B5AB59163a6e93b4486f6055D33CA4a115Dd4D5), 29th of June, 2024.

### Scenario 1

**Simulated Situation:** Sustained negative funding rates, neutral market reaction (no USDe depeg), and reserve fund LP position unaffected.

![image|856x568](upload://c4h7wYAurcBlk13d9jBjMbiT8f0.png)

**Historical analysis:** We assume that negative periods end once a single day has positive funding rates. In reality, there could be two non-overlapping negative periods, one after another, leading to a continued depletion of the reserve fund. For ETH, the evolution of past funding rates suggests one historical period where funding rates were negative for long enough to have drained the reserve fund. 

| Exchange | Start | End | Duration, days | Mean Annualized Funding Rate |
| :--- | :--- | :--- | :--- | :--- |
| Bybit | 2022-09-06 | 2022-09-16 | 10 | -0.46 |
| Binance| 2022-09-03 | 2022-09-16 | 13 | -0.38 |
| OKX | 2022-08-23 | 2022-09-16 | 24 | -0.27 |

No such periods were observed for BTC perpetual.

**Likelihood of depletion:** 

![image|1288x492, 50%](upload://uriYFr7ky46vmjigM6FATFgwu9i.png)

It can be observed that the probability of depletion is especially elevated (0.23) whenever a negative funding rate period of $\leq -50\%$ happens. Historically, $2.5\%$ of all negative funding rate periods had $\overline{F}\leq -50\%$.

Please refer to the appendix for a detailed explanation of the methodology used in these calculations.


### Scenario 2

**Situation:** Sustained negative funding rates, market reaction is negative (USDe depegs), and therefore, liquidity of the reserve fund gets affected. 

**Assumptions:** Uniswap V3 pool positions are assumed to end up holding only USDe and are discounted accordingly. We value sDAI at par, as only a marginal amount of DAI is backed by USDe. Therefore, a de-peg of USDe would not significantly impact the value of sDAI. During the USDC (and DAI) de-peg event, the most actively traded DEX, Curve 3pool, showed an exchange rate of 1.21 for USDT/USDC (and similarly for USDT/DAI) when only 4% of USDT remained in the pool. Based on this historical precedent, we assume that the Uniswap V3 USDT/USDe pool would exhibit similar behavior in the case of a USDe de-peg.

![image|856x568](upload://8s00Szao3Wg2tr07Df74rWMrZVr.png)

The graph above plots a 20% discount on the Uniswap V3 LP position. The time until full depletion is 5% shorter than in scenario 1.

**Historical analysis:** In this scenario, when a 20% discount is applied, one additional instance of reserve fund depletion would have occurred over 21 days in July 2021 on ETH perpetual.

| Exchange | Start | End | Duration, days | Mean Annualized Funding Rate |
| :--- | :--- | :--- | :--- | :--- |
| Bybit | 2022-09-06 | 2022-09-16 | 10 | -0.46 |
| Binance| 2022-09-03 | 2022-09-16 | 13 | -0.38 |
| OKX | 2022-08-23 | 2022-09-16 | 24 | -0.27 |
| Deribit | 2021-07-02 | 2021-07-23 | 21 | -0.19 |

**Likelihood of depletion:** Due to a lower liquid value of the reserve fund, the probability of a full depletion increases, although marginally:

![image|1284x480, 50%](upload://jZSn36N9S8CMQnOpYW5tdtndltW.png)

### Scenario 3

**Situation:** Funding rates are negative, market volatility persists, and users begin redeeming USDe for collateral, forcing Ethena to close perpetual positions and incur slippage losses.

**Assumptions:** Redemptions begin on the first day of a negative funding rate period. USDe does not depeg in this scenario (to isolate the impact of slippage). USDe redemptions are limited to 2M per block and by available contract collateral. Ethena holds approximately $30M of collateral in the contract. Ethena can slow down collateral swaps by custodians to mitigate the impact of slippage.

However, Ethena can also completely pause redeeming on the contract level. It could cause market panic and, in turn, a depeg of USDe on secondary markets. Therefore, such behavior is not tested in any scenario.

Using Chaos Labs' historical slippage data, we focus on the 99th percentile (extreme market conditions) for trades up to 10,000 ETH, which implies a 0.5% slippage.

![image|662x254, 50%](upload://tZYxO1HuwK2nuh0DNb5CTgPq8Yt.png)
Historical slippage in basis points, Source: [Chaos Labs](https://chaoslabs.xyz/resources/chaos_Labs_ethena_perpetual_assessment_risk_report.pdf)

A 50% USDe redemption level is tested, the maximum possible given the 1.5B USDe currently staked with a seven-day cooldown. At this 50% USDe redemption, slippage would amount to $9.14M, reducing the reserve fund by 20%.

![image|856x568](upload://61RqSdOMkaX0a283uxYxzkMCoJT.png)

**Likelihood of depletion:** A marginal increase in the probability of full depletion is observed compared to scenario 2.

![image|1290x474, 50%](upload://tfI5ynnOVW3EMEQrSM45iG5aLhg.png)

### Scenario 4

**Situation:** Scenarios 2 and 3 combined. This would mean the LP position gets discounted and USDe redeemed, amplifying the drawdown effects.

The results indicate that even with up to 50% redeems and a discount of 20% on assets in the reserve fund, Ethena would have at least four days before the reserve fund would be emptied.

![image|856x568](upload://e6sGFL1s7jMs8Vn7U7wO5AnMRvP.png)

**Likelihood of depletion:** This combined scenario further amplifies The likelihood of full depletion.

![image|1282x472, 50%](upload://otQh7dKH35IY4hNGvzSP9cCa7ds.png)

### Conclusion

The simulations underscore the critical importance of maintaining a well-capitalized reserve fund for Ethena, particularly as the market cap of USDe grows. Historical data shows insufficient reserves could have posed significant risks to the protocol's financial stability.

Ethena's diversification into BTC perpetual alongside ETH perpetual, at an approximate 1:1 ratio, is a positive development. Since BTC perpetuals historically exhibit less severe negative funding rates than ETH, this strategy should help mitigate potential negative impacts. Our simulations, which assumed all positions in ETH perpetual, thus represent a worst-case scenario.

In light of these findings, we prompt Ethena to reevaluate its insurance fund capitalization. To illustrate this, we simulated a reserve fund at the original recommended ratio of 33M per 1B market cap. Increasing the reserve to $115M would significantly enhance the protocol's safety margins.

The following is how the safety would increase in terms of measures of depletion under scenario four if the reserve would increase to $115M:

![image|856x568](upload://lkj6EDz38JVRx8RMOIULl2LJhTl.png)

The threshold until full depletion would increase by 2.9x, and the likelihood of full depletion would scale back as follows:

![image|1276x474, 50%](upload://ipd9Xlj1OU0qN8RYHE9S0eFz9mv.png)

No historical occurrences indicate full depletion if the reserve fund is at the recommended level.

While we do not provide a firm recommendation for a specific reserve fund size, it's clear that any significant increase in the insurance fund will strengthen our confidence in Ethena's resilience to adverse market conditions. As the protocol scales, continual assessment and adjustment of the reserve fund size will be necessary to ensure it remains commensurate with the increasing market cap of USDe and evolving market conditions.

## Appendix

### Probability of Depletion Methodology

The severity of negative funding rate periods varies significantly. To account for this variability, we focus on four mean negative funding rate levels: -5%, -10%, -25%, -50% and -100%. A negative funding rate period is categorized into the -50% level if its mean funding rate $\overline{F}$ is less than or equal to -50%. Given the occurrence of a negative period, we can statistically estimate the probabilities of the severity of a negative funding rate:

![image|342x96, 50%](upload://mdFm3eXcO8Ky1Nsnc0Q4YogKbAp.png)

Where:
![image|458x66, 50%](upload://2tOQ7wibQLwXQmyUzeiCFbxUS6z.png)

Each observed negative funding rate period has a duration measured in hours. The distribution of these durations closely approximates an exponential curve.

![image|724x496](upload://zBm5vudXCPQ485ZczKPBX2pKcnp.png)

Source: Historical data from October 2019 to May 2024 (Binance, Bybit, OKX, and Deribit)

Statistically, the duration follows an exponential distribution:

![image|412x290, 50%](upload://o8WJLzFBeVTFzPdQJPtyv7MY2FB.png)

Our simulation demonstrates the time required to deplete the reserve under various severities of negative funding rates. We define this as the threshold of depletion:

![image|738x70, 50%](upload://yssfQK4BmAwMmgoGjr05Cnbjod3.png)

Given the mean lengths of negative funding rate periods, we can estimate the probability that a negative period is of sufficient duration to deplete the reserve fund, contingent on the severity of the negative funding rate period:

![image|922x436, 50%](upload://hxMhY7rV7TUFYtQEEZIxeUGtJkB.png)
