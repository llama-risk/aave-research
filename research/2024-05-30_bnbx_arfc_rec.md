## Recommendation

Based on our analysis, LlamaRisk recommends onboarding BNBx as a collateral asset on Aave V3 BNB Chain with conservative parameters, which as been jointly discussed and will be provided by @ChaosLabs. While BNBx has maintained a consistent presence since its launch in October 2023, its total value locked (TVL) has suffered a significant decline, over 90% from its all-time high of over 65k BNB in October 2022. Several risk factors have been identified that contribute to our recommendation:

1. **Concentration Risk**: A significant portion of BNBx tokens is held in the SwissBorg custodial wallet. Operational issues with SwissBorg could lead to a sell-off, potentially destabilizing the BNBx market.
2. **Validator Selection Opacity**: The process for selecting validators to stake BNB needs to be more transparently disclosed.
3. **Unstaking Cooldown**: The 7-15 day unstaking period may create selling pressure on secondary markets, as users cannot quickly exit their positions in response to market conditions.

Despite these concerns, BNBx liquidity on DEXs appears sufficient for current market conditions, with most liquidity concentrated in BNBx/BNB pairs on Thena, Wombat, and Ellipsis Finance, allowing for swaps of 1,000 BNBx to BNB with sub 1% slippage.

## Introduction

Stader's BNBx is a liquid staking derivative launched in August 2022 that enables users to stake their BNB tokens and participate in the validation process on the BNB Smart Chain. The protocol offers a variety of staking solutions across multiple blockchain networks, most prominently ETHx on Ethereum mainnet (our [initial assessment](https://hackmd.io/@PrismaRisk/ETHxAddendum) and [recent update](https://hackmd.io/@PrismaRisk/ETHx)). On the BNB Smart Chain, user BNB deposits are exchanged for BNBx tokens, creating a liquid representation of staked assets. The staked BNB is then allocated to several validators, generating staking rewards. This accrued value, reflected in the increasing exchange rate of BNBx, allows users to earn staking rewards directly.

## Background

### BNB Chain Hybrid Consensus Model

The BNB Chain comprises two interoperable blockchains: the Binance Beacon Chain (BC) and the Binance Smart Chain (BSC). The BC is being phased out, with its functionalities absorbed into the BSC through the "[BNB Chain Fusion](https://www.bnbchain.org/en/bnb-chain-fusion)" process to consolidate the ecosystem.

