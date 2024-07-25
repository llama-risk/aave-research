# Summary

LlamaRisk supports the proposal to onboard slisBNB on the Aave V3 BNB Chain market. Overall, we have found the protocol to have a sound design and decent liquidity. We also note the presence of a withdrawal mechanism (albeit with a 7-8 day delay) and an active bug bounty program for up to $1M. Our recommendation for conservative onboarding is based on the following weak points identified:

- Peg stability considerations: While slisBNB has generally maintained its peg, there was a period where it experienced a temporary deviation of up to -4% against BNB on secondary markets. Continued monitoring of peg stability over an extended period would bolster confidence in the asset.
- Immature governance: LISTA token holders have limited control over protocol upgrades and parameter changes, resulting in a rather centralized protocol. Two protocol multisigs (virtually with the same signers) control the protocol with no timelock, and the Admin and Manager roles are assigned to the same 3/5 multisig.
- Potential for losses and bank run if validators incur significant slashing, although unlikely. A maximum of 200 BNB slashing could be covered by profit, albeit through a permissioned process at the team's discretion.

Based on these findings, we recommend disabling emode, setting a supply cap at 2x liquidity within 7.5% price impact, and implementing a 65% LTV. We suggest that ListaDAO address these issues, which would ensure further integration and justify more favorable parameters.

# Collateral risk assessment

