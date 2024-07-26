# Summary

LlamaRisk reviewed dlcBTC, a novel non-custodial wrapped Bitcoin enabling participation in EVM-based DeFi while retaining full asset control. Based on the asset maturity, we recommend postponing the onboarding of dlcBTC as collateral on Aave markets. Our research highlighted the following issues:

- **Ecosystem in infancy**: The early implementation stage of dlcBTC's technology and ecosystem development introduces uncertainties and potential vulnerabilities unsuitable for Aave integration.
- **Limited Liquidity**: dlcBTC is only present on Arbitrum, which relies on a single liquidity pool (Curve WBTC/dlcBTC), increasing the risk of bad debt during liquidation events. We do not recommend relying on permissioned merchants (minters) to perform liquidations.
- **Small User Base and Supply**: The small number of dlcBTC holders and low total supply restrict the potential user base for Aave's dlcBTC markets.
- **Centralization Concerns**: The dlcBTC protocol suffers from several centralization vectors, including a permissioned set of attestors and a blacklisting feature that could freeze the dlcBTC of an address. We also note that there is no timelock to protect against contract upgrades.
- **Stable peg**: Although we note the existence of a Chainlink dlcBTC/BTC Proof-of-Reserve oracle, the peg stability against BTC is unknown, and there is no dlcBTC/BTC price feed from a reliable source. This lack of reliable price data and the sole venue for liquidity are concerning.
- **Bug Bounty**: No bug bounty program is implemented, which we consider a showstopper for any integration with Aave moving forward.

These factors collectively present risks we do not believe are acceptable for Aave V3 markets. While the non-custodial nature of dlcBTC is promising compared to centralized alternatives like wBTC, the ecosystem requires further maturation before onboarding.

# Collateral risk assessment

### Useful Links 

