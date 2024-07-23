# Summary

LlamaRisk supports listing weETH on Aave V3 Scroll and parameters recommended by @ChaosLabs. [Our initial assessment](https://www.llamarisk.com/research/collateral-risk-weeth) for collateral onboarding highlighted a few concerns with weETH, including absence of a DAO and centralization governance risk due to a low threshold multisig without a timelock, reliance on EigenLayer airdrop speculation for growth, potential validator risks (especially with non-KYC'd operators), and counterparty risk for node operators relying on legal agreements.

Since then, EtherFi has shown remarkable growth, reaching an ATH TVL of ~$6.8 billion while addressing some of our initial concerns. For L2 onboarding, EtherFi uses LayerZero's OFT native minting technology, which we'll examine. In this brief, we provide an update on weETH, which supports our recommendation to onboard on Scroll.

## Cross-chain bridging using LayerZero OFT

EtherFi employs LayerZero's OFT (Omnichain Fungible Token) to bridge weETH to Layer 2 networks like Scroll. This system uses native minting, where new weETH tokens are minted directly on Scroll when bridged. To maintain a consistent total supply, tokens are burned on Ethereum and minted on Scroll during transfers. The process relies on LayerZero's cross-chain messaging protocol for infrastructure. Users can bridge weETH directly without interacting with intermediate wrapped tokens. 

![image|1706x820](upload://g4g1QeKNUWjJg7JLY1gSTsTwNJF.png)
Source: [LayerZero](https://medium.com/layerzero-ecosystem/introducing-native-l2-restaking-079edaa1804a)

As of July 23, 2024, LayerZero v2 OFTs have a total value locked of over $700 million. [L2BEAT](https://l2beat.com/bridges/projects/layerzerov2oft) provides a good summary of trust assumptions and risk factors, as the security parameters of each Omnichain Fungible Token (OFT) can be changed by their developers. In weETH case, the [escrow contract](https://etherscan.io/address/0xFE7fe01F8B9A76803aF3750144C2715D9bcf7D0D) is owned by a [2/5 multisig](https://etherscan.io/address/0x2aCA71020De61bb532008049e1Bd41E451aE8AdC) and the [weETH OFT implementation on Scroll](https://scrollscan.com/address/0x01f0a31698c4d065659b9bdc21b3610292a1c506) is owned by a [3/6 multisig](https://app.safe.global/settings/setup?safe=scr:0x3cD08f51D0EA86ac93368DE31822117cd70CECA3). Other risk factors include potential theft through malicious OFT (Adapter) contract upgrades by the OApp owner, fraudulent transfers due to Executor-Verifier collusion, the critical risk from malicious security stack changes, and fund compromise if the LayerZero Multisig alters the default stack when no custom stack is set. 

## Token distribution and Liquidity

![image|819x494](upload://hs0gVfUbZlJ4ntohfP230xY2NCt.jpeg)
Source: [Etherscan](https://scrollscan.com/token/tokenholderchart/0x01f0a31698c4d065659b9bdc21b3610292a1c506), July 23rd, 2024

A large portion of weETH is held by [Mitosis](https://app.mitosis.org/) via [miweETH](https://scrollscan.com/address/0xb9ca61a6d5fa0c443f3c48ab1fbf0118964308d6), a protocol that aims to improve efficiency for asset management across multiple chains and DeFi protocols. Our review indicates that the cross-chain LP functionality still needs to be activated, with the Mitosis vault attracting deposits through its incentive (points) program. 

Other notable holders include an unknown EOA, Pencils Wrapped eETH (pweETH) from the [Pencils Protocol](https://pencilsprotocol.io/) (an auction platform and yield aggregator), and Rho weETH (rweETH) from the [Rho Protocol](https://www.rho.trading/) (a DeFi derivatives market). [LayerBank](https://scroll.layerbank.finance/bank), an unsanctioned Aave V3 fork, also has a small ($600k) amount of weETH deposited.

On the DEX side, a majority of the Liquidity is held within Ambient's [weETH/ETH pool](https://scrollscan.com/tokenholdings?a=0xaaaaAAAACB71BF2C8CaE522EA5fa455571A74106) and Nuri's weETH/ETH pool.
![image|652x100](upload://6IKjVnjYOlvIurjPPC7kD1JUQOb.png)

Source: [Ambient](https://ambient.finance/) weETH/ETH pool, July 23rd, 2024

![image|510x110](upload://4Am2q4V90Pbso5qHCbBDk2Toudd.png)
Source: [Nuri](https://www.nuri.exchange/) weETH/ETH pool, July 23rd, 2024

The current Liquidity on Nuri supports swaps of up to approximately 1,000 weETH to ETH, resulting in 8.1% slippage.

![image|519x322](upload://4rBSb1YqwW2HtEtRx9o8pAdgPia.png)
Source: [Nuri](https://www.nuri.exchange/swap?from=0x01f0a31698C4d065659b9bdC21B3610292a1c506&to=ETH), July 23rd, 2024

## Update on Market Risks

The total TVL (weETH + eETH) saw a small reduction from $6.5b to $5.6b following the second ETHFI airdrop. However, it grew to nearly $7 billion as of July 23, 2024.

![image|1011x329](upload://69vlcGVM9b10O4MWyHHdPNgy3h4.png)
Source: [DefiLlama](https://defillama.com/protocol/ether.fi?unlocks=true), July 23rd, 2024

EtherFi remains the leading LRT protocol in TVL and has managed to sustain its growth despite the first EIGEN token airdrop and the first and second waves of the ETHFI airdrop to EtherFi point holders. This helps to alleviate our fear that EtherFi's growth was inorganic and made of mostly temporary airdrop farmers, which could have increased the volatility of its Liquidity.

## Update on Access Control

Our audit of EtherFi's smart contracts confirm the implementation of a [three-day timelock](https://etherscan.io/address/0x9f26d4c958fd811a1f59b01b86be7dffc9d20761) contract. EtherFi uses multiple multisigs:
- [Multisig A](https://etherscan.io/address/0xcdd57D11476c22d265722F68390b036f3DA48c21) (4/7): Manages most contracts, including the timelock's executor, canceller, and proposer roles
- [Multisig B](https://etherscan.io/address/0xF155a2632Ef263a6A382028B3B33feb29175b8A5) (2/6): legacy multisig wallet
- [Multisig C](https://etherscan.io/address/0x2aCA71020De61bb532008049e1Bd41E451aE8AdC) (2/5): LoyaltyPointsMarketSafe only
- [Multisig D](https://etherscan.io/address/0xCEA8039076E35a825854c5C2f85659430b06ec96) (4/6): Liquid Vault only
- [Multisig E](https://etherscan.io/address/0x7A6A41F353B3002751d94118aA7f4935dA39bB53) (3/6): ETHFI distributor

| Contract | Owner |
|----------|-------|
| [`Address Provider`](https://etherscan.io/address/0x8487c5F8550E3C3e7734Fe7DCF77DB2B72E4A848) | Multisig A, via timelock |
| [`Early Adopter Pool`](https://etherscan.io/address/0x7623e9dc0da6ff821ddb9ebaba794054e078f8c4) | Multisig B |
| [`Auction Manager`](https://etherscan.io/address/0x00C452aFFee3a17d9Cecc1Bcd2B8d5C7635C4CB9) | Multisig A, via timelock |
| [`Staking Manager`](https://etherscan.io/address/0x25e821b7197B146F7713C3b89B6A4D83516B912d) | Multisig A, via timelock |
| [`Etherfi Nodes Manager`](https://etherscan.io/address/0x8B71140AD2e5d1E7018d2a7f8a288BD3CD38916F) | Multisig A, via timelock |
| [`BNFT`](https://etherscan.io/address/0x6599861e55abd28b91dd9d86A826eC0cC8D72c2c) | Multisig A, via timelock |
| [`TNFT`](https://etherscan.io/address/0x7B5ae07E2AF1C861BcC4736D23f5f66A61E0cA5e) | Multisig A, via timelock |
| [`eETH`](https://etherscan.io/address/0x35fA164735182de50811E8e2E824cFb9B6118ac2) | Multisig A, via timelock |
| [`WeETH`](https://etherscan.io/address/0xCd5fE23C85820F7B72D0926FC9b05b43E359b7ee) | Multisig A, via timelock |
| [`WithdrawRequestNFT`](https://etherscan.io/address/0x7d5706f6ef3F89B3951E23e557CDFBC3239D4E2c) | Multisig A, via timelock |
| [`Liquidity Pool`](https://etherscan.io/address/0x308861A430be4cce5502d0A12724771Fc6DaF216) | Multisig A, via timelock |
| [`Membership Manager`](https://etherscan.io/address/0x3d320286E014C3e1ce99Af6d6B00f0C1D63E3000) | Multisig A, via timelock |
| [`Membership NFT`](https://etherscan.io/address/0xb49e4420eA6e35F98060Cd133842DbeA9c27e479) | Multisig A, via timelock |
| [`Node Operator Manager`](https://etherscan.io/address/0xd5edf7730ABAd812247F6F54D7bd31a52554e35E) | Multisig A, via timelock |
| [`ETHFI`](https://etherscan.io/address/0xFe0c30065B384F05761f15d0CC899D4F9F9Cc0eB) | Gov contract, not owned or upgradeable |
| [`Treasury`](https://etherscan.io/address/0x6329004E903B7F420245E7aF3f355186f2432466) | Multisig A, via timelock |
| [`LoyaltyPointsMarketSafe`](https://etherscan.io/address/0x3165542a27D40fBE0DAd050614180F01a4f4eE24) | Multisig C |
| [`Liquifier`](https://etherscan.io/address/0x9ffdf407cde9a93c47611799da23924af3ef764f) | Multisig A, via timelock |
| [`EtherFiOracle`](https://etherscan.io/address/0x57AaF0004C716388B21795431CD7D5f9D3Bb6a41) | Multisig A, via timelock |
| [`EtherFiAdmin`](https://etherscan.io/address/0x0EF8fa4760Db8f5Cd4d993f3e3416f30f942D705) | Multisig A, via timelock |
| [`EtherFiTimelock`](https://etherscan.io/address/0x9f26d4C958fD811A1F59B01B86Be7dFFc9d20761) | Multisig A, via timelock |
| [`Liquid Vault`](https://etherscan.io/address/0xeA1A6307D9b18F8d1cbf1c3Dd6aad8416C06a221) | Multisig D |

## Update on Governance and Reward System

Etherfi launched the ETHFI token in March 2024. A [3/6 multisig](https://etherscan.io/address/0x7A6A41F353B3002751d94118aA7f4935dA39bB53) received 100% of the ETHFI supply and began distributing funds to various wallets according to the [documented allocation schedule](https://etherfi.gitbook.io/gov/ethfi-allocations).

The next governance development phase, "Phase 1 - Full governance deployment," is planned for the coming months. This phase will expand voter involvement in Etherfi's governance by deploying a governor and granting access to Etherfi's protocol and treasury.

Holders can vote on DAO proposals via [Snapshot](https://snapshot.org/#/etherfi.eth) or delegate their votes. A multisig committee implements changes, handles emergency actions, and ensures proposals align with Foundation objectives, with veto power. Anyone can propose, but a quorum of 1m ETHFI is required. Approved proposals are executed off-chain by the multisig committee. The system remains centralized until on-chain, trustless proposal deployment is introduced.

ETHFI staking is available through the [Etherfi dApp](https://app.ether.fi/). It accumulates loyalty points (6.5 points daily per staked ETHFI as of July 2024). The ETHFI vault automatically re-stakes on Karak for additional rewards. Staking is not required to vote on governance proposals; staked ETHFI can still be used to vote.

Additional resources on governance:
- Governance documentation: [etherfi.gitbook.io/gov](https://etherfi.gitbook.io/gov)
- Governance forum: [governance.ether.fi](https://governance.ether.fi/)
- Governance delegatees: [vote.ether.fi/delegates](https://vote.ether.fi/delegates)
- ETHFI dashboard: [dune.com/ether_fi/ethfi-token](https://dune.com/ether_fi/ethfi-token)

## Update on Dependencies

EtherFi relies on two primary external components: EigenLayer for restaking functionality and Obol Network for Distributed Validator Technology (DVT). While these integrations are crucial for EtherFi's operations, they also represent potential risk points in the system.

EigenLayer serves as a protocol dependency, providing the restaking infrastructure. In contrast, Obol DVT is an off-chain middleware for validators, provided "as is" and managed by node operators. 

The protocol maintains two categories of node operators: Permissioned Professional Node Operators subject to Know Your Customer (KYC) procedures and Permissioned 2 ETH Bonded Node Operators exempt from KYC requirements. This dual structure allows for a balance between professional oversight and broader participation.

Notably, Professional Node Operators rely on legal agreements rather than collateral. While this approach may streamline operations, it introduces potential counterparty risk, as the protocol's security partially depends on the enforceability of these agreements.





