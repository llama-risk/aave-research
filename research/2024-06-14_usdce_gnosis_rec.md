## Summary

LlamaRisk supports this proposal to onboard USDC.e, the new bridged USDC token on Gnosis Chain adheres to Circle's Bridged USDC Standard. This standard allows for future upgrades to native USDC issuance, maintains compatibility with Circle products like the Cross-Chain Transfer Protocol (CCTP), and provides a more standardized and efficient user experience than the old bridged USDC token. While current USDC.e liquidity is low, with only one Balancer pool containing approximately $275k USDC.e as of June 13, 2024, it is expected to migrate gradually with the help of incentive programs.

We share our research and analysis below. We do not see a significant change in this asset's risk profile and recommend onboarding, with parameters evolving alongside liquidity provision as it grows.

## Gnosis Bridges

The Gnosis Chain bridge enables the transfer of ERC-20 tokens and xDAI (the chain's native token) between Ethereum and Gnosis Chain. [Bridge types](https://docs.gnosischain.com/bridges/About%20Token%20Bridges/#bridges-conceptual-architecture) include native bridges, 3rd party bridges, and application-specific bridges.

![Ethereum to Gnosis Bridge Design](https://hackmd.io/_uploads/Bk3SDatSA.png)
*Source: [Ethereum to Gnosis Bridge Design](https://docs.gnosischain.com/bridges/About%20Token%20Bridges/)*

For USDC, tokens are bridged via Omnibridge (the native token bridge) and Arbitrary Message Bridge (AMB). USDC is deposited into Omnibridge, and once validated, Omnibridge mints the bridged token on Gnosis (in this case, USDC.e). Omnibridge mints bridged tokens using a variant of the [ERC-677 token standard](https://docs.gnosischain.com/bridges/About%20Token%20Bridges/omnibridge#key-information); bridged tokens are tracked in a canonical 'Bridged Token Registry'.

Built on top of the AMB, Gnosis Bridges relies on a set of validators to enable the deposit and mint of USDC on Gnosis from Ethereum. According to Gnosis docs, "Bridge validators are run by trusted members of the Gnosis community." 

| Attribute     | Description               |
|---------------|---------------------------|
| Trust Mode    | [4-of-8 Validator Multisig](https://docs.gnosischain.com/bridges/management/validators#amb--omnibridge) |
| Governance    | [8-of-16 Multisig](https://docs.gnosischain.com/bridges/management)          |
| Bug Bounty    | $2m                       |
| Bug Reporting | Immunefi                  |

## Bridged USDC Standard

Before the bridged standard, the only way for new L1s and L2s to generate USDC liquidity was through their unofficial bridge of USDC in the absence of native USDC. These 3rd party tokens are not issued nor redeemable for US dollars by Circle and serve as a proxy where Circle has not yet deployed native USDC.

The main points of difference between bridged USDC and native USDC include:
* Tokens are backed by USDC, not US dollars
* Multiple unofficial 3rd party versions
* Not compatible with Circle products like Cross-Chain Transfer Protocol (CCTP)

The [Bridged USDC Standard](https://www.circle.com/blog/bridged-usdc-standard) is a specification and process for deploying a bridged form of USDC on EVM blockchains with optionality for Circle to upgrade to native issuance in the future, introduced by Circle in Nov 2023. The standard will allow ecosystems to transfer ownership of a bridged USDC token contract to Circle to upgrade to native USDC (enabling compatibility with Circle products).

The standard does not require migration by holders and upgrades in place, maintaining applications, addresses, and balances. Existing bridged USDC token contracts cannot be upgraded to match the Bridged USDC Standard, requiring holders of 'old' bridged USDC to migrate. Old USDC can be swapped for USDC.e via the Gnosis bridge, and newly bridged USDC automatically transfers to USDC.e.

![image|644x628, 75%](upload://xb9UjAhnGtu3khGVjHCRwLykzmL.png)
Source: [Gnosis Bridge - USDC swap](https://bridge.gnosischain.com/usdc)

## Assessment

USDC.e liquidity is currently low, with a single Balancer pool at the time of writing. Based on the recent activity of the contract, it is reasonable to expect liquidity to slowly transition away from the old USDC token to USDC.e (the total supply of the old USDC is currently ~9.4M). 

#### USDC.e Liquidity

Currently, little data is available on liquidity for USDC.e, according to [Coinmarketcap](https://coinmarketcap.com/dexscan/gnosis/0xfc095c811fe836ed12f247bcf042504342b73fb700000000000000000000009f-0x2a22f9c3b484c3629090feed35f17ff8f88f76f0-0xaf204776c7245bf4147c2612bf6e5972ee483701/#TradeHistory) a single USDC.e pool exists on Balancer v2. When looking at Balancer, a single [USDC.e/USDT/sDAI pool](https://app.balancer.fi/#/gnosis-chain/pool/0xfc095c811fe836ed12f247bcf042504342b73fb700000000000000000000009f) exists, but liquidity is low, ~$1.15M in total and $276,537 in USDC.e as of June 13 2024.

#### USDC.e Distribution

An overview of USDC.e distribution shows that the current total supply stands at [~291,663](https://gnosisscan.io/token/0x2a22f9c3b484c3629090feed35f17ff8f88f76f0). Close to 95% of the total supply is held in the Balancer 3pool as of June 13, 2024. 

The proposal of an incentive program by Gnosis DAO indicates an intention to push for migration and attract greater liquidity. However, this presents two potential factors to consider that relate to onboarding:
1. The incentive program could attract short-term yield seekers, and once incentives end, this could lead to capital withdrawals.
2. Historical stablecoin TVL on the Gnosis Chain has remained relatively stable over the last six months, and by proxy, USDC (as shown in the graph below). Liquidity expectations should consider historic levels seen with old USDC and, therefore, consider liquidity growth related to subsequent incentive programs.
 
![image|958x323](upload://xk5GFb5GkfAoKvOmL5Qv3SQckAm.png)
*Gnosis chain TVL. Source: [DeFiLlama](https://defillama.com/chain/Gnosis?stables=true&inflows=false), June 14th, 2024*

The migration away from USDC has overall benefits from an efficiency standpoint; the bridge standard creates a more fluid cross-chain experience for users, interoperability with Circle products that expand USDC usability, and standardized transfers. It should be noted that this remains a bridged USDC and not a native USDC since the option to upgrade remains to be enacted by Circle.

The main benefit of CCTP is greater [capital efficiency](https://developers.circle.com/stablecoins/docs/cctp-getting-started) when bridging given unified liquidity across ecosystems; the Circle utility allows bridges to incorporate its functionalities to facilitate transfers. Since the same bridge mechanism is used for USDC.e, validator risk in the form of fraudulent messages relayed to bridge contracts could create exploit opportunities. Omnibridge is [governed](https://docs.gnosischain.com/bridges/governance) by an 8-of-16 multisig and controls contract upgrades and parameters. Although a remote possibility, malicious upgrade code could affect bridge operations and the user's ability to transfer liquidity away from GC.

Ultimately, this migration will reduce costs associated with bridging USDC, expand USDC utility, and, through standardization, offer greater security aligned with native USDC code. Liquidity is currently limited, as the migration was initiated fairly recently and needs more historical data. Bridge contract and validator risks remain identical to those of the previously onboarded USDC asset.
