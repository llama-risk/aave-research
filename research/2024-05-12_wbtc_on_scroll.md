# Background - Aave on Scroll

To explore the possibility of adding WBTC Scroll to Aave, we will first provide some context and background information on Aave's current integration with the Scroll network. On January 9, an [ARCF proposal](https://governance.aave.com/t/arfc-aave-v3-deployment-on-scroll-mainnet/16126) was made to deploy Aave V3 on the Scroll mainnet. This proposal was officially approved and executed through [an on-chain vote](https://app.aave.com/governance/v3/proposal/?proposalId=20) on February 9. The Scroll implementation was instantiated with 3 markets: WETH, wsETH, and USDC. The markets were established with the following parameters:

|              Parameter             |     WETH |      USDC |     wstETH |
|:----------------------------------:|---------:|----------:|-----------:|
| Isolation Mode                     |    FALSE |      TRUE |       TRUE |
| Borrowable                         |  ENABLED |   ENABLED |    ENABLED |
| Collateral Enabled                 |     TRUE |      TRUE |       TRUE |
| Supply Cap                         |      240 | 1,000,000 |        130 |
| Borrow Cap                         |      200 |   900,000 |         45 |
| Debt Ceiling                       |    USD 0 |     USD 0 |      USD 0 |
| LTV                                |     75 % |      77 % |       75 % |
| LT                                 |     78 % |      80 % |       78 % |
| Liquidation Bonus                  |      6 % |       5 % |        7 % |
| Liquidation Protocol Fee           |     10 % |      10 % |       10 % |
| Reserve Factor                     |     15 % |      10 % |       15 % |
| Base Variable Borrow Rate          |      0 % |       0 % |        0 % |
| Variable Slope 1                   |    3.3 % |       6 % |        7 % |
| Variable Slope 2                   |      8 % |      60 % |      300 % |
| Uoptimal                           |     80 % |      90 % |       45 % |
| Stable Borrowing                   | DISABLED |  DISABLED |   DISABLED |
| Stable Slope1                      |    3.3 % |       6 % |        7 % |
| Stable Slope2                      |      8 % |      60 % |      300 % |
| Base Stable Rate Offset            |      2 % |       1 % |        2 % |
| Stable Rate Excess Offset          |      8 % |       8 % |        8 % |
| Optimal Stable To Total Debt Ratio |     20 % |      20 % |       20 % |
| Flashloanable                      |  ENABLED |   ENABLED |    ENABLED |
| Siloed Borrowing                   | DISABLED |  DISABLED |   DISABLED |
| Borrowable in Isolation            | DISABLED |   ENABLED |   DISABLED |
| Oracle                             |  [ETH/USD](https://scrollscan.com/address/0x6bF14CB0A831078629D993FDeBcB182b21A8774C)|  [USDC/USD](https://scrollscan.com/address/0x43d12Fb3AfCAd5347fA764EeAB105478337b7200) | [wstETH/USD](https://scrollscan.com/address/0xdb93e2712a8b36835078f8d28c70fcc95fd6d37c) |

On April 18, an Aave Improvement Proposal (AIP) was approved to [set the Liquidity Observation Labs wallet address](https://app.aave.com/governance/v3/proposal/?proposalId=79) (`0xC18F11735C6a1941431cCC5BcF13AF0a052A5022`) as the Scroll wstETH Emissions Manager. This change makes the Liquidity Observation Labs wallet the emission admin for the wstETH token on the Scroll network, in addition to the existing Ethereum, Base, Arbitrum, Optimism, Polygon, and Gnosis V3 markets, where it already serves as the emission admin.

As of May 11, USDC and ETH are the most prominent markets in total supplied and borrowed. Both have ~$5m supplied and ~$2-3m in borrows
![Screen Shot 2024-05-11 at 10.00.03 AM](https://hackmd.io/_uploads/rJimNm6MA.png)

# Scroll Bridge

ETH and tokens (including WBTC and the previously onboarded tokens) can be bridged between Ethereum and Scroll via the Scroll Bridge and an arbitrary messaging bridge. Bridging from L1->L2 involves a ~10-minute wait time, and bridging from L2->L1 involves a ~1-hour wait time. See the bidirectional flow logic below: 

![image](https://hackmd.io/_uploads/By6y07Tf0.png)
![image](https://hackmd.io/_uploads/HJoe0XpfR.png)
Source: [Scroll Bridge Docs ](https://docs.scroll.io/en/technology/bridge/cross-domain-messaging/)

Looking historically at tokens bridged, we can see a trend that a marked uptick in bridge TVL occurs for assets onboarded to Aave after February 9 (WETH, wstETH, USDC).

![Screen Shot 2024-05-11 at 10.35.45 AM](https://hackmd.io/_uploads/rJ616XaMA.png)
Source: [DefiLlama](https://defillama.com/protocol/scroll-bridge#tvl-charts)

![Screen Shot 2024-05-11 at 10.49.34 AM](https://hackmd.io/_uploads/BJOTyEafR.png)
Source: [Arkham Intelligence - Scroll wstETH Gateway](https://platform.arkhamintelligence.com/explorer/address/0x6625C6332c9F91F2D27c304E729B86db87A3f504)

WBTC has historically made up a relatively small portion of value bridged to Scroll and has not shown any growth trend, indicating that demand for WBTC integrations on Scroll has been relatively stable but may not be experiencing a growth in opportunities or interest to integrate it into newly launched protocols. Since inception, it has waned at ~40 WBTC bridged or ~$2m.

![Screen Shot 2024-05-11 at 10.54.05 AM](https://hackmd.io/_uploads/SJrJW4az0.png)
Source: [DefiLlama](https://defillama.com/protocol/scroll-bridge#tvl-charts)

# WBTC Integrations on Scroll

To determine whether WBTC is a suitable collateral type on the Scroll network, it is essential to understand the background information on the Scroll bridge and the interest in bridging assets. This context will help assess how WBTC is currently being utilized on Scroll and whether the market for WBTC on this network is sufficiently stable and resilient. The ease of bridging is important in ensuring an efficient arbitrage market and sourcing liquidity for liquidation. However, on-chain liquidity provides a stronger assurance of timely liquidation and merits observing the usage of WBTC on Scroll.

[WBTC on Scroll](https://scrollscan.com/token/0x3c1bca5a656e69edcd0d4e36bebb3fcdaca60cf1), as described above, has not experienced significant demand growth. Here is an overview of how WBTC is being utilized today (May 11, 2024):

![WBTC DeFi Integrations on Scroll (May 11, 2024)(1)](https://hackmd.io/_uploads/By24cNTfA.png)
![WBTC DeFi Integrations on Scroll (May 11, 2024)](https://hackmd.io/_uploads/rknN94pMR.png)
Source: [ScrollScan](https://scrollscan.com/token/0x3c1bca5a656e69edcd0d4e36bebb3fcdaca60cf1#balances) - May 11, 2024

WBTC in contracts make up ~55% of WBTC on Scroll; of those, WBTC is exclusively utilized in DEX venues. The vast majority of WBTC on DEX is paired with WETH.

The most liquid venue is the Ambient Finance ETH/WBTC market. Ambient is a DEX protocol that allows for two-sided AMMs combining concentrated and ambient constant-product liquidity on any arbitrary pair of blockchain assets. At this time (May 11), a swap size of just 2.75 WBTC triggers a price impact warning of >2% price impact.  
![Screen Shot 2024-05-11 at 11.45.32 AM](https://hackmd.io/_uploads/HkrkpEaMC.png)

While it is encouraging to see a diversity of DEX pools having integrated WBTC, the overall adoption of these markets remains low, and WBTC is not a reasonably liquid asset on Scroll. 

This does not preclude liquidators from bridging WBTC off Scroll to complete an arbitrage loop, but the bridge process can take ~1 hour, substantially increasing the risk assumed by the liquidator and/or complexity involved with managing hedged positions across networks or exchanges.

## wstETH Cross-comparison

wstETH will likely face similar challenges as WBTC for use as collateral, so we cross-compare how wstETH is utilized on Scroll.

![Screen Shot 2024-05-11 at 10.36.42 PM](https://hackmd.io/_uploads/rJ-sH06MR.png)
Source: [ScrollScan](https://scrollscan.com/token/0xf610a9dfb7c89644979b4a0f27063e9e7d7cda32#balances) - May 11, 2024

By contrast, wstETH is concentrated much more heavily in EOA addresses. The top 3 wstETH holders on Scroll are EOAs with generally low activity, i.e., do not appear to be market makers but instead generally passive holders. Aside from the Aave integration, wstETH is typically integrated into DEXs, and generally, the wstETH/ETH pair is represented. Ambient and SyncSwap also appear to be the dominant DEX venues.

wstETH may retain a notable advantage over WBTC arbitrage in that it is a stableswap- arbitrageurs may be more inclined to assume prolonged exposure to wstETH in case of a depeg, with the promise that wstETH can be redeemed from Lido directly for a proportional share of its underlying ETH. Given that ETH is available in ample supply on Scroll - a reasonable assumption for an L2 network - wstETH may be more likely to attract market makers without hesitation. In the case of WBTC, arbs must assume exposure to a secondary asset (BTC), which may be undesirable, and a commensurate premium may be expected to restore its peg, i.e., market makers may be less likely to exhibit the necessary demand to absorb liquidation events.

# Recommendation

Our initial recommendation regarding onboarding WBTC on Scroll considers its level of observed adoption and DeFi utilization on Scroll and observations about the relative risk compared to wstETH. 

Despite various DEX integrations, the overall liquidity profile is unimpressive and does not show strengthening growth trends. However, it has maintained a certain consistency, and given that WBTC is the defacto tokenized BTC in the Ethereum ecosystem and has substantial integrations on mainnet and other L2s, it does increase confidence that integrations with WBTC on Scroll are likely to endure. Positive trends here are necessary to minimize the creation of bad debt due to missed liquidations.

As a cursory comparison to the liquidity depth and utilization of wstETH on Scroll vs. WBTC and referencing the size of the wstETH market on Aave Scroll, we can assign a comparable market for WBTC that may be within acceptable risk parameters. The wstETH was established with a 130 wstETH supply cap, which was subsequently raised several times to a current cap of 1,250. WBTC may be suitable to establish with similarly conservative parameters commensurate with the available liquidity on Scroll. A comparable supply cap/borrow cap at market creation, which limits the liquidation risk of WBTC in terms of current market conditions, would be around 6 WBTC supply cap and 2 WBTC borrow cap. These values should undergo additional review from Risk Service Providers before increasing to ensure the market can absorb additional leverage in all foreseeable market conditions.

<!--
Before onboarding WBTC as a collateral asset to Aave, it is advised to consult market makers and ensure 
-->