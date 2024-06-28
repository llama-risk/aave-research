## Recommendation

LlamaRisk reviewed artMETIS, a Liquid Staking Derivative (LSD) on the Metis L2 chain, and recommends holding off onboarding until i) access control of its upgradeable contracts is transferred to a multi-sig, ii) unstake feature is enabled, and iii) its peg against METIS improves. Most of its contracts, including the artMETIS token ERC20 contract, can be upgraded by a single EOA without a timelock. This critical flaw in its access control could lead to a manipulation of the artMETIS supply, a risk that we deem unacceptable for Aave. The absence of an unstake feature, planned for the near future, has also led to a deteriorating peg against METIS. Based on this review, we advise against onboarding. The full review is provided below for Aave's consideration.

## Resources
- Metis L2 documentation: docs.metis.io/dev/decentralized-sequencer/overview
- Artemis documentation: docs.artemisfinance.io
- Sequencers: sequencer.metis.io/#/sequencers#sequencer

## Introduction

artMETIS is an LSD proposed by Artemis on the Metis L2 chain. It represents staked METIS tokens — the native token of the Metis L2 chain — which are staked as collateral by users to get the right to operate sequencers of the Metis L2 chain. Artemis offers to operate sequencers and stake METIS tokens on behalf of their users. It is the third-biggest dApp in terms of TVL on the Metis L2 chain, with $9.2m in assets locked. With a TVL of $5.4m, the Enki Protocol is its only competitor.

## I - Asset Fundamentals

#### Metis L2 chain

