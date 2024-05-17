## Summary

LlamaRisk is supportive of @ChaosLabs’s recommendation to onboard tBTC on Ethereum mainnet. We've prepared an [updated report](https://hackmd.io/@LlamaRisk/tBTC-addendum-1) referencing LlamaRisk's initial assessment of tBTC published on November 1st, 2023. We are also of the opinion that tBTC does not have sufficient liquidity to be onboarded on Optimism and Arbitrum networks.

## Asset rating
In updating our assessment of tBTC, we are revising our risk rating. Based on the risks identified for each category, the following chart summarizes a risk rating for tBTC as collateral. The rating for each category is ranked from excellent, good, ok, and poor.

* We rank tBTC **ok on liquidity** (unchanged) since it remains a minor tokenized BTC asset. Its liquidity provision on DEX appears adequate, although listing on CEX (Kraken) needs more volume. The introduction of the Wormhole bridge has increased tBTC's availability across multiple chains, but Curve still holds the majority of liquidity and volume, albeit to a lesser extent since the initial analysis.
* We rank tBTC **good in volatility** (unchanged) due to the permissionless ease of mints/redemptions that facilitate arbitrage, with a small fee on each action. tBTC has exhibited strong peg strength since redemptions were activated in July 2023.
* We rank tBTC **ok in smart contracts** (unchanged) since there has been no change to its system architecture since deployment. The $500,000 ImmuneFi bug bounty program remains.
* We rank tBTC **good in dependencies** as it has recently added a Chainlink oracle, reducing reliance on Curve EMA and permitting further DeFi integration. Significant off-chain processes that introduce complexity to the system remain a risk vector.
*We rank tBTC **good in decentralization** (unchanged) for prioritizing permissionless access, a decentralized bridge network, and a reasonably convincing pathway to on-chain governance.
* We rank tBTC **ok in legal** (unchanged) as the legal structure(s) are domiciled in a prominent jurisdiction, while no enforcement actions against Threshold are evident. Clarifying the legal status of cross-chain bridges and fortifying the protocol's defenses could be better implemented.

### Specific Consideration for Ethereum mainnet

Our previous assessment reviewed tBTC favorably, with moderate concerns about liquidity provisions and the lack of a dependable oracle. Considering liquidity provisions, holder distribution, and DeFi integration, tBTC is suitable for listing on Aave V3. The newly launched Chainlink price feed addresses the primary concern raised in the previous assessment by providing a dependable Oracle source.

The Ethereum mainnet remains the primary network for tBTC, holding the most significant share of the token's activity, despite the Wormhole bridge expanding tBTC's availability across multiple chains.

tBTC's liquidity on Ethereum is sufficient for listing on Aave V3, with a diverse set of liquidity providers. The token's volatility remains low due to the permissionless nature of mints and redemptions, which facilitates efficient arbitrage.

Although risks associated with the significant off-chain processes in the tBTC system persist, the overall risk profile has improved since the initial analysis. The Chainlink oracle, ongoing bug bounty program, and strong peg strength since July 2023 contribute to a favorable outlook for tBTC on the Ethereum mainnet.

In conclusion, we recommend listing tBTC on Aave V3 for the Ethereum mainnet, with appropriate risk parameters based on the token's liquidity, volatility, and overall market conditions.

### Specific Consideration for Optimism and Arbitrum

Despite the recent growth in tBTC availability across multiple chains through the Wormhole integration, liquidity on Optimism and Arbitrum still needs to be increased to recommend onboarding. The main liquidity pool (Curve) holds significantly less TVL than Ethereum mainnet, with an important price impact for trades as small as five tBTC.

While tBTC has seen some volume on L2s, the overall liquidity profile is unimpressive and does not show strengthening growth trends. Positive trends in liquidity depth and utilization are necessary to minimize the creation of bad debt due to missed liquidations.

We do not recommend onboarding tBTC on Aave V3 for Optimism and Arbitrum networks.