In November 2023, [ListaDAO](https://medium.com/listadao/a-new-chapter-introducing-lista-dao-771d69be7930) emerged from the association of both Helio and Synclub. This protocol proposes several DeFi products on the BNB Chain, including the [slisBNB](https://www.coingecko.com/en/coins/lista-staked-bnb) liquid staking token and [lisUSD](https://coinmarketcap.com/currencies/lisusd/), a stablecoin that can be minted using various collaterals. In this assessment, we examine the suitability of slisBNB as collateral on the Aave V3 BNB instance.

## 1. Asset Fundamental Characteristics

### 1.1 Background

#### BNB Chain Hybrid Consensus Model

The BNB Chain comprises two interoperable blockchains: the Binance Beacon Chain (BC) and the Binance Smart Chain (BSC). The BC is being phased out, with its functionalities absorbed into the BSC through the “[BNB Chain Fusion](https://www.bnbchain.org/en/bnb-chain-fusion)” process to consolidate the ecosystem.

ListaDAO uses the BSC chain, powered by a [hybrid consensus model](https://www.bnbchain.org/en/blog/a-journey-to-decentralization-validators-delegators) of Proof-of-Authority (PoA) and Delegated-Proof-of-Stake (DPoS). PoA designates permissioned validators to decide block transactions, while DPoS allows stakers to delegate their stake to their chosen validator. This consensus system prioritizes high availability and performance while providing limited decentralization.

Anyone can become a validator by securing a delegated amount of at least 2,000 BNB. Every 24 hours, the top 21 validators, sorted in decreasing order of their stake, are selected as the *Cabinet* validators. These Cabinet validators propose blocks in turns, similar to [Ethereum's clique signing](https://geth.ethereum.org/docs/tools/clef/clique-signing). The next 24 validators in the sorted list are designated as *Candidate* validators and have a smaller chance of producing blocks. The remaining validators are considered *Inactive* and can only propose blocks after at least 24 hours.

#### Slashing

As in other Proof-of-Stake (PoS) chains, Binance Chain validators are penalized if they fail to perform as expected — a condition known as [slashing](https://docs.bnbchain.org/docs/validator/bc-slashing/#slashing-1). Validators can be slashed for four different reasons:
* [Double Signing](https://docs.bnbchain.org/bnb-smart-chain/validator/overview/#double-sign-slash)
* [Malicious Vote](https://docs.bnbchain.org/bnb-smart-chain/validator/overview/#malicious-fast-finality-vote-slash)
* [Inavailability](https://docs.bnbchain.org/bnb-smart-chain/validator/overview/#downtime-slash)
* [Low Self-Delegation](https://docs.bnbchain.org/bnb-smart-chain/validator/overview/#low-self-delegation-slash)

Unavailability and Low Self-Delegation are considered minor infractions, punished with two days of jail time and a 10 BNB loss in the case of Unavailability. In contrast, Double Signing and Malicious Voting are severe offenses, penalized with 30 days of jail time and a 200 BNB loss.

![image|644x179](upload://oyt4snOLFXTBVz8rhCxayuGK5mP.png)
Source: [BSCScan](https://bscscan.com/advanced-filter?fadd=0x0000000000000000000000000000000000001001&tadd=0x0000000000000000000000000000000000001001&mtd=0xc96be4cb%7eSlash) (July 25th, 2024)

As the above graph illustrates, some validators are frequently in jail for being offline. In practice, this primarily affects validators with the lowest stakes, who are not selected to propose blocks. To determine if any validator has been banned for reasons other than downtime, we examined function calls for methods *submitFinalityViolationEvidence*, *submitDoubleSignEvidence*, and *sendFelonyPackage* in the [SlashIndicator contract](https://bscscan.com/address/0x0000000000000000000000000000000000001001). Our investigation revealed no past transactions for these methods. We also inspected the *felony* method on the [ValidatorSet contract](https://bscscan.com/advanced-filter?fadd=0x0000000000000000000000000000000000001000&tadd=0x0000000000000000000000000000000000001000&mtd=0x35409f7f%7eFelony). While we found three calls, all were associated with failed transactions not initiated by the slash contract. This evidence suggests that no validator has ever been slashed for these more severe offenses.

### 1.2 Asset

slisBNB is a yield-bearing asset backed by staked BNB on the BNB Smart Chain (BSC), with a soft-peg to BNB. It implements the [BEP-20 interface](https://academy.binance.com/en/glossary/bep-20) (a Binance-specific extension of the ERC-20 interface) and follows a re-pricing pattern, where the exchange rate automatically increases against BNB due to accumulated staking rewards. ListaDAO currently levies a 5% fee on the staking rewards accrued by the staked BNB.

slisBNB token statistics (as of July 25, 2024):
- **Circulating supply**: 302,261 slisBNB
- **Market cap**: $172.6m
- **Exchange rate**: 1.0205 BNB
- **Protocol fee**: 5% of staking rewards
- **APR**: 0.81%

### 1.3 Architecture

The architecture is straightforward. Users deposit BNB into the *ListaStakeManager* contract, and new slisBNB tokens are minted from the *slisBNB* contract and sent to the user in return. The *ListaStakeManager* contract then stakes the deposited BNB into the BNB Smart Chain *StakeHub* contract.

The withdrawal process consists of two steps: First, users must request to redeem their slisBNB for BNB by providing slisBNB to the *ListaStakeManager* contract. A minimum withdrawal delay of 7 to 8 days applies. Behind the scenes, the *ListaStakeManager* contract unstakes BNB from the BNB Smart Chain *StakeHub* contract and burns the associated slisBNB tokens.

![image|1354x620](upload://jJuUlTmZr8j43NHe2Z7QBKNxCc2.png)
Source: [contracts architecture](https://github.com/lista-dao/synclub-contracts) (July 14th, 2024)

### 1.4 Tokenomics

In addition to slisBNB, ListaDAO issues the [LISTA](https://www.coingecko.com/en/coins/lista-dao) governance token. LISTA is a BEP-20 token, a Binance Chain token standard that extends the ERC-20 standard commonly found on Ethereum. It acts as a governance token that allows holders to propose and vote for protocol changes. In addition to being available on the secondary market, users can receive LISTA by staking through the ListaDAO or interacting with the protocol over time.

Users must lock their LISTA tokens to participate actively in the governance process to obtain veLISTA. veLISTA cannot be transferred and will be locked for a minimum of 1 week and a maximum of 52 weeks. The veLISTA/LISTA exchange rate depends on the locking time, such that `veLISTA = N * LISTA`, whereas `N` is the number of weeks the token is locked. In addition, the amount of veLISTA tokens will decrease linearly over the locking period. An early claim fee is also levied on redemption requests made before the end of the locking period; starting at 100%, it decreases linearly over time.

[The documentation](https://docs.bsc.lista.org/tokens/tokenomics) states that the LISTA token can only be used to vote on the features of ListaDAO products and does not allow voting on the operation and management of ListaDAO itself. This indicates a rather semi-centralized control of the protocol. Although veLISTA holders cannot make proposals directly for now, they can discuss them with the ListaDAO team, which will consider them. Only the ListaDAO core team can make proposals, and the team retains the right to veto changes and take emergency actions when needed.

We note that there are currently 0 proposals on [snapshot.org](https://snapshot.org/#/listavote.eth). The documentation claims the protocol will gradually switch to a fully on-chain governance process.

## 2. Market Risk

### 2.1 Liquidity

slisBNB is currently supported by two DEX:
- [ThenaFusion slisBNB/WBNB](https://thena.fi/swap?swapType=1): can sell approx. 4,500 slisBNB to BNB, within 7.5% of price impact.
![image|701x142](upload://n0msT8LZcIa7f726oFCh5snTaja.png)
- [PancakeSwap slisBNB/WBNB](https://pancakeswap.finance/swap?inputCurrency=0xb0b84d294e0c75a6abe60171b70edeb2efd14a1b&outputCurrency=0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c?ref=coingecko&user=Coingecko&discount=0&perps=false): can sell 5,850 slisBNB for BNB within 7.5% of price impact.
![image|701x142](upload://n0msT8LZcIa7f726oFCh5snTaja.png)

The total amount of slisBNB that can be sold on secondary markets within a 7.5% price impact is 10,750 slisBNB.

![image|493x276](upload://hlmsu9mgwiW3OGKQyDGOcMr7K3H.png)
Source: [1nch aggregator](https://app.1inch.io/#/56/simple/swap/slisBNB/BNB) (July 25th, 2024)

### 2.2 Volatility

We look at the slisBNB/WBNB market rate on the PancakeSwapV3 liquidity pool. We observe multiple strong downside depegs reaching up to -4% on February 22, 2024, with an upward trend reflecting the added staking rewards over time.

When strong downside depegs are observed, periods coincide with periods of high transacted volume on the chart. The ListaDAO team explained that this depeg was due to an airdrop campaign that encouraged users to mint large amounts of slisBNB and a subsequent pool launch event that led many participants to sell their freshly minted slisBNB, causing significant selling pressure that affected the pool's stability. They later adjusted the parameters of the airdrop campaign and increased the pool's depth, resolving the issue. Additionally, withdrawals took 7-15 days at the time, whereas they only take 7-8 days now, making it easier for arbitrageurs to restore the peg.

![image|845x602](upload://4Q7V09oaj8hQ3nKWX3NZ8iMyUfn.png)
Source: [geckoterminal.com](https://www.geckoterminal.com/bsc/pools/0x9474e972f49605315763c296b122cbb998b615cf?utm_source=coingecko&utm_medium=referral&utm_campaign=livechart) (July 25th, 2024)

### 2.3 Growth

The biggest holder of slisBNB is the *SnBnbYieldConverterStrategy* contract, with around 62% of the total supply. The second biggest holder is a MakerDAO *GemJoin* contract adapter for slisBNB initially deployed by HeliosProtocol, which ListaDAO acquired following their bankruptcy. Consequently, users can now [borrow lisUSD](https://lista.org/borrow-lisusd), ListaDAO's stablecoin, by depositing slisBNB into this *GemJoin* contract. 12% of the minted slisBNB supply is currently used as collateral to mint lisUSD.

With 343,876 holders and a minted supply of 302,261, we obtain a mean balance per holder of 0.878 slisBNB, a fairly small amount that indicates numerous smallholders apart from the three biggest holders previously mentioned.

![image|988x824](upload://2Zlm4gX8Bol4zXpAxhrX0jYEnP9.png)
Source: [BSCscan](https://bscscan.com/token/tokenholderchart/0xB0b84D294e0C75A6abe60171b70edEb2EFd14A1B) (July 25th, 2024)

## 3. Technological Risk

### 3.1 Smart Contract Risk

#### Audits

- [PeckShield (September 1st, 2023)](https://github.com/lista-dao/lista-audit/blob/main/Synclub_SnBNB/PeckShield-Audit-Report-SynclubLSD-v1.2.pdf): 3 medium risk findings, and 1 low risk finding. Re-entrancy is possible in the contract. While no immediate vulnerabilities have been identified, the presence of re-entrancy possibilities should be carefully evaluated and monitored.
- [SlowMist (September 4th, 2023)](https://github.com/lista-dao/lista-audit/blob/main/Synclub_SnBNB/SlowMist%20Audit%20Report%20-%20Synclub.pdf): 1 medium risk, 1 low risk, and multiple suggestions. 

Findings were limited in number and addressed by the team, except for one involving the privileged account. PeckShield and SlowMist recommended using a DAO-like structure to govern the privileged account, controlling contract parameters, and implementing a privilege separation strategy. SyncClub's response was to acknowledge the issue and disclose their plan to use a multisig instead, which is an improvement but could be improved. We can confirm that a multisig wallet has been deployed since then.

#### Code quality

The code for slisBNB is publicly available [in this repository](https://github.com/lista-dao/synclub-contracts). The slisBNB system comprises two main contracts — the *slisBNB* contract and the *ListaStakeManager* contract. The *slisBNB* contract is relatively compact at 74 lines, while the *ListaStakeManager* is considerably larger at 985 lines. The size of the *ListaStakeManager* suggests potential areas for improvement regarding code factorization and readability. This could present challenges for security researchers and developers working with the codebase. However, it's worth noting that the code is relatively well-documented.

The repository shows 135 commits, with contributions made through pull requests and direct pushes to the main branch. This approach indicates that developers are collaborating in a public and transparent manner.

#### Bug Bounty Program

Lista DAO maintains an active [bug bounty program on Immunefi](https://immunefi.com/bug-bounty/listadao/), offering rewards up to $1,000,000 for critical vulnerabilities. The program covers slisBNB and other Lista DAO protocols, incentivizing security researchers to identify and responsibly disclose potential issues.

#### Immutability

The *slisBNB* and *ListaStakeManager* contracts operate behind a *TransparentUpgradeableProxy*. The admin of this proxy is a *ProxyAdmin* contract, which is owned by a [3/6 multisig](https://bscscan.com/address/0x8225fdA5613bd64a1944d3eB7497e380C2885f12). Both high-privilege and medium-privilege functions, which allow changes to key contract parameters and addresses, are accessible by a separate [3/5 multisig](https://bscscan.com/address/0x5C0F11c927216E4D780E2a219b06632Fb027274E). It's worth noting that five signers overlap between these two multisig wallets.

### 3.2 Price Feed Risk

Although no third party currently offers a slisBNB/USD price feed, ListaDAO itself provides an [Oracle for slisBNB](https://bscscan.com/address/0x8ecf78fb59e5a4c26cb218d34db29c4696af89f6). This oracle combines the Chainlink BNB/USD price feed with the internal exchange rate provided by the *ListaStakeManager* contract.

The internal exchange rate provided by the *ListaStakeManager* contract does not rely on external information, as it is calculated using the contract's balance variables. This approach, while straightforward, presents an optimistic view that cannot account for any validator slashing by the BSC chain consensus. 

A potential consequence of this design is the risk of a bank running into a protocol if its validators are slashed. In such a scenario, the last slisBNB holders might be unable to redeem their BNB tokens. When questioned about this risk, the ListaDAO team responded that any potential slashing penalty would likely be a small fraction of the delegated funds, and their accumulated profits would be sufficient to cover the loss. While this may be true, it's important to note that this mitigation process would be permissioned and not guaranteed by any on-chain mechanisms.

### 3.3 Dependency Risk

An off-chain service that operates [through an EOA](https://bscscan.com/address/0x9c975db5E112235b6c4a177C2A5c67ab4d758499) executes multiple daily transactions. The functions it can access, while essential to the correct behavior of the protocol, represent a manageable risk. However, the lack of redundancy posed by a single instance of this off-chain service could hinder the protocol's resiliency and potentially prevent withdrawals.

## 4. Counterparty Risk

### 4.1 Governance and Regulatory Risk

[Legal disclaimer](https://docs.bsc.lista.org/legal-disclaimer/legal-disclaimer) displayed at https://lista.org/ argues that Lista DAO is decentralized, *“acting solely as an arms’ length third party about the LISTA distribution, and not in the capacity as a financial advisor or fiduciary of any person about the distribution of LISTA”*.

The agreement for the distribution of LISTA and the continued holding of LISTA shall be governed by a separate set of Terms and Conditions or Token Distribution Agreements as stipulated by the Disclaimer. However, none of these documents were available on the website at the review date.

The [Representations and Warranties](https://docs.bsc.lista.org/legal-disclaimer/legal-disclaimer#:~:text=Deemed%20Representations%20and%20Warranties) section primarily addresses the LISTA token and all related user activities. Although staking is not specifically mentioned, a broad disclaimer states that neither Lista DAO nor its affiliates deal in, or are in the business of, buying or selling any virtual asset or digital payment token (including LISTA). The document includes standard disclaimers stating that the information provided does not constitute legal, financial, business, or tax advice. The website is for general informational purposes and is not a prospectus, offer document, or solicitation for investment or business engagement. Neither Lista DAO, its contributors, nor any service providers are liable for any direct or indirect damages or losses from accessing the materials related to LISTA available on the website.

The need for more data regarding the implemented governance model and ongoing governance processes hampers the assessment of the decentralization of the protocol. From a structural perspective, some sources ([LinkedIn](https://www.linkedin.com/company/listadao/about/), [Pitchbook](https://pitchbook.com/profiles/company/589677-04#overview)) suggest that Lista DAO may have a corporate seat in Singapore. However, these indications cannot be validated with any references on https://lista.org/. A [lookup](https://lookup.icann.org/en/lookup) on the domain registrant(s) also does not yield any results linked to corporate ownership.

### 4.2 Access Control Risk

Several roles can interact with the protocol, each with different levels of responsibility. Most methods of interest are exposed by the [ListaStakeManager contract](https://bscscan.com/address/0x1adB950d8bB3dA4bE104211D5AB038628e477fE6#writeProxyContract).

The *DEFAULT_ADMIN_ROLE* is assigned to a [3/5 multisig](https://bscscan.com/address/0x5C0F11c927216E4D780E2a219b06632Fb027274E) that can call:
- *setSynFee()* to change the protocol fee on staking rewards.
- *setRedirectAddress()* to change the address that receives the undelegated funds.
- *setRevenuePool()* to change the address that receives the staking rewards.
- *whitelistValidator()* to add a new whitelisted validator.
- *disableValidator()* so that funds can only be undelegated from it, not delegated.
- *removeValidator()* from the whitelist. 
- *togglePause()* to pause minting and withdrawals.
- *toggleVote()* to delegate/undelegate all funds simultaneously.

Although not a role, the Manager can update some of the contract's parameters. It is assigned to the same [3/5 multisig](https://bscscan.com/address/0x5C0F11c927216E4D780E2a219b06632Fb027274E) as the *DEFAULT_ADMIN_ROLE*, and can only access the following functions:
- *setReserveAmount()* to set the BNB buffer to keep inside the *ListaStakeManager* contract.
- *proposeNewManager()* to change the current manager. The new manager's address must later accept this.
- *setBSCValidator()* to change the validator to which BNB must be delegated for staking.
- *setMinBnb()* to set the minimum amount of BNB that can be withdrawn.

The *BOT* role can access low-privilege functions that are essential to the correct behavior of the protocol and is assigned to an [EOA](https://bscscan.com/address/0x9c975db5E112235b6c4a177C2A5c67ab4d758499):
- *UndelegateFrom()* a validator.
- *ClaimUndelegated()* to claim unbonded BNB from a validator.
- *DelegateTo()* validator.
- *CompoundRewards()*.

Only the *ListaStakeManager* contract can mint and burn slisBNB in the *slisBNB* contract. Furthermore, although the *DEFAULT_ADMIN_ROLE* and the Manager are the same 3/5 multisig wallet, they have different privilege levels. Each privilege level should be assigned to its multisig wallet to benefit from the improved security of privilege separation.

## 5. Aave V3 Specific Parameters 

| Parameter                 | Recommendation |
|---------------------------|----------------|
| Isolation Mode            | No               |
| Emode                     | Disabled for BNB  |
| Borrowable                | Yes               |
| Borrowable in Isolation   | No               |
| Collateral Enabled        | Yes               |
| Stable Borrowing          | No               |
| Supply Cap                | 21,500               |
| Borrow Cap                | 2,150               |
| Debt Ceiling              | NA               |
| LTV                       | 65%               |
| LT                        | 70%               |
| Liquidation Bonus         | 7.5%               |
| Liquidation Protocol Fee  | 10%               |
| Reserve Factor            | 20%               |
| Base Variable Borrow Rate | 0%               |
| Variable Slope 1          | 7%               |
| Variable Slope 2          | 300%               |
| Uoptimal                  | 45%               |

**Note**: This assessment follows the LLR-Aave Framework, a comprehensive methodology for asset onboarding and parameterization in Aave V3. This framework is continuously updated and [available here](https://github.com/llama-risk/aave-research/blob/main/frameworks/aave_v3_framework.md).
