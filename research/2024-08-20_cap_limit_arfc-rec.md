# Summary

- LlamaRisk supports the proposal to increase supply cap preferences to 90% for Liquid Staking Tokens (LSTs) and Liquid Reward Tokens (LRTs) across all Aave markets.
- Market analysis:
  - The Base market is significantly affected, with the weETH supply cap nearing 95% of the total supply. Approximately 68% of the $82 million in borrows is concentrated in ETH-correlated assets, primarily due to extensive leverage looping between ETH and LSTs. A single borrower holds roughly 40% of the weETH supply.
  - In the Scroll market, the wstETH supply cap stands at 71%, with 80% of the $108 million in borrows focused on ETH-correlated assets. Of this amount, $72 million is in the ETH e-Mode, indicating a similar leverage looping strategy.
  - The Polygon market exhibits greater diversification, with wstETH at 70% of the total supply. Only 25% of borrows are in ETH-correlated assets, and ETH/LST leverage looping accounts for just 10% of the activity.
- Liquidation risks are considered manageable due to using CAPO price oracles, which limit the impact on ETH-correlated borrow positions. Liquidators are incentivized to transfer liquidity from the Ethereum mainnet to L2 chains due to the potential for high liquidation bonuses and attractive LP yields in markets with thin liquidity.
- Past liquidation events, potential discrepancies between supply and borrowing rates, and the ability to transfer liquidity across networks may introduce additional challenges. Each increase in the supply cap preference should be carefully evaluated based on the specific liquidity and market conditions.

LlamaRisk intends to conduct further research on liquidity requirements and liquidator response times in L2 markets to propose proactive measures to mitigate risks and support smaller Aave markets' confident and sustainable growth.

[details="Detail research below"]

## Introduction

Given this proposal's sensitive and risk-related nature, we aim to thoroughly assess the potential risks associated with increasing the cap preferences to 90% of the total supply for Liquid Staking Tokens (LSTs) and Liquid Reward Tokens (LRTs).

It is evident that on certain smaller chains where Aave markets operate, the Aave protocol has established itself as the leading platform. It attracts demand and, consequently, newly bridged assets as these supply caps are expanded. As a result, Aave is driving the growth of its new markets and contributing to the overall growth of asset supplies on these networks.

However, it is crucial to comprehend the circulation patterns of these assets, the nature of the borrow positions opened using such collateral, and the overall health of these positions. Furthermore, in the event of liquidations of an asset whose supply is heavily concentrated on Aave, the constrained on-chain liquidity necessitates robust bridging capabilities; hence, a thorough evaluation is required.

## High supply assets & markets

To better understand the relevance of the supply cap problem, we have inspected current LST and LRT supply caps about their on-chain supply for different Aave markets. These are the findings:

- weETH on Base, the supply cap is already at ~95% of all supply.
- wstETH on Scroll market is at 71% of the supply.
- wstETH on Polygon is at 70% of total supply
- as for Ethereum market, weETH is at 50% of total supply.
- All other LST and LRT assets on different markets are still far from the supply cap preference limit of 75%.

Therefore, this supply cap preference increase only concerns Base, Scroll, and Polygon Aave V3 markets. The assets of interest are weETH and wstETH.

## Borrow positions

### Scroll market

As for the Aave Scroll market, it is heavily focused on ETH-correlated assets and USDC. Consequently, 80% of the $108M borrows are in ETH-correlated assets.

![image|744x432](upload://jFqpgiqLRguEeFC6XNC7lN3UfkC.png)
Source: [ChaosLabs Aave Dashboard](https://community.chaoslabs.xyz/aave/risk/markets/Scroll/overview)

$72M worth of borrow positions are opened in ETH correlated e-Mode. Therefore, this market's primary use case is ETH/LST leverage looping.

![image|1551x162](upload://v7DDt0HVplqfD72IqjP3WYoWAVS.png)
Source: [ChaosLabs Aave Dashboard](https://community.chaoslabs.xyz/aave/risk/markets/Scroll/e-mode)

### Base market

Aave Base market possesses similar features, containing ETH-correlated assets as well as USDC and USDbC. Slightly less, 68% of $82M borrows are in ETH-correlated assets. Almost all of the ETH correlated borrow positions are in the corresponding e-Mode. Therefore, it contains the same ETH/LST leverage looping use case. 

Moreover, the largest borrower, who also uses this market for the same use case, supplies more than half of the total weETH supply. It accounts for ~40% of the total weETH supply on the Base network.

![image|1062x610](upload://wZAQCrcirt7C5ACY43jMCFhPYkq.png)
Source: [ChaosLabs Aave Dashboard](https://community.chaoslabs.xyz/aave/risk/markets/Base/overview)

### Polygon market

The Aave Polygon market contains more diverse asset types, where ETH-correlated assets only make up 25% of total supplies and borrow. Consequently, borrow positions are also more varied, with ETH correlated looping representing a mere 10% of the market's activity. 

![image|1058x616](upload://rNr7Qpt04DfqdqsFWtvPc0GJsL9.png)
Source: [ChaosLabs Aave Dashboard](https://community.chaoslabs.xyz/aave/risk/markets/Polygon/overview)

It cannot be concluded that ETH/LST leverage looping is the main use case for this market, and the wstETH supply on this market is slowly approaching the supply cap preference limit for other reasons.

## Liquidation Risks

While many of the largest borrow positions are exposed to the looping and are of low health (due to e-Mode), CAPO price oracles limit the risk of liquidating ETH-correlated borrow positions. 

Moreover, if the liquidations are bound to happen, the liquidators would be highly incentivized (due to the liquidation bonus) to bridge the LST/LRT liquidity from the Ethereum mainnet to these L2 chains and be able to perform the liquidations. Also, thin secondary market liquidity on these networks would offer high LP yields for such assets.

Nonetheless, it is important to dynamically monitor the overall health of the positions, as in addition to LST/LRT price deviations, a mismatch of supply and borrow rates for the looping users could also cause unexpected liquidations. It also needs to be considered that liquidators may not be able to instantly move liquidity from other, more liquid networks into the L2s.

The aggregated risk profile of the markets would not change drastically if the community preference for supply cap limits is lifted to 90% of the total LST/LRT supply. However, each supply cap raise requires an individual review covering specific liquidity and market conditions.

## Next steps

LlamaRisk will further research this subject to evaluate the liquidity and liquidators' needs in discussed L2 markets, understand how quickly the liquidity can be moved, and propose proactive measures to limit the discussed risks. This will help to scale the smaller Aave markets with higher confidence.

[/details]
