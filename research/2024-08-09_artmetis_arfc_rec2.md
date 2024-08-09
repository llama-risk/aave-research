# Summary

This is the second review of the artMetis Liquid Staking Derivative (LSD) on the Metis L2 chain. [Our initial assessment](https://governance.aave.com/t/arfc-onboard-artmetis-to-aave-v3-on-metis-market/18079/2?u=llamarisk), conducted on June 28th, 2024, identified several critical vulnerabilities that necessitated remediation, leading to our recommendation against onboarding artMETIS as collateral at that time.

Following the implementation of several changes by the Artemis team, we now view artMetis as a sound collateral that can be onboarded on the Metis Aave V3 instance. More specifically, withdrawals were enabled, which restored the peg to its expected theoretical value. The EOA that had control over all contracts on the Metis L2 chain has also been replaced by a 3/5 multisig. Although we welcome the use of a multisig, adding timelocks on both L1 and L2 could further strengthen the security of the Artemis protocol.

We are, therefore, ready to recommend onboarding artMETIS and can provide parameter recommendations when a new ARFC is proposed.

*For the sake of conciseness, we only mention what has changed since our first report*

## Asset fundamentals

METIS token statistics (as of the August 7th, 2024):
- Total supply: 10,000,000
- Circulating supply: 5,686,334
- Market cap: $176,987,148
- Staked supply: 333,699 METIS (5.87% of circulating supply)
- Number of sequencers: 6

Compared to our first review, the market cap of artMETIS has decreased from $290,915,236 to $176,987,148, a 39% decrease that correlates with the overall crypto market sentiment. The staked supply of METIS has barely changed, currently standing at 333,699 METIS tokens or 5.87% of the circulating supply.

artMETIS token statistics (as of the August 7th, 2024):
- Circulating Supply: [170,933 artMETIS]([0x2583A2538272f31e9A15dD12A432B8C96Ab4821d](https://explorer.metis.io/token/0x2583A2538272f31e9A15dD12A432B8C96Ab4821d))
- Holders: [2,134 unique holders](https://explorer.metis.io/token/0x2583A2538272f31e9A15dD12A432B8C96Ab4821d/tokenholderchart)
- METIS staking share: 53.13%

The circulating supply of artMETIS has slightly decreased from 177,311 to 170,933 (-3.6%). Considering that withdrawals were enabled since our last review, such a small decrease in the circulating supply is positive and indicative of users' continued interest in the Artemis protocol. Apart from market valuation, the asset fundamentals have remained fairly stable despite adverse global market conditions.

## Withdrawals

Withdrawals are now enabled. It is a two-step process that users must first initiate by interacting with the *artMETIS Module* contract on the Metis L2 chain. At this point, artMETIS tokens are immediately burned, and the contract records a claim. Through communication with Ethereum mainnet, sufficient funds are unstaked in batches to satisfy the total amount requested by users. After a 21-day unbounded period imposed by the Metis staking consensus, funds are made available to Artemis contracts on L1, bridging the funds back to Metis L2. Then, users can finalize their withdrawal request and receive their METIS tokens back.

![image|768x350](upload://lXxciCsXkriE2ZNaVKltZGZ2S5t.png)
Source: [docs.artemisfinance.io/mechanism/architecture](https://docs.artemisfinance.io/mechanism/architecture), August 9th, 2024

Notably, Artemis does not add any delay to the withdrawal process, apart from the time it takes to bridge METIS tokens between the Ethereum L1 and Metis L2 chains.

## artMETIS/METIS Peg

![image|1039x522](upload://yXHcE40saYAuePnq8wRop3QAmI0.png)
[HerculesV3 artMETIS/WMETIS](https://app.hercules.exchange/pools/0x75A05DEa768F5a8E90227d900EC82038e4584e9a) Source: [geckoterminal.com](https://www.geckoterminal.com/metis/pools/0xfd1f58c4c05d8ed5040ee9ba7edb5cc5bf53930e?utm_campaign=livechart-btn&utm_medium=referral&utm_source=coingecko, August 9th, 2024

As expected following the activation of withdrawals, the artMETIS/METIS peg has recovered to reach a value of 1.0241 as of August 9th, 2024. This is still slightly below the theoretical peg of 1.0327 given by the [withdrawal modal for artMETIS](https://artemisfinance.io/stake). A possible reason for this is the large liquid staking APY of 107.76%, boosted by Artemis compared to the base 20% staking APY, which farmers might be constantly selling on secondary markets.

![image|295x110](upload://zgzu2jidM3iw0qQr2rzM6rM2xDD.png)
Source: [artemisfinance.io/stake](https://artemisfinance.io/stake), August 9th, 2024

## Access-control

On the Metis L2 chain, the *proxyAdmin* contract, which controls all other L2 contracts, is now controlled by a [3/5 multisig](https://explorer.metis.io/address/0xFc7FA6C1Fec55b6C501851bd8fBDfffC23a8edc0). Although a positive and much-needed development, we recommend the addition of a timelock to allow the team to prevent a malicious upgrade from going live and allow users to exit the system if they don't support the changes.