Metis is an L2 rollup that settles on Ethereum mainnet. According to [L2Beat](https://l2beat.com/scaling/projects/metis), it represents 0.97% of the L2 market share. Metis L2 utilizes the Optimistic Virtual Machine (OVM) codebase, an early iteration of the Optimism codebase. The primary challenge with the OVM lies in its partial compatibility with the Ethereum Virtual Machine (EVM), necessitating additional development efforts for teams to deploy their applications on this platform. Subsequently, Optimism developed OVM 2.0, which achieved full EVM compatibility. This updated codebase is currently employed by numerous rollups, including the official Optimism L2 rollup. However, Metis L2 has opted to continue using the initial version of the OVM.

Source: [Perpetual Protocol blog post](https://blog.perp.fi/everything-you-need-to-know-about-optimism-86477fd104c5)

METIS token statistics (as of the 20th of June 2024):
- Total supply: 10,000,000
- Circulating supply: 5,686,334
- Market cap: $290,915,236
- Staked supply: 335,168 METIS (5.89% of circulating supply)
- Number of sequencers: 6

#### Metis staking

Contrary to Ethereum L1 (mainnet), where staked ETH provides economic security to ensure the chain's state is correct, METIS tokens are staked to provide economic security to the decentralized set of sequencers of the Metis L2 chain. In an optimistic L2 chain, transactions are processed off-chain to increase scalability. The backend process responsible for ordering transactions is called a sequencer. The staking of METIS tokens provides economic security to a decentralized set of sequencers by operating a Proof-of-Stake Sequencer Pool. In their beginnings, most L2 chains opted to centralize their sequencers and considered decentralizing them later. Metis L2 is the first rollup to attempt to decentralize its sequencers. Please refer to the [official documentation of Artemis](https://docs.artemisfinance.io/backgroud/decentralized-sequencer) for more information.

![image|2000x1128](upload://rP7OIB2EieaBJQs6rf0jhKGBFvt.png)
Metis L2 chain sequencers. Source: [Metis L2 official website](https://sequencer.metis.io/#/sequencers#sequencer)

Metis currently boasts 6 sequencers, of which the Metis team operates 3. Although a good first step, especially compared to other L2 chains, this remains a limited degree of decentralization. To get the right to operate a sequencer and secure the Metis L2 network, participants must stake at least 20,000 METIS tokens ($1.02M as of the 20th of June 2024) in an L1 contract called the Sequencer Locking Pool. A sequencer's stake is limited to 100,000 METIS. If the maximum number of sequencers is reached, candidates enter a FIFO queue and are selected when a new sequencer spot is freed. Underperforming sequencers can be rejected from the pool. On deposit, participants receive a Soul Bound Token (SBT) containing their sequencer ID. This SBT is later destroyed upon their exit from the sequencer pool.

Sequencers in the pool are selected, in turn, according to a weighted random selection algorithm that considers their voting power, which is a linear function of each sequencer's stake. The probability for a sequencer to be selected, P(A), is calculated as follows:
```
P(A) = VotingPower(A) / TotalVotingPower 

votingPower(A) = lockedAmount(A) / 10^18
```
Source: [Metis L2 chain documentation](https://docs.metis.io/dev/decentralized-sequencer/overview/selection-and-rotation)

A new random selection is made if the active sequencer is down. According to the documentation, apart from being ejected from the sequencer pool and missing out on future rewards, no penalties are inflicted upon underperforming sequencers. Active and well-performing validators are rewarded with a 20% APY reward on their stake, and withdrawals are subject to a 21-day unbonding period.

#### Artemis protocol
 
artMETIS is a liquid staking token representing staked METIS in the *Sequencer Locking Pool* L1 contract. This re-pricing token can be exchanged to increase METIS tokens thanks to the accrued staking rewards. Because of how the Metis L2 staking system works, there is no risk of slashing. Therefore, depegging risks are limited to potential smart contract vulnerabilities and exploits.
 
![image|1536x697](upload://kqLc0QfmdH1Fy8fVuPW0FteLgrh.png)
Source: [Metis L2 documentation](https://docs.artemisfinance.io/mechanism/architecture)

The Artemis architecture spans both layers because the sequencers are tracked on L1. The system works as follows: METIS token holders deposit METIS tokens on the Metis L2 network into the *artMETIS Module* contract and return the artMETIS token in exchange. The Artemis protocol will automatically deposit user deposits into the L1 bridge and stake them into the *Sequencer Locking Pool* L1 contract. Artemis currently operates two sequencers:
- [ArtemisSuperNode](https://sequencer.metis.io/#/sequencers/0x31e623dcb8b43ad4d05aaa6209574cf336980590): locked 100,000 METIS tokens since 22nd of March 2024. 100% of blocks signed. 
- [ArtemisSuperNode2](https://sequencer.metis.io/#/sequencers/0xec05be638d1941c788244603aebb5b937cd72c21): locked 75,167 METIS tokens since the 13th of April 2024. 96% of blocks signed.

We observe that the *ArtemisSuperNode2* sequencer has a 96% block signing rate, the lowest block signing rate of all sequencers. However, this remains a relatively high rate and is not a cause for concern.

It's important to note that unstaking functionality is yet to be enabled in the Artemis protocol. The planned unstaking process will involve a 21-day unbonding period once implemented, which is expected to occur shortly.

#### Incentives

METIS staking currently provides a relatively high reward rate of 20%. Usually, liquid staking provides a staking yield slightly lower than the underlying staking yield because the protocol takes a cut of the staking yield. This differs from artMETIS, which currently proposes a staking yield of 74.08% APY, a boosted staking yield provided by a $50M incentive program funded by Artemis. This indicates that Artemis is well-funded. The artMETIS staking yield is calculated as follows:

```
artMETIS APY = 20% sequencer APY + (10% x 50M $USD / TVL)
```

It follows from the calculation that the incentive will gradually decrease as the TVL of the protocol approaches 50M $USD.

## II - Market Risk Assessment

#### Key metrics (as of the 20th of June 2024)

- Circulating Supply: [177,311 artMETIS](0x2583A2538272f31e9A15dD12A432B8C96Ab4821d)
- Holders: [2,293 unique holders](https://explorer.metis.io/token/0x2583A2538272f31e9A15dD12A432B8C96Ab4821d/tokenholderchart)
- METIS staking share: 52%

#### Liquidity

![image|1630x982](upload://cNBtbpZqohsgwM8M4EdNXzHNpuz.png)

Source: daily volume of the [HerculesV3 artMETIS/WMETIS](https://app.hercules.exchange/pools/0x75A05DEa768F5a8E90227d900EC82038e4584e9a) liquidity pool in USD

The primary liquidity venue for artMETIS is the [artMETIS/WMETIS](https://app.hercules.exchange/pools/0x75A05DEa768F5a8E90227d900EC82038e4584e9a) liquidity pool on the [HerculesV3 exchange](https://app.hercules.exchange/), the main swap exchange of Metis L2 chain. The pool currently boasts a $1.6m TVL. It relies on a [Channel Multiplier Strategy from SteerProtocol](https://app.steer.finance/vault/0x252d0af80d46652a74b062be56c1cc38324d3ea4), an LP method that aims to capitalize on market deviation from the theoretical peg.

![image|2000x657](upload://w7iRspmiAOS2zLkAn3Ka1xtTHgp.png)
Liquidity trend in the HerculesV3 artMETIS/WMETIS pool. Source: [SteerProtocol](https://app.steer.finance/vault/0x252d0af80d46652a74b062be56c1cc38324d3ea4)

#### Volatility

![image|2000x936](upload://gUe5kshTPLjMxasjzHqgd0HPNaH.png)
[HerculesV3 artMETIS/WMETIS](https://app.hercules.exchange/pools/0x75A05DEa768F5a8E90227d900EC82038e4584e9a) Source: [geckoterminal.com](https://www.geckoterminal.com/metis/pools/0xfd1f58c4c05d8ed5040ee9ba7edb5cc5bf53930e?utm_campaign=livechart-btn&utm_medium=referral&utm_source=coingecko)

The secondary market rate between artMETIS and METIS, its underlying asset, has been slowly declining since its inception. This is troubling since the opposite should be observed: a unit of artMETIS should be exchangeable for increasing METIS tokens through time, thanks to the accrued rewards from the Metis L2 sequencer pool. The depeg on secondary markets currently stands at 3.9%, which is relatively large compared to the observed deviation of other liquid staking tokens. 

The absence of an unstake feature, currently pending launch by the METIS sequencer node, has contributed to a deteriorating peg of artMETIS against METIS. This depeg is likely exacerbated by a $50m incentive program that has boosted staking yields from 20% to approximately 75%. Some stakers may constantly be withdrawing their rewards and converting them into METIS tokens, creating selling pressure on artMETIS. The team plans to enable unstaking shortly, including a 21-day unbonding period. While this unbonding period might initially limit liquidity, introducing unstaking functionality is anticipated to help recover the peg.

#### Growth

Looking at the top holders on L1, we can see that 3/4 of the total supply helps in the Metis official bridge, that is, the Metis L2 chain. The second top holder is the *SequencerLockingPool* contract, in which sequencer operators must lock their METIS tokens. The third top holder is Binance.

![image|1748x726](upload://3WYerhwdzKMbfH2qvdRTHcEUJcD.png)
Source: [Etherscan](https://etherscan.io/token/tokenholderchart/0x9e32b13ce7f2e80a01932b42553652e053d6ed8e)

Unique holder addresses on L2 have reached a maximum of 800,000 addresses.

![image|2000x996](upload://5zaL3MCpslSrgdw4FBd27mMCzQ7.png)
Source: [Metis explorer](https://explorer.metis.io/chart?id=activeaddresses&metrics=chain%3A1088%3AActive%20Addresses%3A%2327aeef%3Aday%3Alinear%3Aline%3Avisible%3Ay1)

The TVL reached a maximum of ~$14m at the beginning of June 2024 and has since retraced to a previously observed plateau of ~$10M.

![image|1420x722](upload://7VeBYQVIk3y6fnZSB3VOKrz2vYu.png)

Source: [DeFiLlama](https://defillama.com/protocol/artemis-finance#information)

## III - Technological Risk

### 3.1 Smart Contract Risk Assessment

#### Audits

Artemis has been audited by [PeckShield](https://79226619-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F198urHxz9fLDSymBGOYf%2Fuploads%2F7DxuyRfKvFSf1kTGkLwN%2FPeckShield-Audit-Report-Artemis-v1.0.pdf?alt=media&token=c449e10d-a8a0-493a-8141-90edee52da94) on the 26th of January 2024. This audit revealed three findings, including one medium risk and two low risks. Notably, PeckShield classified the extended responsibilities of the ADMIN_ROLE as medium risk for the protocol and recommended transferring this role to a proper DAO-like governance contract. The Artemis team claimed that the issue was mitigated by transferring this role to a multisig, better than an EOA but still far from truly decentralized governance.

#### Codebase

Artemis contracts are verified on Metis Explorer but are not available on GitHub. No details about off-chain services comprising the Artemis protocol are provided, limiting transparency and independent review.

#### Upgradeability

All L2 contract implementations use *TransparentUpgradeableProxy* contracts with a *proxyAdmin* at [0x479603DE0a8B6D2f4D4eaA1058Eea0d7Ac9E218d](https://explorer.metis.io/address/0x479603DE0a8B6D2f4D4eaA1058Eea0d7Ac9E218d), owned by an EOA at [0xc493BD1d8d794357E79dA84613b67533Afc4D337](https://explorer.metis.io/address/0xc493BD1d8d794357E79dA84613b67533Afc4D337).

This single-EOA control is a critical security flaw. If compromised, an attacker could upgrade contracts to allow infinite minting of artMETIS tokens, risking complete value loss. The lack of a timelock exacerbates this vulnerability by enabling immediate execution of changes. While initially chosen for development ease, this centralized control violates best practices for decentralized protocols. The team plans to transfer ownership to a multisig wallet, which is urgently needed to enhance security and decentralization.

In contrast, the [Sequencer Locking Pool](https://etherscan.io/address/0x0fe382b74c3894b65c10e5c12ae60bbd8faf5b48) L1 contract uses a more secure [4/9 protocol multisig](https://etherscan.io/address/0x48fE1f85ff8Ad9D088863A42Af54d06a1328cF21) ownership. A similar approach should be swiftly implemented for L2 contracts to address current vulnerabilities.

<!--
L2 contact list
- priceFeed 0xD4a5Bb03B5D66d9bf81507379302Ac2C2DFDFa6D -> 4/9 multisig 0xe272dAe29dfE0fB36755D20993716D6142055E3f
- proxyAdmin 0x479603DE0a8B6D2f4D4eaA1058Eea0d7Ac9E218d -> EOA 0xc493BD1d8d794357E79dA84613b67533Afc4D337
- amtConfig 0x4D32C8Ff2fACC771eC7Efc70d6A8468bC30C26bF -> proxyAdmin 0x479603DE0a8B6D2f4D4eaA1058Eea0d7Ac9E218d
- artMETIS 0x2583A2538272f31e9A15dD12A432B8C96Ab4821d -> proxyAdmin 0x479603DE0a8B6D2f4D4eaA1058Eea0d7Ac9E218d
- amtRewardPool 0x0Cf6ab3c169B0169E35aD58D350CbACdaF80E139 -> proxyAdmin 0x479603DE0a8B6D2f4D4eaA1058Eea0d7Ac9E218d
- amtDepositPool 0x96C4A48Abdf781e9c931cfA92EC0167Ba219ad8E -> proxyAdmin 0x479603DE0a8B6D2f4D4eaA1058Eea0d7Ac9E218d
- chainlinkOracle 0x22Fc5A29bd3d6CCe19a06f844019fd506fCe4455 -> proxyAdmin 0x479603DE0a8B6D2f4D4eaA1058Eea0d7Ac9E218d
- oMETIS 0x70f61901658aAFB7aE57dA0C30695cE4417e72b9 -> proxyAdmin 0x479603DE0a8B6D2f4D4eaA1058Eea0d7Ac9E218d
- vester 0x357F55b46821A6C6e476CC32EBB2674cD125e849 -> proxyAdmin 0x479603DE0a8B6D2f4D4eaA1058Eea0d7Ac9E218d
-->

### 3.2 Price Feed Considerations

A [Chainlink price feed](https://explorer.metis.io/address/0x22Fc5A29bd3d6CCe19a06f844019fd506fCe4455) is available on Metis L2 chain for the METIS/USD exchange rate. This could be used with the exchange rate, derived by `amtDepositPool.totalDeposits() / artMETIS.totalSupply()`.

### 3.3 Dependencies

As a liquid staking token representing staked METIS that secures the Metis L2 chain, Artemis directly inherits the risk associated with the Metis L2 chain. With a TVL of only ~$56m, Metis L2 chain is a relatively small L2 chain whose limited economic security budget might prevent its ability to secure itself. Furthermore, the limited number of sequencers it relies upon and the absence of penalties for underperforming sequencers might hinder its ability to maintain high uptime. 

## IV - Counterparty Risk

### 4.1 Governance and Regulatory Risk Assessment

#### Governance model

Artemis plans to distribute the ART token, allowing users to vote on governance proposals. Below is a draft of the planned allocation.

![image|1316x948, 75%](upload://c26pjGJp4PFWns5N3FOczod82TS.png)

Source: [Artemis documentation](https://docs.artemisfinance.io/mechanism/tokenomics)

For now, the protocol is centralized in the hands of the Artemis team. There is no public forum where protocol upgrades are discussed.

#### Regulatory risks

It's noted that the METIS staking functionality is accessible through https://artemisfinance.io. The website links to a [Docs section](https://docs.artemisfinance.io/) detailing artMETIS mechanics, fees, deployed contracts, security audits, and related information. However, a significant absence is observed—neither the 'Docs' nor the landing page includes a comprehensive Terms of Service or similar document outlining conditions governing access to and use of the protocol's front-end interface. Ideally, such terms would cover eligible user profiles, acceptable use policies, restrictions, liability limitations, warranties, and dispute resolution mechanisms.

The lack of specific risk disclaimers or disclosures related to the protocol's intricacies is also noticeable. While acknowledging the protocol's inherently non-custodial nature, activities on the front-end layers may be subject to various rules and regulations. Including risk explanations would benefit both the front-end operator, establishing liability boundaries, and users, enabling them to understand better and potentially mitigate risks.

The Artemis team should expand on METIS staking options beyond the centralized https://artemisfinance.io interface. Given its potentially centralized control, users should be informed about alternative ways to interact with the protocol if the front end is no longer supported or undergoes modifications.

### 4.2 Access Control

The *proxyAdmin* contract, which is the admin of all contracts on L2, is itself owned by an EOA located at [0xc493BD1d8d794357E79dA84613b67533Afc4D337](https://explorer.metis.io/address/0xc493BD1d8d794357E79dA84613b67533Afc4D337). The only contract that is not controlled by the *proxyAdmin* is the *priceFeed* contract which is owned by a [4/9 multisig](https://explorer.metis.io/address/0xe272dAe29dfE0fB36755D20993716D6142055E3f).

## IV - Aave V3 Specific Parameters

We suggest tentative parameters contingent on resolving the critical access control flaw.

| Parameter                 | Recommendation |
|---------------------------|----------------|
| Isolation Mode            | No               |
| Emode                     | Enabled for METIS tokens  |
| Borrowable                | Yes               |
| Borrowable in Isolation   | No               |
| Collateral Enabled        | No               |
| Stable Borrowing          | No               |
| Supply Cap                | 4,000 (1/3 of available liquidity)              |
| Borrow Cap                | 400 (1/10 of supply cap)               |
| Debt Ceiling              | NA               |
| LTV                       | 30%               |
| LT                        | 40%               |
| Liquidation Bonus         | 10%               |
| Liquidation Protocol Fee  | 10%               |
| Reserve Factor            | 15%               |
| Base Variable Borrow Rate | 0%               |
| Variable Slope 1          | 7%               |
| Variable Slope 2          | 300%               |
| Uoptimal                  | 45%               |

#### Note: This assessment follows the LLR-Aave Framework, a comprehensive methodology for asset onboarding and parameterization in Aave V3. This framework is continuously updated and [available here](https://github.com/llama-risk/aave-research/blob/main/frameworks/aave_v3_framework.md).