Technical documentation: [DLC.Link Technical Architecture v1.1](https://docs.google.com/document/d/1fKfQxKAzvh7Zrl9OaqB82-wRrskcUGi6_R0MkfbvXos/edit?usp=sharing)
Security documentation: [DLC.Link Platform Security](https://docs.google.com/document/d/1aJACD73qJt-jajnmG874XJeb_myAVVe_f5sl1iwP0BQ/edit)
Contracts: [github.com/DLC-link/dlc-solidity](https://github.com/DLC-link/dlc-solidity)
Attestor layer source code: [github.com/DLC-link/dlc-stack](https://github.com/DLC-link/dlc-stack)
Chainlink PoR feed: [data.chain.link](https://data.chain.link/feeds/arbitrum/mainnet/dlcbtc-por)

## 1. Asset Fundamental Characteristics

### 1.1 Asset

dlcBTC is a non-custodial, wrapped representation of Bitcoin on EVM blockchains, designed to enable Bitcoin holders to participate in EVM-based DeFi protocols while maintaining full ownership and control over their assets. The protocol's design ensures that dlcBTC on EVM chains are backed on a 1:1 basis by locked BTC on the Bitcoin network, thereby supporting the theoretical dlcBTC/BTC peg of 1.

#### dlcBTC token statistics (as of July 25, 2024)

- **Circulating supply**: $1,256,557
- **Market cap**:  $1,256,557
- **Unique Holders**: 51

### 1.2 Architecture

#### Overview

The dlcBTC architecture is made of three components: special multisig wallets called Discreet Log Contracts (DLCs), a decentralized network of oracles called the Attestor layer and on-chain ERC-20 contracts that allow for the minting and burning of dlcBTC.

DLCs are multisig wallets on the Bitcoin network that allow two participants to enter an agreement to redistribute the assets according to predefined outcomes determined by a third party. DLCs look like any other multisig wallet on the Bitcoin network, which improves privacy. The third party is an *Attestor*, an off-chain service that acts as a trusted intermediary between the Bitcoin network and the EVM chain. Because of the way DLC contracts work, the funds are guaranteed to be distributed back to the participant's wallet on the Bitcoin network, regardless of any potential security breaches on EVM chains: the attestor layer cannot misappropriate the funds.

Participants wishing to lock their BTC on the Bitcoin network to obtain dlcBTC on an EVM chain are known as *Merchants*. When creating a DLC to lock their BTC, they provide the first key, and the decentralized network called the Attestor layer holds the second key. When the Attestor network detects the creation of a DLC on-chain, they inform smart contracts on EVM chains to mint new dlcBTC. Similarly, merchants wishing to redeem their dlcBTC for the locked BTC can interact with the ERC-20 contract on EVM chains to burn their dlcBTC and trigger the distribution of the locked BTC from the DLC. Merchants are permissioned entities selected by the dlcBTC team; not everyone can mint and burn dlcBTC for the underlying BTC.

#### Key components

- **DLC**: A special multisig wallet that can only pay out to the original depositor their respective shares according to a set of predefined outcomes. This alleviates the risk of fund misappropriation present in other wrapped-Bitcoin custodial solutions like wBTC.
- **Attestor Network**: A decentralized network of node operators (attestors) that monitor blockchain events, accept DLC creations, and validate EVM blockchain outcomes. The attestors work by threshold consensus, with documentation mentioning an ideal 5-of-7 threshold and nodes being run by [independent third parties](https://docs.google.com/document/d/1aJACD73qJt-jajnmG874XJeb_myAVVe_f5sl1iwP0BQ/edit#heading=h.ouokf3704lfq). The Attestor layer is operated by a permissioned set of node operators and operates off-chain.
- **Smart Contracts**: Ethereum-based contracts that manage the minting and burning dlcBTC tokens based on the Attestor layer's trusted input. 
- **Pre-signed Transactions**: The system uses pre-signed Bitcoin transactions — one for each possible DLC outcome — to ensure that even in case of a security breach, only the original depositors can receive the BTC they locked.

#### Architecture diagram

![image|1920x2605, 50%](upload://x1Z3SJfqLf4zovWge59MEwW6Jn5.jpeg)
Source: [dlcBTC mint flow](https://docs.dlc.link/tech-stack#steps-of-a-dlc:~:text=be%20added%20later.-,Steps%20of%20a%20DLC,-A%20Standard%20DLC) (July 25, 2024)

### 1.3 Tokenomics

Although the dlcBTC protocol is non-custodial and its minting process automated, it is currently not governed by a DAO and lacks a governance token. The operation of the Attestor layer and the overall direction of the protocol remain entirely in the hands of the development team. Moreover, the development team's multisig wallet aggregates additional merchants' onboarding. There is no mention of a plan to decentralize the governance process of dlcBTC through a DAO and governance token.

**Fee Structure**

As of April 3, 2024, mint and burn fees are as follows:
 
Mint Fees:
- less than 500 BTC: 0.15% (compared to wBTC: 0.16%)
- between 500 BTC and 1500 BTC: 0.10% (compared to wBTC: 0.12%)
- between 1,500 BTC and 3000 BTC: 0.07% (compared to wBTC: 0.08%)
- more than 3,000 BTC: 0.04% (compared to wBTC: 0.05%)

Burn Fees:
- less than 500 BTC: 0.20% (same as wBTC) 
- between 500 BTC and 1500 BTC: 0.15% (compared to wBTC: 0.16%)
- between 1,500 BTC and 3000 BTC: 0.10% (compared to wBTC: 0.12%)
- more than 3,000 BTC: 0.08% (compared to wBTC: 0.10%)
 
## 2. Market Risk

### 2.1 Liquidity

dlcBTC currently maintains a Total Value Locked (TVL) of $1.3 million, equivalent to less than 20 BTC. This figure is notably lower than wBTC's 154,534 BTC, primarily due to dlcBTC's recent market entry three months ago.

![image|656x164](upload://zO6aztxu74lETxO9zv8H4AXDS2m.png)
Source: [Dune](https://dune.com/embeds/3918903/6588278), July 26th, 2024

### 2.2 Volatility

Given the extremely limited supply and liquidity venues, any volatility measure would be premature and a poor indicator.

### 2.3 Exchanges

dlcBTC is supported by a single liquidity venue — a [Curve dlcBTC/WBTC pool on Arbitrum](https://curve.fi/#/arbitrum/pools/factory-stable-ng-49/deposit) with a $980k TVL. There are no liquidity venues on Ethereum mainnet.

![image|1028x400](upload://zON5YQ81rdbY3unvfXdOvY2JFFh.png)
Source: [Curve dlcBTC/WBTC pool on Arbitrum](https://curve.fi/#/arbitrum/pools/factory-stable-ng-49/deposit) (July 25, 2024)

### 2.4 Growth

Despite its recent launch, dlcBTC exhibits exponential growth in its holder base, though further observation is required to confirm this trend. The minted supply is incrementally increasing, suggesting that a select group of BTC holders is minting dlcBTC, which is subsequently distributed among many holders in the EVM ecosystem.

![image|656x315](upload://udZfjWfsHcClRCVTmLtNr449upL.png)
Source: [Dune](https://dune.com/embeds/3918904/6588281), July 26th, 2024

A notable uptick in daily transfer volume has been observed since early July 2024.

![image|656x315](upload://opdQhN2dUtH7VDyvMld4ZMqzGGv.png)
Source: [Dune](https://dune.com/embeds/3918912/6588304), July 26th, 2024

## 3. Technological Risk

### 3.1 Smart Contract Risk

#### Audits

CoinFabrik and Metatrust conducted several audits:
- [CoinFabrik](https://818995421-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F1d1QXmk0rpzxLZAKPlLL%2Fuploads%2Fbdg6C27uIcLrT1X2ZggH%2FDLC-Link%20-%20Platform%20Design%20Review.pdf?alt=media&token=29ac2e60-a452-4eb9-a9c5-34eefe8c4132) (August 2023): A design review.
- [CoinFabrik](https://818995421-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F1d1QXmk0rpzxLZAKPlLL%2Fuploads%2FJ1UxlnMfp11FQEu7fqMr%2FDLC-Link%20Audit-Final.pdf?alt=media&token=a7a4fe86-8593-47dd-82c9-9ffcbcb779e0) (October 2023): 11 findings including four critical and three high-risk.
- Metatrust ([attestor audit](https://818995421-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F1d1QXmk0rpzxLZAKPlLL%2Fuploads%2FeaKLJealFyrYPyuInioc%2FDLC.link-attestor_FINAL_1715082047003.pdf?alt=media&token=692b6c26-44c7-4988-8790-8ecb87c02086) and [contract audit](https://818995421-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F1d1QXmk0rpzxLZAKPlLL%2Fuploads%2F9pHI4oXzmF8D6R863BlN%2FDLC-link-solidity_FINAL_20240507.pdf?alt=media&token=8703ee7b-990a-415a-bc1c-f744f9da5fb0)) (May 2024): No findings.
- [Metatrust](https://818995421-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F1d1QXmk0rpzxLZAKPlLL%2Fuploads%2FvQzcdjlHiV34xqjhyVCi%2FDLC.Link%20Jul%204_FINAL_1720195281355.pdf?alt=media&token=cc0ed6e1-9348-4c90-ab6d-e699cbde19ec) (July 6, 2024): 11 findings including three medium-risk and three low-risk.

Significant findings include:
- A Remote Code Execution (RCE) exploit was made possible on the DLCManager.sol contract due to a lack of verification when registering a callback. The development team implemented verification that the provided callback address was a valid DLC UUID as a fix.
- The storage API exposed by Attestor off-chain services had no authentication, allowing anyone to read, store, and modify events and contracts. An authentication system was implemented as a fix.
- A block timestamp was used as a source of randomness to select the Attestor for a new DLC. A malicious block builder could manipulate the block timestamp and select the Attestor of a DLC. This compromises the fairness and integrity of the selection process, increasing collusion and centralization risks. The team acknowledged this issue but deemed it not critical as the contract it was found in was bound to be deprecated.

#### Code Quality

The code for the dlcBTC protocol is found in two different repositories:
- [DLC-link/dlc-stack](https://github.com/DLC-link/dlc-stack) contains the code for the off-chain services and DLC wallet. It is available under a *Business Source License* (BUSL), a non-open source license that prevents production use.
- [DLC-link/dlc-solidity](https://github.com/DLC-link/dlc-solidity) contains the code for EVM smart contracts, made available under an MIT license (open-source).

Numerous commits from different contributors can be seen, as well as Pull Requests (PR) which display a high level of engagement and transparency from contributors. The code displays professional development practices and a well-documented code base.

#### Bug Bounty Program

There is no bug bounty for the protocol underlying dlcBTC.

#### Upgradeability

On EVM chains, the dlcBTC protocol consists of two contracts: `DLCBTC.sol` and `DLCManager.sol`:
- `DLCBTC.sol` is an ERC-20 contract that can mint and burn dlcBTC tokens.
- `DLCManager.sol` acts as the main contract of the dlcBTC protocol and serves as the point of contact for the decentralized network of Attestor off-chain services.

Both `DLCBTC.sol` and `DLCManager.sol` are deployed behind a `TransparentUpgradeableProxy` whose owner is a [5/6 multisig](https://arbiscan.io/address/0x24f75096ad315Ab617a3d0f2621aC3e9D391Aa77).

### 3.2 Price Feed Risk

A [Chainlink dlcBTC/BTC Proof-of-Reserve](https://data.chain.link/feeds/arbitrum/mainnet/dlcbtc-por) price feed is available on Arbitrum. This is a specialized type of price feed that returns the dlcBTC protocol's contract balance. It does not provide information about the dlcBTC/BTC exchange rate.

Due to the fact that dlcBTC can always be burned to redeem the underlying BTC on the Bitcoin network, the dlcBTC/BTC price on the secondary market should rarely fall below 1. However, because dlcBTC minters are permissioned, a strong on-chain demand could temporarily push the dlcBTC/BTC exchange rate upward, depending on the minters' reaction time. This situation could present an arbitrage opportunity for dlcBTC minters.

### 3.3 Dependency Risk

#### Attestors

The dlcBTC protocol relies on a decentralized network of node operators (7 as of July 26, 2024) known as *Attestors*. These Attestors are currently permissioned and selected by the dlcBTC development team. Although they must undergo KYC procedures, no economic security guarantees their correct behavior.

The Attestors function like an Oracle using a threshold consensus. According to the source code, this threshold equals the number of attestors, meaning all attestors must agree for dlcBTC to be minted or burned. There is a discrepancy between the code and technical documentation, where 5-of-7 and 3-of-5 threshold mechanisms are mentioned. The documentation also specifies that all attestor nodes would initially be run by DLC.link itself, gradually being replaced by independent operators. The current status of this replacement process could not be established.

#### Merchants

Merchants are permissioned participants who can lock their BTC into a DLC multisig to mint dlcBTC on EVM chains. They are known entities selected by the dlcBTC core team and must undergo multiple KYC processes to be whitelisted. Consequently, although the dlcBTC protocol is non-custodial, it is permissioned. We also note the presence of a blacklisting feature in the *DLCManager* contract, which allows the *DLC_ADMIN_ROLE* to prevent an account from receiving or sending dlcBTC.

## 4. Counterparty Risk

### 4.1 Governance and Regulatory Risk

Upon examination of the footer on https://www.dlc.link/, a copyright notice under DLC.Link, Inc. is evident, leading to the reasonable inference that the same entity owns and operates the website, including the dlcBTC dApp.

The [FAQ section](https://www.dlc.link/faq) incorporates several self-assessment tabs addressing regulatory inquiries. Notably, it emphasizes that the BTC depositor engages in a "self-wrapping" process, locking the assets and maintaining exclusive access to BTC funds. DLC.Link asserts that dlcBTC does not constitute a security, predicated on the fact that users, specifically dlcBTC Merchants, self-wrap their own BTC while retaining self-custody. Furthermore, they contend that no scenario exists wherein DLC.Link obtains possession of users' funds, thereby precluding classification as a money transmitter.

To gain access to the dlcBTC dApp, prospective Merchants must navigate a comprehensive whitelisting procedure. This process entails submitting an application, undergoing a thorough compliance review (including KYC/KYT/AML checks), completing technical integration, and participating in training and support sessions. The business relationship is formalized by executing a Merchant Services Agreement with DLC.Link, Inc.

Below are our key findings from the agreement review:

- Custodial services are excluded from the scope of services provided.
- DLC.Link, Inc. explicitly disclaims any role as a manager or investment adviser to the Merchant and bears no obligation to elucidate or caution against any risks taken or assumed by the Merchant.
- The agreement includes a comprehensive limitation of liability clause, absolving DLC.Link of responsibility for any consequential, incidental, exemplary, punitive, special, or indirect damages.
- The onus of conducting AML/KYC procedures and identity verification for end-users rests solely with the Merchant, before facilitating any transfers of BTC or dlcBTC to or from such users.
- The Merchant provides representations, warranties, and covenants affirming that it is neither controlled by sanctioned individuals nor established or located in jurisdictions subject to international sanctions.
- The agreement places the responsibility squarely on the Merchant to ascertain whether compatible Merchant wallets satisfy all applicable requirements, laws, and regulations that the Merchant is obligated to fulfill.

The agreement is designed to support DLC's hands-off approach.Link regarding custodianship and any asserted funds management activities. The thorough counterparty checks, supported by the strict AML/KYC obligations and sanctions compliance requirements imposed on the Merchants, add extra credibility to DLC.Link's setup.

### 4.2 Access Control Risk

Two multisig wallets control the protocol:
- [Multisig A](https://arbiscan.io/address/0x24f75096ad315ab617a3d0f2621ac3e9d391aa77) with 5/6 signers required. This is a high-privilege multisig that controls critical aspects of the dlcBTC protocol.
- [Multisig B](https://arbiscan.io/address/0xaa2949c5285c2f2887abd567865344240c29d619) with 4/6 signers required. This is a lower privilege multisig.

dlcBTC relies on a role-based access control system made of the following roles:
- *DEFAULT_ADMIN_ROLE* has the highest privilege level of all contracts. It is assigned to a [multisig A](https://arbiscan.io/address/0x24f75096ad315ab617a3d0f2621ac3e9d391aa77) and can re-assign other roles. A 2-day delay is required to transfer it.
- *PAUSER_ROLE* allows the minting and burning of dlcBTC to be paused and unpaused. It is assigned to [Multisig B](https://arbiscan.io/address/0xaa2949c5285c2f2887abd567865344240c29d619).
- *DLC_ADMIN_ROLE* can set multiple parameters, including the minting and redemption fees, whitelist addresses, etc. It is assigned to [Multisig B](https://arbiscan.io/address/0xaa2949c5285c2f2887abd567865344240c29d619).

## 5. Aave V3 Specific Parameters

There are no parameter recommendations at this stage, as we recommend holding off on onboarding from both Arbitrum and Ethereum mainnet.

*Note: This assessment follows the LLR-Aave Framework, a comprehensive methodology for asset onboarding and parameterization in Aave V3. This framework is continuously updated and [available here](https://github.com/llama-risk/aave-research/blob/main/frameworks/aave_v3_framework.md).*
