## Summary

This proposal to remove DAI from eMode on Arbitrum, Avalanche, Optimism, and Polygon aligns with the DAO's decision to reduce the loan-to-value (LTV) ratios for DAI and sDAI on Aave. We note that the main area of concern is the recent exposure of DAI to Ethena's USDe and Maker's evolving roadmap, with new details (NewStable & PureDai tokens) announced this week.

Based on our extensive risk assessment of USDe ([general assessment](https://cryptorisks.substack.com/p/asset-risk-assessment-ethena-usde) | [Aave specific considerations](https://governance.aave.com/t/arfc-onboard-usde-to-aave-v3-on-ethereum/17690/3?u=llamarisk)), we concluded that Ethena does not currently pose a significant risk to DAI backing. DAI exposure to USDe is marginal, **4% at the time of writing**, and up to 12% if the D3M loan reaches the approved debt ceiling of 1b. USDe liquidity provision, mainly on Curve and Uniswap and also supplemented by the recent Bybit listing, appears to be sufficient. We also note a good diversification of DAI's over-collateralized portfolio.

LlamaRisk believe this change is not immediately required, with the potential for adverse effects on a few large accounts, as noted by @mcsquared. Should the DAO decide to proceed, allowing sufficient time for depositors at risk of liquidation to take appropriate actions is recommended to ensure a smooth transition and minimize user impact.

## Risk considerations

### DAI exposure to Ethena Protocol

DAI gains exposure to Ethena's hedged perpetual yield through the ["DIRECT-SPARK-MORPHO-DAI"](https://makerburn.com/#/collateral/DIRECT-SPARK-MORPHO-DAI) loan facility. By minting DAI to a [Spark DAI MetaMorpho vault](https://app.morpho.org/vault?vault=0x73e65DBD630f90604062f6E02fAb9138e713edD9), Maker supports the supply of DAI to multiple markets that can be borrowed against with USDe/sUSDe collateral.

![image|896x426](upload://liN3yJ7DxGiNc94LAKYFIrpIgSu.png)

Source: [Makerburn.com](https://makerburn.com/#/rundown), May 16th, 2024

![image|911x343](upload://6tCA2zhTjB3uGXf37f940IA4GFe.png)

Source: [Makerburn.com](https://makerburn.com/#/rundown), May 16th, 2024

### Upcoming Developments in the Maker ecosystem

In line with the ever-evolving Maker endgame plan, it is important to follow the latest developments and roadmap for DAI, namely:

#### Vision of DAI's Future

The latest perspectives on the future of DAI can be found in this [forum post](https://forum.makerdao.com/t/reconciling-the-two-opposing-paths-for-decentralized-stablecoins/24280). The Maker community's vision for DAI involves creating two distinct stablecoins to address the Stablecoin Trilemma: NewStable, focused on utility and scale, and PureDai, emphasizing pure decentralization. NewStable will integrate RWAs and TradFi, while PureDai will use only decentralized collateral. The transition will be gradual, with DAI initially functioning as usual and eventually serving as a backend for NewStable. MKR will remain linked to MakerDAO, allowing holders to upgrade to a new governance token.

The ongoing monitoring of these changes and how they may impact the Aave ecosystem is very important.

#### Discussion on additional exposure to USDe

Maker is [considering gaining additional exposure to USDe](https://forum.makerdao.com/t/bt-project-ethena-risk-legal-assessment/23978) via their Andromeda vault, involving:

* TACO Foundation & TACO & SUBS, LLC: Cayman Islands entities to facilitate real-world activity
* BlockTower Capital: Manages assets per Subsidiary's guidelines
* Ankura Trust: Paying agent for fees, assists with deployment/returns
* Coinbase: Exchange & custody platform (Coinbase Prime Web3 Wallet)

We plan on posting a detailed analysis of the implications of this change should Maker decide to proceed with this proposal.