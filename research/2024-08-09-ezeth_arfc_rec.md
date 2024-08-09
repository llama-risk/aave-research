# Summary

LlamaRisk expressed reservations regarding integrating ezETH as collateral in the Aave V3 Lido Instance. This position aligns with the Lido market's objectives, initially understood as risk isolation, enabling more aggressive looping parameters. 

The Liquid Restaking Token (LRT) ecosystem, including ezETH, presents a significantly higher risk profile than wstETH. This proposal may deviate from the goal of risk isolation, and depositors should be aware of the additional risks associated with LRTs like ezETH. The absence of EigenLayer slashing mechanisms has led to LRT protocols onboarding numerous Actively Validated Services (AVSs) without immediate repercussions. However, the potential implementation of slashing protocols necessitates a comprehensive re-evaluation of LRT use cases as collateral.

Notwithstanding these concerns, a viable path exists for the safe integration of ezETH, either within the main or Lido instance. It's worth highlighting that Renzo ezETH has made significant progress since our last report, namely enabling withdrawals and on-chain governance processes — although governance remains centralized.

# Collateral Risk Assessment

## 1. Asset Fundamental Characteristics

### 1.1 Asset

ezETH is an ERC20 repricing token that maintains a soft peg to ETH, with its exchange rate against ETH incrementally appreciating as rewards accumulate. It is collateralized by a portfolio of staked Ethereum and select Liquid Staking Derivatives (LSDs), specifically WBETH and stETH. The yield is derived from two primary sources: the native Ethereum staking rewards and the re-staking incentives provided by secured Active Validator Sets (AVSs) through the EigenLayer protocol. Renzo imposes a 10% fee on all accrued rewards.

Despite mentioning plans to expand LSD coverage in our first report, Renzo currently accepts only WBETH and stETH as supported Liquid Staking Derivatives, which remain the only accepted options. The minting mechanism is based on ezETH's book value and underlying re-staked collaterals. The ezETH exchange rate is calculated using the ETH-equivalent value of assets involved, the total ETH value in the protocol, and ezETH's circulating supply. For LSDs, using their protocols' internal exchange rates rather than market rates provides more stability to the ezETH/ETH exchange rate, reducing risks of depegs and liquidations.

On-chain analysis shows that value locked is predominantly in WETH, with only marginal amounts of wBETH and stETH. Only stETH deposits are limited to 50k and currently standing at 6.3k as of August 8th, 2024.

### 1.2 Architecture

#### Overview

The deposit and exchange process mechanics vary slightly depending on whether a native ETH or an LSD is deposited. Native ETH deposits must first be staked by spinning up validators through select node operators before re-staking into EigenLayer, whereas LSD deposits can be directly re-staked. The deposit of stETH is limited to 50k and is currently filled up to 5.9k, whereas WBETH and ETH deposits are uncapped. The Renzo Protocol also provides a cross-chain feature, enabling the restaking of native ETH from partnered chains through Chainlink's Cross-Chain Interoperability Protocol (CCIP), which broadens the utility and accessibility of ezETH.

