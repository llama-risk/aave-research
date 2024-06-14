## Recommendation

LlamaRisk supports the assets and parameters recommended by @ChaosLabs for deploying Aave V3 on zkSync Era: **USDC (native)**, **USDT**, **WETH**, and **wstETH**. 

zkSync Era shows promising trends in [user adoption](https://dune.com/matter_labs/zksync-era-overview) and [developer activity](https://zksync.io/ecosystem). However, DEX liquidity remains relatively low and concentrated primarily on [SyncSwap](https://syncswap.xyz/). The presence of official and third-party bridges is a positive factor, but the 24-hour withdrawal delay from zkSync to Ethereum mainnet could pose challenges for liquidators in volatile market conditions. 

While liquidity for the newly launched native USDC is very early, we believe listing it over the bridged USDC.e token is advantageous. Native USDC avoids the inherent risks associated with bridged assets and will likely see improved liquidity as Circle and its partners continue incentivizing integrations and usage across the zkSync ecosystem.

Liquidity provisions are expected to improve rapidly over the next period, and we are likely to support increased caps and onboarding of additional assets as the ecosystem matures.

## About zkSync Era

- zkSync Era is a Layer 2 scaling solution for Ethereum that utilizes zk-rollups to batch multiple transactions off-chain and submit a single proof to the Ethereum mainnet.
- Launched in April 2024, zkSync Era currently has a Total Value Locked (TVL) of over [$750m](https://defillama.com/bridged/zkSync%20Era) ([≈$130m](https://defillama.com/chain/zkSync%20Era) excluding bridged ETH) as of June 12th, 2024.
- The network hosts a small number of Dapps, including DEXes ([SyncSwap](https://syncswap.xyz/), [zkSwap](https://zkswap.finance/), [Koi](https://dapp.koi.finance/swap), [Maverick](https://www.mav.xyz/), [PancakeSwap](https://pancakeswap.finance/), and [IziSwap](https://izumi.finance/trade/swap)) and [ZeroLend](https://zerolend.xyz/), an Aave V3 fork.

![image|718x539, 75%](upload://xUUPOAfk7g27d62cJXvPB4swOWV.png)
Source: [DefiLlama](https://defillama.com/chain/zkSync%20Era), June 11th, 2024

## Main Tokens

The main tokens on zkSync Era and their supply as of June 12th, 2024 (source: [zkSync Era Explorer](https://era.zksync.network/)):

| Token  | Contract                                     | Supply     | Supply ($) |
|--------|----------------------------------------------|------------|------------|
| USDC.e [1] | [`0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4`](https://era.zksync.network/address/0x3355df6d4c9c3035724fd0e3914de96a5a83aaf4) | 85,921,544 | 86,179,309 |
| WETH   | [`0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91`](https://era.zksync.network/address/0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91) | 13,166     | 47,665,197 |
| USDT   | [`0x493257fD37EDB34451f62EDf8D2a0C418852bA4C`](https://era.zksync.network/address/0x493257fD37EDB34451f62EDf8D2a0C418852bA4C) | 14,675,886 | 14,690,562 |
| WBTC   | [`0xBBeB516fb02a01611cBBE0453Fe3c580D7281011`](https://era.zksync.network/address/0xBBeB516fb02a01611cBBE0453Fe3c580D7281011) | 201        | 13,979,599 |
| wstETH | [`0x703b52F2b28fEbcB60E1372858AF5b18849FE867`](https://era.zksync.network/address/0x703b52F2b28fEbcB60E1372858AF5b18849FE867) | 991      | 3,587,737  |
| DAI    | [`0x4B9eb6c0b6ea15176BBF62841C6B2A8a398cb656`](https://era.zksync.network/address/0x4B9eb6c0b6ea15176BBF62841C6B2A8a398cb656) | 1,162,825  | 1,166,313  |

[1] [Native USDC launched on zkSync](https://www.circle.com/blog/what-you-need-to-know-native-usdc-on-zksync) (April 9th), bridged USDC is USDC.e, which remains the more widely used token.

## Oracle Providers

We recommend using Chainlink price feeds for zkSync, namely:

* [ETH/USD](https://data.chain.link/feeds/zksync/zksync/eth-usd) (0.5% deviation threshold, 24h heartbeat)
* [USDC/USD](https://data.chain.link/feeds/zksync/zksync/usdc-usd) (0.3% deviation threshold, 24h heartbeat)
* [USDT/USD](https://data.chain.link/feeds/zksync/zksync/usdt-usd) (0.3% deviation threshold, 24h heartbeat)

[Pyth Network](https://pyth.network/blog/pyth-launches-price-oracles-on-zksync-era) also offers price feeds on zkSync using its "On-Demand Price Update" model. However, the methodology and data provider sources used by Pyth Network are not readily accessible.

## Bridging Assets

Asset transfers are achieved through the Official zkSync Bridge and third-party bridging solutions.

### Official zkSync Bridge

The Official zkSync Bridge enables asset transfers between Ethereum and zkSync Era. Its key components are:

- **Bridgehub Contract on L1**: Central hub for bridges, locking L1 assets for all ZK chains. Implements registry, ETH deposits/withdrawals, and message routing.
- **State Transition Contract**: Manages proof verification and data availability for ZK chains. Uses StateTransitionRegistry and deploys DiamondProxy with facets for each chain. 
- **Upgrade Mechanism**: Ensures all chains are updated to the latest implementation. Non-compliant chains are frozen until updated.
- **WETH Contract**: Deployed from L1 WETH bridge for seamless wrapped ETH transfers.

![image|2000x2116](upload://3deVYYICCqXfaDxX0pGcrm360Lb.png)
Source: [zkSync documentation](https://docs.zksync.io/zk-stack/components/shared-bridges)

#### Bridging Process

1. **Deposit (Ethereum to zkSync Era):**
   - Users lock tokens on Ethereum via L1 bridge contract `deposit`, specifying destination chain. 
   - Bridgehub mints tokens on destination L2.

2. **Withdraw (zkSync Era to Ethereum):**
   - Users burn tokens on source L2 via L2 bridge contract `withdraw`.
   - L2 bridge sends withdrawal info to Bridgehub.
   - After processing (24-hour delay), Bridgehub releases funds on Ethereum.

The bridge contract ([`0xD7f9f54194C633F36CCD5F3da84ad4a1c38cB2cB`](https://etherscan.io/address/0xd7f9f54194c633f36ccd5f3da84ad4a1c38cb2cb)) was recently migrated and now holds the canonically bridged assets.

![image|857x451](upload://g680om1J6ZWhkU7SsLnxHgbEvAq.png)
Source: [L2Beat](https://l2beat.com/scaling/projects/zksync-era/tvl-breakdown), June 12th, 2024

### Third-party Bridges

Third-party bridges, such as [Orbiter Finance](https://www.orbiter.finance/), [Bungee Exchange](https://www.bungee.exchange/?intro=true), [LayerSwap](https://www.layerswap.io/app) & [Symbiosis](https://app.symbiosis.finance/bridge), expand zkSync interoperability with other L1 and L2 networks. 

## Liquidity 

SyncSwap dominates the DEX liquidity landscape on zkSync Era. Its multiple pool types (Classic, Stable, Aqua) aim to optimize for different trading pairs and use cases. It is also worth noting that [Uniswap just launched on zkSync](https://blog.uniswap.org/zksync-is-now-live-on-uniswap), with other mainnet DEXs likely to follow suit.

![image|898x391](upload://4VaFtwuLGHzPpxNs1KMq9rdJZr8.png)
Source: [DeFillama](https://defillama.com/dexs/chains/zksync-era), June 14th, 2024

Overall liquidity remains relatively low, especially for the newly launched native USDC. DEX liquidity is mainly concentrated around the USDC.e/ETH ($30m), WBTC-ETH ($5.1m), and USDC.e/USDT ($5.7m) pairs as of June 12th, 2024. This does not preclude liquidators from bridging assets off zkSync to complete an arbitrage loop. However, the native bridge process currently takes 24 hours, with faster options using third-party bridges, substantially increasing the risk the liquidator assumes and the complexity involved with managing hedged positions across networks or exchanges.