Stader uses the BSC chain, powered by a [hybrid consensus model](https://www.bnbchain.org/en/blog/a-journey-to-decentralization-validators-delegators) of Proof-of-Authority (PoA) and Delegated-Proof-of-Stake (DPoS). PoA designates permissioned validators to decide block transactions, while DPoS allows stakers to delegate their stake to their chosen validator. This consensus system prioritizes high availability and performance while providing limited decentralization. The BSC consensus consists of 56 validators selected by decreasing order of total stake (own stake of 10,000 BNB plus delegated stake). According to the documentation:
> The validator set is determined by a staking module built on the BNB Beacon Chain for the BNB Smart Chain and propagated daily at 00:00 UTC from BC to BSC via Cross-Chain communication.

40 validators are *active*, while 16 act as backup. [BSC validators](https://bscscan.com/validators) must stake at least 10,000 BNB and be among the top 40 by total stake. Elected validators are renewed every 24 hours based on the total stake and propose blocks cyclically, similar to [Ethereum's clique signing](https://geth.ethereum.org/docs/tools/clef/clique-signing) consensus.

The limited validator set reduces network overhead, allowing for a faster 3-second block time compared to Ethereum's 12 seconds. However, this limits decentralization. The large 150 million gas block size (compared to Ethereum's 30 million) also allows higher transaction throughput but requires bigger hardware, further limiting decentralization. 

### Slashing

Like in other PoS chains, Binance Chain validators are penalized if they don't perform as expected — a condition known as [slashing](https://docs.bnbchain.org/docs/validator/bc-slashing/#slashing-1). Validators can be slashed for three different reasons: [Inavailability](https://docs.bnbchain.org/docs/validator/overview/#loss-for-offline-slash), [Double Signing](https://docs.bnbchain.org/docs/validator/overview/#loss-for-double-sign-slash) and [Malicious Vote](https://docs.bnbchain.org/docs/validator/overview/#loss-for-malicious-vote-slash). Inavailability is a weak penalty inflicted upon offline validators, with a 50 BNB penalty taken from the validator's stake. In addition, if the validator is offline for more than 150 blocks within 24 hours, it will be in jail for two days, meaning it won't be able to validate during that time. Double signing and malicious voting are much more serious offenses that are punished by taking 1,000 BNB from the validator's stake.

![image|2000x544](upload://yOLBKcoXEvlBmElXDqq2ej2rKKy.png)
Source: [Etherscan](https://bscscan.com/advanced-filter?fadd=0x0000000000000000000000000000000000001001&tadd=0x0000000000000000000000000000000000001001&mtd=0xc96be4cb%7eSlash)

As the above graph shows, some validators are often in jail for being offline. In practice, this is true for validators whose stakes are some of the lowest, meaning they are not selected to propose blocks. To check if a validator has ever been banned for either a Double Signing or Malicious Vote, we look at the *felony* event on the *ValidatorSet* contract on [bscscan](https://bscscan.com/advanced-filter?fadd=0x0000000000000000000000000000000000001000&tadd=0x0000000000000000000000000000000000001000&mtd=0x35409f7f%7eFelony). We found three events, all associated with failed transactions, meaning that no validator has ever been slashed for those reasons. 

## System Architecture

### Mint and burn mechanisms

Stader's BNBx utilizes a mint and burn mechanism for staking on the BNB Chain. Users deposit BNB and receive equivalent BNBx tokens staked with validators. The staking rewards, minus a 10% fee from Stader, are reflected in the BNB/BNBx exchange rate. Allocation of BNB to the validators is typically automated, but this process has been halted and is currently manual due to the upcoming BNB chain fusion.

To unstake, users submit a request through the interface, subject to a cooldown mechanism. Per BNB network rules, unstaking requests have a seven-day waiting period before BNB is unstaked and available for withdrawal, starting at UTC 00:00 the following day. Only one unstaking request per address from a validator is allowed every seven days. Stader aggregates unstaking requests over a week and submits them once per week, resulting in a maximum wait time of 15 days, including the seven-day unbonding period. After a successful unstaking request and once the release time has passed, users can withdraw their BNB to their wallets.

### Validator Set

Details on Stader's BNB Chain validator is not currently readily available to the public. Stader provided the following criteria for validator selection as of March 2024:

1. No jailing in the past 90 days
2. No more than ten slashing events in the last 24 hours
3. Inclusion of the validator should result in Stader's 7-day average APR being at least equal to the overall average APR on BNB Chain 

However, Stader mentioned that exceptions were made after March 2024 due to not all BNB validators being present on BNB Smart Chain and ongoing contract migration related to chain fusion. Once the migration is complete, Stader will adhere to the original criteria again.

The validator set as of May 28th, 2024 (source: Stader):
![image|360x432, 75%](upload://2z8xcuuVzh1UBmo7V0vhessJudu.png)

### Smart Contracts & Access controls

The BNBx contract suite is simple, with the [BNBx token](https://bscscan.com/address/0x1bdd3cf7f79cfb8edbb955f20ad99211551ba275) adhering to the ERC-20 standard. Deployment information can be found [here](https://github.com/stader-labs/bnbX/blob/main/mainnet-deployment-info.json). The [`StakeManager`](https://bscscan.com/address/0x7276241a669489e4bbb76f63d2a43bfe63080f2f) contract is responsible for handling deposits, withdrawal requests, and claiming withdrawals. Both contracts are upgradeable proxies managed by a [`TimelockController`](https://bscscan.com/address/0xD990A252E7e36700d47520e46cD2B3E446836488). The current minimum delay for the timelock is three days, and the proposer role is held with a [3/5 multisig](https://bscscan.com/address/0xb866E12b414d9f975034C4BA51498E6E64559a4c) with the following signers:

* Key 1: Wombat
* Key 2: Apeswap
* Key 3: Accel
* Key 4: Stader
* Key 5: Stader

#### Audits

Audits of the BNBx contracts were performed by [Halborn](https://www.staderlabs.com/docs/bnb/StaderLabs%20BnbX%20Smart%20Contrac%20Audit%20Report%20by%20Halborn.pdf) and [PeckShield](https://www.staderlabs.com/docs/bnb/StaderLabs%20BnbX%20Smart%20Contract%20audit%20report%20by%20PeckShield.pdf) (July 2022). Findings were either fixed or mitigated. Since then, the codebase has remained unchanged.

#### Bug bounty program
BNBx has an [active bounty program](https://immunefi.com/bug-bounty/staderforbnb/) with ImmuneFi offering up to $250k in rewards to individuals who discover and report bugs and vulnerabilities.

## Performance Metrics

**Key metrics (as of May 28th, 2024)**
- Circulating Supply: [25,197](https://www.coingecko.com/en/coins/stader-bnbx)
- Holders: 9,762
- Market share: 1.8% (over [1,384,517](https://www.bnbchain.org/en/staking) total bounded BNB)

### Holders

More than half of the BNBx supply is owned in the SwissBorg custodial wallet app. SwissBorg is a crypto-asset service provider authorized to operate under license No [FVT000326](https://mtr.ttja.ee/taotluse_tulemus/547618?backurl=%40juriidiline_isik_show%3Fid%3D267215) in Estonia and registration No [E2022-034](https://www.amf-france.org/en/professionals/fintech/my-relations-amf/obtain-dasp-authorisation) in France. Digital assets custody and virtual currency exchange for fiat or other digital assets are permitted.

Other large holders of BNBx include DEXs (Thena and Ellipsis) and unknown EOAs.

![image|950x456](upload://i864BBbl7u4htjSbmB1IhlOKd5c.png)
Source: [BscScan](https://bscscan.com/token/tokenholderchart/0x1bdd3cf7f79cfb8edbb955f20ad99211551ba275), May 27th, 2024

### Growth

![image|726x308](upload://7v5hDD0QDp7ZFozDb1Mh0UVHQiB.png)
Source: [Dune](https://dune.com/embeds/3181933/5313993/), May 30th, 2024

BNBx total value locked (TVL) has suffered a significant decline, over 90% from its all-time high of over 65k BNB in October 2022.

### Integrations

To determine whether BNBx is a suitable collateral type, it is essential to understand its liquidity provisions on the secondary market (DEXs). The majority of liquidity is concentrated around BNBx/BNB pairs, mostly on [Thena](https://thena.fi/pools), [Wombat](https://app.wombat.exchange/pool?chain=bsc), and [Ellipsis Finance](https://ellipsis.finance/pool). BNBx sees very little activity on DEXs, as most users prefer to unstake (with a cooldown) directly with Stader to exit their positions. 

![image|849x231, 75%](upload://dla6ACNv8cGwULf57lm4vS6mwUy.png)
Source: [Thena](https://thena.fi/pools), May 28th, 2024

![image|860x138, 75%](upload://mqtu8Rc4ITAIwVMduvcPzjvPbVt.png)
Source: [Ellipsis Finance](https://ellipsis.finance/pool), May 28th, 2024

Current liquidity allows for a swap of 1000 BNBx to BNB, with sub 1% slippage.

![image|450x414, 75%](upload://4XzwWeB0hpB0mqdgd8k3t1OtMah.png)
Source: [Thena](https://thena.fi/pools), May 28th, 2024

### Legal Commentary

The legal standing of BNBx hinges on the token qualification as a financial instrument under applicable law. The jurisdictional substance of the entity operating the protocol UI and target markets play an important role in such an evaluation because there are no uniform global securities laws. Legal acts regulating financial markets differ from country to country. The fact that the crypto asset complies with a particular legal framework does not necessarily mean it can be freely offered in another country without domestic authorizations. 

Some of the common features of financial instruments observed in different statutory rules are:

1) **Contractual Basis**: A formal agreement between the parties must delineate the rights and responsibilities tied to the financial instrument.
2) **Marketability**:
    - Transferability: Financial instruments should allow for the assignment of rights to another party through straightforward ownership transfer mechanisms.
    - Negotiability: Ownership transfer should be seamless and safeguarded against competing claims.
    - Fungibility: The object must be uniform in quality and characteristics, standardized, and available in multiple units, facilitating interchangeability.
3) **Investment Traits**: Predominantly, financial instruments are designed for investment purposes, with the primary goal being the generation of future monetary returns. This investment intent is particularly accentuated in U.S. jurisprudence where the term "investment contract" has been interpreted by the seminal Howey judgment as encompassing four elements: (1) an investment of money; (2) in a common enterprise; (3) with expectations of a profit; (4) to be derived from the efforts of others.

Our assessment of ETHx revealed that Stakeinfra Technologies Inc., incorporated in Panama, operates the protocol front-end, i.e., https://www.staderlabs.com. Without a definitive framework in Panama for regulating cryptoassets and services related to cryptoassets, the team has explored alternative approaches to ensure compliance with prevailing regulatory standards. To this end, they have conducted a legal analysis of MaticX's status using the Howey test, which duly qualified legal professionals perform. The findings of this assessment have been shared with us under a confidentiality agreement, which precludes us from disclosing specific details of the conclusions drawn.

As long as we are not served with a legal opinion dedicated to BNBx, analysis of Howey prongs in MaticX evaluation may be relevant to BNBx to the extent that the token relies on the same UI platform and protocol design.

- There appears to be a significant likelihood that the token will fulfill the "Investment of Money" prong, given that token acquisition would involve an expenditure of capital;
- The "Common Enterprise" element is likely to be circumvented;
- Although the token may have utility features, its potential use for speculative purposes aimed at profit generation cannot be disregarded. The issuance intent of the token might not be profit-oriented, yet the possibility of its use for such purposes suggests it could meet the "Expectation of Profits" criterion; 
- "Efforts of Others" prong is unlikely to be met, given the team's assertion of the project's sufficient decentralization. 

It is imperative to reconsider these interpretations, especially the fourth point, in light of evolving US legislation, particularly with the suggested definition of decentralization under [FIT21 crypto bill](https://financialservices.house.gov/news/documentsingle.aspx?DocumentID=409277). Nonetheless, if BNBx, by its design similar to that of MaticX, fails to meet all the Howey test prongs, it would likely not be classified as a security under U.S. law. However, a definitive legal opinion can only be rendered by a legal practitioner authorized to practice in the United States.

At last, BNB is currently embroiled in a [lawsuit filed by the Securities and Exchange Commission (SEC)](https://www.sec.gov/files/litigation/complaints/2023/comp-pr2023-101.pdf), which accuses Binance of operating illegally as an unregistered securities exchange, broker, and clearing agency. The SEC's allegations extend to BNB, BUSD, and a staking investment product offered on Binance.US, categorizing them as unregistered securities. As the court has yet to deliver a verdict in this matter, the legal community finds it challenging to predict the outcome, particularly in light of mixed precedents. For instance, the court found that Ripple's XRP token sales did not constitute securities offers. In contrast, in a separate case, it permitted the SEC to proceed with its lawsuit against Terraform Labs for failing to register digital currencies.

The involvement of BNB in these legal proceedings does not necessarily directly increase the risk associated with BNBx. Still, it is undoubtedly a significant factor to monitor closely and consider in future legal risk assessments.

*Rev 01: Minor corrections following clarifications received from Stader*