![image|1904x696](upload://5JNlHuevEOT5q5zBUpVhkrkc8D7.png)
Source: [docs.renzoprotocol.com/docs](https://docs.renzoprotocol.com/docs/renzo/understanding-liquid-restaking)

#### Enabled withdrawals

Users can now redeem their ezETH for ETH, WBETH, and stETH thanks to [withdrawal buffers](https://etherscan.io/address/0x5efc9D10E42FB517456f4ac41EB5e2eBe42C8918) that are replenished hourly through staking rewards, unstaked assets, and new deposits. As of Monday, February 5, 2024, there are 190 WBETH and close to 0 stETH in the contract's buffer. 

It is important to note that no LSD withdrawals are possible if the buffers are empty and that queued withdrawals are only available for native ETH. Queued withdrawals work on a first-come, first-served basis (FIFO), meaning that the unstaked assets will be allocated to the earliest withdrawal requests and then the subsequent ones. Furthermore, queued (ETH) withdrawals have priority over the buffer replenishing process, meaning that unstaked assets will first be allocated to ongoing withdrawal requests and then replenish the buffers.

In addition to the time needed for LSD buffer replenishment or ETH unstaking from Ethereum consensus and EigenLayer or Symbiotic, all withdrawals are subject to a 3-day cooldown period, regardless of the underlying asset. This waiting period, set to increase to 7 days once EigenLayer enables slashing, allows the Renzo protocol to detect potential issues and prevent front-runners from taking advantage of unfair ezETH exchange rates during slashing events. The ezETH exchange rate is calculated twice: at withdrawal initiation and finalization, with the lower rate applied. While these added delays may impact ezETH peg stability by slowing arbitrage opportunities, we consider them a necessary precaution.

### 1.3 Tokenomics

REZ token statistics as of August 7, 2024:
- 10,000,000,000 total supply
- 1,150,000,000 circulating supply
- $39.7m market cap

Renzo introduced the REZ governance token on April 30, 2024, through the first TGE event called *Season1*, where 7% of the total supply was distributed linearly to ezPoint holders. REZ can be staked for additional rewards, but it is not necessary to vote on governance proposals. However, it can be delegated to others. The allocation of REZ to large holders such as investors and core contributors is subject to various vesting schedules, ensuring the long-term participation of key stakeholders.

According to the documentation, this governance token will vote on various aspects of the protocol, including risk management, collateral assets, whitelisted operators and AVSs, and treasury allocation. For now, no proposals discussed in the [forum](https://gov.renzoprotocol.com/latest) have been escalated to a vote on [Snapshot](https://snapshot.org/#/renzogovernance.eth/), as the only topics on the forum are REZ delegate pitches and a single proposal for strengthening community engagement and rewards.

## 2. Market Risk

### 2.1 Liquidity

As of August 6, 2024, Renzo ezETH is supported on many DEXs, including but not limited to:

- [Thruster](https://app.thruster.finance/analytics#pool-table): $26.88m across two ezETH/WETH pools
- [Kim](https://app.kim.exchange/): $7.02m of TVL in [ezETH/ETH](https://app.kim.exchange/pools/v4/0xd9a06f63e523757973ffd1a4606a1260252636d2) 
- [Nile](https://www.nile.build/liquidity): $5.83m in [ezETH/ETH](https://www.nile.build/manage/v1/0xa9a1fb9f6664a0b6bfb1f52724fd7b23842248c5) pool and in another [ezETH/ETH](https://www.nile.build/liquidity/v2/0x6ba5ccc757541851d610ecc8f8ac3714b5f95314) pool
- [BalanceV2](https://app.balancer.fi/#/trade): $26.63m in [ezETH/ETH](https://app.balancer.fi/#/ethereum/pool/0x596192bb6e41802428ac943d2f1476c1af25cc0e000000000000000000000659) and $6.80m in [ezETH/weETH/rswETH](https://app.balancer.fi/#/ethereum/pool/0x848a5564158d84b8a8fb68ab5d004fae11619a5400000000000000000000066a) pool
- [Camelot](https://app.camelot.exchange): $1.04m in [ezETH/ETH](https://app.camelot.exchange/pools/0xaA45265A94C93802BE9511E426933239117E658f) pool

Paraswap, a DeFi aggregator, indicates that 2,124 ezETH ($5.5m as of August 9, 2024) can be liquidated within a 7.5% price impact. It's important to note that this measure follows the Yen carry trade unwind on August 5, 2024, significantly reducing available liquidity on secondary markets. These abnormal conditions may not be representative of typical market circumstances.

![image|427x488](upload://hLp2p4E5zTBaFAkU9OoJvy4JHSo.png)
Source: [Paraswap](https://app.paraswap.io/#/0xbf5495efe5db9ce00f80364c8b423567e58d2110-0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE/2930/SELL?version=6.2&network=ethereum) (August 9th, 2024)

### 2.2 Volatility

Since our first report on May 24, 2024, Renzo protocol has implemented a withdrawal feature for native ETH and the supported LSDs WBETH and stETH. Consequently, the ezETH peg to its theoretical book value has significantly improved, reaching a value slightly below the expected one.

A significant event that affected the ezETH peg in the past was the disclosure of the REZ tokenomics, which at the time caused a lot of disappointment from token holders and led to them exiting their position on secondary markets. Because withdrawals were not enabled at the time, this caused a significant depeg of ezETH which reached up to -78% on some trading venues.

<iframe width="400" height="400" src="https://dune.com/embeds/3966228/6673999/"></iframe>

Source: [Dune](https://dune.com/queries/3966228) query forked from [@Henrystats](https://dune.com/Henrystats)

Like other LSD/LRT, ezETH depegged to the downside following the unwinding of the Yen carry trade on Monday, August 5, 2024. This was due to market-wide liquidations that took place on-chain, which consumed all available liquidity on DEXs. This depeg is expected to correct itself as on-chain liquidity replenishes.

### 2.3 Growth

After reaching a plateau at around 1.1m ETH-equivalent on April 24th, 2024, the TVL then started to decrease following the activation of withdrawals in mid-June 2024, and seems to have now stabilized at around 550k ETH-equivalent. We can also see that the TVL of pzETH, an LRT that is based on Symbiotic, has been picking up since the end of June 2024. Renzo ezETH remains the second-largest LRT by TVL, behind EtherFi weETH.

<iframe width="400" height="400" src="https://dune.com/embeds/3973328/6686422/"/></iframe>

Source: [Dune](https://dune.com/queries/3334134/5585650), August 8th, 2024

## 3. Technological Risk

### 3.1 Smart Contract Risk

At the time of our first report, Renzo only provided a single audit from [Halborn](https://github.com/HalbornSecurity/PublicReports/blob/master/Solidity%20Smart%20Contract%20Audits/Renzo_Protocol_EVM_Contracts_Smart_Contract_Security_Assessment_Report_Halborn_Final.pdf) (November 29, 2023). Three additional audits have been performed since then:

- [Halborn](https://github.com/Renzo-Protocol/contracts-public/blob/master/Audit/Halborn_Renzo_Protocol_Withdrawals_Smart_Contract_Security_Assessment_Report.pdf) (May 22, 2024) specifically for the withdrawal feature: 3 critical issues, two high issues, one medium issue.
- [Halborn](https://github.com/Renzo-Protocol/contracts-public/blob/master/Audit/Halborn_Renzo_REZ_Smart_Contract_Security_Assessment_Report_Halborn_Final.pdf) (April 24, 2024) specifically for the REZ staking feature: 1 informational finding.
- [SigmaPrime](https://github.com/Renzo-Protocol/contracts-public/blob/master/Audit/Sigma_Prime_Renzo_Restaking_Security_Assessment_Report_v2_1.pdf) (June 2024): 1 critical issue, five high issues, and three medium issues. All were either fixed or dismissed.

All findings were addressed through justification or remediation. The SigmaPrime audit revealed critical issues potentially risking significant user funds. Given the protocol's >$1b TVL, earlier detection of these issues through more frequent audits during initial deployment would have been prudent. Notably, these recent audits now cover the cross-chain interoperability feature, addressing a gap identified in our previous report.

The Renzo Protocol has also been running a [bug bounty with Immunefi](https://immunefi.com/bug-bounty/renzoprotocol/information/#top) since December 14, 2023, with a maximum bounty of $250,000. This maximum amount is much lower than the recommended 10% of the TVL. Notably, the bounty does not cover the cross-chain interoperability contract *xRenzoDeposit*. More details can be found at Immunefi.com.

### 3.2 Price Feed Risk

ezETH utilizes a [Chainlink oracle](https://data.chain.link/feeds/ethereum/mainnet/ezeth-eth), available on multiple L2 networks. The oracle is configured with a 0.5% deviation threshold and a 24-hour heartbeat. The system employs 16 oracles, with each price aggregation requiring responses from at least 11 of them.

### 3.3 Dependency Risk

ezETH, like other Liquid Restaking Tokens (LRTs), integrates with EigenLayer to secure Active Validator Sets (AVSs) and generate additional yield for token holders. While EigenLayer's smart contract risk is inherent, Renzo claims to select node operators and AVSs carefully. Renzo aims to secure numerous AVSs, as EigenLayer's slashing and reward mechanisms are not yet operational. However, once activated, a thorough reassessment of secured AVSs will be crucial to ensure well-defined slashing conditions that align with the protocol's risk profile and maintain a positive risk-adjusted yield for token holders.

Renzo Protocol uses Connext Network and Chainlink's CCIP for native cross-chain restaking on supported L2s and alternative L1s. Users can obtain xezETH without migrating funds to L1. While this introduces limited risks to the core L1 system, xezETH minters face potential slippage due to ezETH price reporting via CCIP and bridge-related inflation attacks. Notably, the `xRenzoDeposit` contract allows both CCIP and the contract owner to update the ezETH price, the latter through the `updatePriceByOwner` function.

Renzo previously relied on a Chainlink oracle for stETH and a centralized oracle operated by Binance for WBETH. The Binance-operated oracle presented a significant centralization risk, potentially exposing the protocol to exploitation. It's important to note that the WBETH oracle has not been updated since our initial report. Consequently, ezETH remains vulnerable to the price manipulation attack that [we previously demonstrated](https://www.llamarisk.com/research/collateral-risk-ezeth).

## 4. Counterparty Risk

### 4.1 Governance and Regulatory Risk

Although the REZ governance token's distribution has started, its governance utility remains limited. [Renzo's governance forum](https://gov.renzoprotocol.com/latest) currently only contains delegate pitches and [a single governance proposal](https://gov.renzoprotocol.com/t/rp-1-renzo-amore-strengthening-community-engagement-and-rewards/35) that has not been escalated to a [snapshot.org](https://snapshot.org/#/renzogovernance.eth/) vote yet. According to the current snapshot.org parameters for the Renzo space, the execution of proposals is off-chain for now, meaning that the team remains the ultimate arbiter regarding the protocol's governance. Therefore, Renzo ezETH remains centralized.

### 4.2 Access Control Risk

We identified several important wallets:
- [EOA A](https://etherscan.io/address/0xAdef586efB3287Da4d7d1cbe15F12E0Be69e0DF0): canceller and executor of [Timelock A](https://etherscan.io/address/0x81f6e9914136da1a1d3b1efd14f7e0761c3d4cc7)
- [EOA B](https://etherscan.io/address/0x64E968003c934F8d7Ad9a4e30F48EE8e2409baE6): beacon chain deposit address
- [EOA C](https://etherscan.io/address/0x3b8c27038848592a51384334d8090dd869a816cb): offchain service
- [EOA D](https://etherscan.io/address/0x87f9693dffbc20db8581304c092f84f4576c09e9): L2 price oracle
- [EOA E](https://etherscan.io/address/0x19d74871a530c97065d95278223e8b7a7cd5ba27): emergency pauser
- [Timelock A](https://etherscan.io/address/0x81f6e9914136da1a1d3b1efd14f7e0761c3d4cc7): 3-day delay
- [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A): 3/5 threshold, proposer and admin of [Timelock A](https://etherscan.io/address/0x81f6e9914136da1a1d3b1efd14f7e0761c3d4cc7).
- [Multisig B](https://etherscan.io/address/0xd22fb2d2c09c108c44b622c37f6d2f4bc9f85668): 3/5 threshold, contains the DAO treasury

Contract upgrades are controlled by [Timelock A](https://etherscan.io/address/0x81f6e9914136da1a1d3b1efd14f7e0761c3d4cc7) with a 3-day delay with the following role assignment:
- CANCELLER_ROLE: [EOA A](https://etherscan.io/address/0xAdef586efB3287Da4d7d1cbe15F12E0Be69e0DF0)
- EXECUTOR_ROLE: [EOA A](https://etherscan.io/address/0xAdef586efB3287Da4d7d1cbe15F12E0Be69e0DF0)
- PROPOSER_ROLE: [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A)
- TIMELOCK_ADMIN_ROLE: [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A)

Renzo protocol also uses a role-based access control system comprised of the following roles and assignations:
- BRIDGE_ADMIN: [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A)
- DEFAULT_ADMIN_ROLE: [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A)
- DEPOSIT_WITHDRAW_PAUSER: [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A) and [EOA E](https://etherscan.io/address/0x19d74871a530c97065d95278223e8b7a7cd5ba27)
- EIGEN_LAYER_REWARDS_ADMIN: none
- EMERGENCY_WITHDRAW_TRACKING_ADMIN: [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A)
- ERC20_REWARD_ADMIN: none
- NATIVE_ETH_RESTAKE_ADMIN: [EOA B](https://etherscan.io/address/0x64E968003c934F8d7Ad9a4e30F48EE8e2409baE6) and [EOA C](https://etherscan.io/address/0x3b8c27038848592a51384334d8090dd869a816cb)
- OPERATOR_DELEGATOR_ADMIN: [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A)
- ORACLE_ADMIN: [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A)
- PRICE_FEED_SENDER: [EOA D](https://etherscan.io/address/0x87f9693dffbc20db8581304c092f84f4576c09e9)
- RESTAKE_MANAGER_ADMIN: [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A)
- RX_ETH_MINTER_BURNER: [withdrawal contract](https://etherscan.io/address/0x5efc9D10E42FB517456f4ac41EB5e2eBe42C8918) and [deposit contract](https://etherscan.io/address/0x74a09653A083691711cF8215a6ab074BB4e99ef5)
- TOKEN_ADMIN: [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A)
- WITHDRAW_QUEUE_ADMIN: [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A)

Although numerous roles were created, most of them are assigned to [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A). Ideally, roles should be split according to privilege levels and assigned to different multisig wallets with gradually increasing security requirements (threshold and eventually timelock).

We also note that the DEFAULT_ADMIN_ROLE role is still assigned to [Multisig A](https://etherscan.io/address/0xD1e6626310fD54Eceb5b9a51dA2eC329D6D4B68A) without a Timelock, meaning that the multisig could change the assignment of roles instantly. Notably, the RX_ETH_MINTER_BURNER role could be assigned to another wallet which would be able to mint ezETH and extract the collaterals from the protocol at the expense of Renzo's users.

**Note**: This assessment follows the LLR-Aave Framework, a comprehensive methodology for asset onboarding and parameterization in Aave V3. This framework is continuously updated and [available here](https://github.com/llama-risk/aave-research/blob/main/frameworks/aave_v3_framework.md).
