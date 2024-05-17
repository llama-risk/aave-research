## Summary

LlamaRisk is supportive of @ChaosLabs's recommendation to onboard USDe in Isolation Mode. While we note several risk factors to consider and potential improvements from Ethena's side, we deemed that the parameters proposed above are prudent and in line with this asset risk profile. We invite Aave community members to go through our extensive [USDe asset risk assessment](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde) conducted over the last month, which highlights a number of risk factors associated with Ethena's USDe.

The primary risk USDe poses is the potential for collateral failure, given the heavy reliance on centralized components and the opaqueness of its basis trading operational procedures. Liquidity plays a critical role in maintaining collateral value and preventing mass liquidations. This risk is accentuated if Ethena encounters significant operational disruptions (e.g., CEX downtime), which could heavily impact the secondary market and precipitate cascading liquidations characterized by a swift depletion of USDe liquidity. Current liquidity levels are adequate. However, it is important to note that Ethena has yet to face an event requiring significant redemptions.

Ethena's insurance fund raises several concerns. Firstly, there is an absence of public guidelines delineating its intended use. Secondly, the fund's amount appears inadequate relative to the USDe supply and prior research based on historical funding rates. Furthermore, the fund's actual value cannot be considered at par due to partial backing by endogenous collateral, Uniswap V3 USDT LP, and, to a lesser extent, sDAI, which needs to be discounted.

In the context of Aave, listing USDe as a collateral asset introduces significant strategic opportunities for users, particularly through the potential to create stablecoin leverage loops. In isolated mode, the risk of collateral failure is confined to participants in individual markets accepting USDe as collateral as long as liquidation can be done promptly to avoid bad debt for the protocol.

## Key Risk Considerations

1. **Centralized Components and Failure Points**: Ethena's operations rely on centralized components, such as centralized exchanges, for critical operations. These components introduce additional failure points that are not readily auditable. Ethena's ability to manage collateral and maintain delta-neutral positions on various centralized exchanges is crucial for USDe's stability. Disruptions or failures in these off-chain systems could compromise USDe's stability.

2. **Concentration of collateral and effectiveness of delta-neutral hedging strategies**: High collateral concentration raises concerns about market depth and liquidity during volatile periods, potentially compromising delta-neutral hedging strategies, especially during market stress. If the markets used for hedging lack sufficient liquidity to absorb Ethena's trades without significant price impact, it could lead to ineffective hedging and increased risk for USDe. Perpetual futures used in Ethena's delta-neutral strategy are inherently leveraged. Reduced liquidity on centralized exchanges during market downturns could be problematic for Ethena when rebalancing positions. This does not constitute an immediate issue at Ethena's current scale but could change rapidly according to market conditions and Ethena's growth.  
![image|1012x289](upload://1Ha5IXgE08JjtClgh2hm621yztV.png)
Source: [Ethena](https://app.ethena.fi/dashboards/positions), May 16th, 2024

3. **Market liquidity**: The ratio of secondary market liquidity to total USDe supply is a concern for DeFi integrations such as Aave. The main liquidity venues, aside from whitelisted users capable of direct USDe redemption, remain Curve and Uniswap pools. Although secondary market USDe liquidity has generally grown since inception, a recent pullback has been observed:
![image|776x492](upload://eiX8X4Rdvc4ilJlMhBUjAzRvSzd.png)
Source: [Ethena RIsk Radar](https://defirisk.intotheblock.com/metrics/ethereum/ethena), May 16th, 2024

    USDe has significantly deeper liquidity across DEXes compared to sUSDe, which is also subject to a 7-day cooldown period when unstaking. Only whitelisted addresses (currently 20, most of which are market makers) undergoing KYC/AML checks can mint and redeem USDe directly. The newly listed USDe spot markets (BTC/USDe and ETH/USDe) on Bybit and the ability to use USDe as collateral to trade perpetual futures are noteworthy and improve its trading volume and liquidity.

4. **Insurance fund adequacy**: The insurance fund appears insufficient, given Ethena's scale of operations and potential risks. Previous [research conducted by Chaos Labs](https://chaoslabs.xyz/resources/chaos_Labs_ethena_perpetual_assessment_risk_report.pdf) suggests that the current insurance fund, standing around 1.7% of USDe supply, may be inadequate.

    As a significant portion of the fund is allocated to USDe/USDT liquidity provision on Uniswap V3 and deposits in sDAI, a yield-generating vault involving USDe, circular ties could compromise the fund's value in a de-peg scenario. The fund's true value must be discounted due to partial backing by endogenous collateral. It remains to be seen under what circumstances this fund may be used, as no guidelines have been disclosed.
![image|674x784](upload://vsYqRV7xbnkWm0HweL7hEQTyaZ1.png)
Source: [Zerion](https://app.zerion.io/0x2b5ab59163a6e93b4486f6055d33ca4a115dd4d5/overview), May 16th, 2024

5. **USDe liquidity relying on incentives**: USDe is not yield-bearing and mainly relies on incentives to retain appeal for users to provide liquidity. The current Sats Season 2 campaign is set to run until September 2024; it remains to be seen how Ethena intends to maintain liquidity levels after this time.

6. **Governance structure, token distribution, and limited public information**: The proposed governance functionalities are yet to be activated, with no active forum discussions or the ability for ENA holders to weigh in on protocol decisions. This contradicts ENA token rights attributions (e.g., governance power). However, the team mentioned that governance is set to launch in the coming days. Furthermore, more detailed public information about Ethena's operational procedures and mechanisms for interfacing with centralized exchanges and managing governance is needed.

7. **Legal and regulatory compliance**: Impending regulations like MiCAR in the E.U. could pose significant operational hurdles and introduce uncertainty. Ethena must navigate a complex and evolving regulatory landscape, which may require significant resources and adaptations to maintain compliance.