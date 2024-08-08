# Summary

LlamaRisk conducted an expedited review of sFRAX as a potential collateral asset following our [December 2023 analysis](https://www.llamarisk.com/research/collateral-risk-sfrax). Most of the information from our previous report remains relevant, except that the current yield primarily comes from on-chain sources (AMO activities) rather than RWAs due to their superior yields. Our key concerns include numerous centralized dependencies in protocol operations, limited visibility into off-chain assets held by FinResPBC, and general lapses in funds management oversight, both on and off-chain.

We recognize that this proposal may generate additional utility and revenue for Aave and that the DAO may weigh Frax's operational risk against the strategic importance of this relationship. Despite the concerns we outline here, the strict parameterization for sFRAX proposed by Chaos Labs sufficiently mitigates the adverse impact of an operational failure. 

On removing FRAX from isolation mode, although FRAX's risk profile differs from Maker's DAI (FRAX's collateralization ratio stands at 95% compared to DAI's 127%), we concur with using similar parameters, notably the recently lowered LTV of 63%. 

Based on these factors, we are prepared to support the proposal.

# Collateral Risk Assessment

## 1. Asset Fundamental Characteristics

#### FRAX (ERC20)
FRAX is a US dollar-denominated stablecoin launched in 2020 with multiple use cases, including yield generation, network bridging, and leverage. Initially fractionally backed, its backing mechanism has evolved. As of August 5, 2024, the DAO self-reports a 95% collateralization ratio, excluding $103M of "locked liquidity". Notably, [Frax balance sheet](https://facts.frax.finance/frax/balance-sheet) suggests that over half of this collateral consists of FRAX itself at the time of writing.

#### sFRAX (ERC4626)
sFRAX is the yield-bearing counterpart to FRAX, enabling weekly distribution of protocol yield to stakers. It represents proportional deposits in the vault and is fully collateralized by FRAX. Yield sources are partially managed offchain by [FinResPBC](https://gov.frax.finance/t/fip-277-onboard-finrespbc-as-frax-v3s-offchain-rwa-partner/2492), a Delaware-incorporated public benefit corporation widely believed to be overseen by the [Frax core team](https://x.com/ImperiumPaper/status/1687796014084653056). AMO earnings from various on-chain activities supplement this. The strategy aims to meet or exceed Federal interest rates, though limited public information is available on off-chain yield sources.

### 1.2 Architecture

Frax is a stablecoin whose peg is dependent on four different AMOs. An AMO protocol uses preprogrammed activities to fulfill a purpose, often through market mechanisms. Frax is in its V3, and its primary AMO is Curve (see architecture diagram). Other AMOs include Fraxlend (Frax's in-house lending market), Fraxswap (a DEX using a TWAMM pricing solution), and FXB (Frax Bonds). 

#### FRAX

![image|1292x702](upload://x1G8zlkYs8grpRVxLTZkfRe79En.jpeg)
Source: FRAX's Curve AMO, taken from [Frax V3 Docs](https://docs.frax.finance/frax-v3/amos)

These AMOs build on Frax V2, which introduced more flexible AMOs, expanding upon Frax V1's singular AMO or "base stability mechanism". V1 and V2 used FXS, Frax's governance token, to reach 100% collateralization. 

In response to Terra's collapse, the Frax DAO decided to work towards full decentralization and exogenous collateral by introducing FraxGov with Frax V3. While the [FraxGov GitHub repository](https://github.com/FraxFinance/frax-governance) has been made public, the new governance system has not yet been fully implemented. LlamaRisk has been reporting on Frax's stated intention to decentralize governance [since December 2021](https://cryptorisks.substack.com/p/asset-risk-assessment-frax-finance) when they first expressed the intention to transition to fully on-chain governance in "3-6 months". 

#### sFRAX

sFRAX (Staked FRAX) is a core component in Frax v3, functioning as an ERC-4626-compliant staking vault. It distributes protocol yield to stakers weekly in FRAX stablecoins. Depositors act as lenders to FRAX, earning interest on provided funds.

![image|1600x1018](upload://gPg7nSCiLbPMi3KzNOgpG2NKO8m.png)
Source: sFRAX architecture, from [Frax's April STEP application](https://forum.arbitrum.foundation/t/frax-finance-sfrax-fxbs-step-application/23528)

The Frax Comptroller multisig manages deposits by minting FRAX through the Curve AMO and withdrawing counterparty stablecoins, which are then used for yield-generating strategies. This process reverses for withdrawals.

While the [sFRAX documentation](https://docs.frax.finance/frax-v3/sfrax) suggests yield primarily comes from RWAs and AMO activities, current allocations favor on-chain yields. The exact distribution isn't fully transparent. For accurate allocation data, refer to the FRAX [balance sheet](https://facts.frax.finance/frax/balance-sheet).

The documentation mentions an IORB rate oracle to automate the RWA and AMO deployment division, targeting the Federal Reserve's risk-free rate. However, this oracle isn't currently implemented, and the process appears to be manually managed by the Frax team. Despite [reports of collaboration with Chainlink](https://fraxfinancecommunity.medium.com/frax-finance-using-chainlink-to-bring-u-s-cpi-data-on-chain-in-support-of-the-frax-price-index-737ea893ab73), current [documentation](https://docs.frax.finance/frax-v3/sfrax) and [development repositories](https://github.com/FraxFinance/frax-solidity/tree/master/src/hardhat/contracts/Oracle) don't show evidence of its implementation.

### 1.3 Tokenomics

#### FRAX

FRAX, as an algorithmic stablecoin, has no fixed tokenomics. Its supply is managed by AMOs that mint/burn FRAX based on market conditions. The supply has remained steady at 650M after a significant decrease in September last year, partly due to V3's shift away from endogenous collateralization.

![image|1184x734](upload://bEYMm732gsW6tSsyMxQaZBkBtRa.png)
Source: FRAX supply (Coingecko), August 7, 2024

[Largest holders](https://etherscan.io/token/0x853d955aCEf822Db058eb8505911ED77F175b99e#balances) include Curve and Uniswap pools, the Frax comptroller, and the sFRAX contract.

#### sFRAX

sFRAX supply directly relates to FRAX supply. As of August 8, 2024:
- Market capitalization: $57M
- Mainnet capitalization: $50.5M
- APY: ±7.55%

Large holders include the Frax Price Index Comptroller, Fraxtal bridge, Karak restaking market, and FraxFerry bridge.

## 2. Market Risk

### 2.1 Liquidity

#### FRAX
![image|1248x398](upload://pGHvBeMeKaAxL9QVxsHOo4e6eXA.png)
Source: FRAX liquidity via DeFiLlama.com/liquidity, August 7th, 2024

FRAX has excellent on-chain liquidity, with minimal slippage up to ±$10M trades.

#### sFRAX
![image|1250x318](upload://ng3a6vWJbbFyWh5fxYsIzOZ17E4.png)
Source: sFRAX liquidity via DeFiLlama.com/liquidity, August 7th, 2024

sFRAX has poor on-chain liquidity, but FRAX's instant redeemability mitigates this issue.

### 2.2 Volatility

#### FRAX
![image|1228x612](upload://dj6Y6Os565kbBxACttrPhiQQsYp.jpeg)
Source: Frax's price history (Coingecko), August 7, 2024

FRAX has maintained its peg with no prolonged depeg events.

#### sFRAX
![image|1254x752](upload://7c7nIrdlKX28YRbuNY1lwUKGNYm.jpeg)
Source: sFRAX price (Coingecko Terminal), August 7, 2024

sFRAX has shown a slow increase in value compared to USD, as intended.

### 2.3 Exchanges

Both FRAX and sFRAX are exclusively available on DEXs. FRAX is very liquid, while sFRAX is illiquid but instantly redeemable.

### 2.4 Growth

FRAX supply has been stable for the past year. sFRAX has grown, stabilizing around $57M market cap in the past month.

![image|687x410](upload://vn81noncAC8O7duEZfrfF7IQOGP.png)
Source: sFRAX growth ([Dune](https://dune.com/queries/3174637/5299428)), August 7th, 2024

## 3. Technological Risk 

### 3.1 Smart Contract Risk

Frax has a self-managed bounty program advertised in their docs. The bounty for discovering an exploit is set at the lesser of 10% of the total potential exploit or $10M. The bounty program includes all smart contracts deployed by Frax Deployer.

#### FRAX

[Frax's system components have been audited](https://docs.frax.finance/other/audits) at various stages:
- V1: Audited in 2020 and 2021
- AMOs (FraxLend, FraxSwap): Audited in 2022
- FrxGov (V3): Audited in 2023
- Latest audit (2024): Conducted by Frax Security Cartel, but didn't include FRAX modules

Most audits were conducted by Trail of Bits, a reputable firm. However, FRAX's current system lacks a comprehensive audit.

#### sFRAX

sFRAX contracts are unaudited, though the contract is relatively simple, primarily handling deposits and proportional reward allocation.

### 3.2 Price Feed Risk

#### FRAX

FRAX uses a Chainlink USD price oracle, already implemented in [FRAX's Aave V3 market](https://etherscan.io/address/0x45D270263BBee500CF8adcf2AbC0aC227097b036). The feed has a 1% deviation threshold and hourly updates. Chainlink categorizes this as "Medium market risk".

#### sFRAX

As an ERC4626 vault representing FRAX share price, sFRAX's price can be derived from the FRAX/USD feed multiplied by the share price, limiting additional risk.

### 3.3 Dependency Risk

#### FRAX

Frax is a stablecoin built on the ERC20 token standard, using a modified ERC20 contract. It has various dependencies, the most significant being the Algorithmic Market Operations (AMO) Protocols. [AMOs](https://docs.frax.finance/frax-v3/amos) in FRAX Finance are autonomous smart contracts designed to implement preprogrammed monetary policies into specific subprotocols, either internally within the Frax Protocol ecosystem or externally with other protocols like Curve.

The [Curve AMO](https://etherscan.io/address/0x49ee75278820f409ecd67063D8D717B38d66bd71) mints FRAX stablecoins into approved Curve liquidity pools and can withdraw and burn FRAX to maintain exchange rates. The [Fraxlend AMO](https://etherscan.io/address/0xf6E697e95D4008f81044337A749ECf4d15C30Ea6) operates within the Fraxlend subprotocol, allowing anyone to lend FRAX stablecoins and earning interest from these loans. The [Fraxswap TWAMM AMO](https://etherscan.io/address/0x629C473e0E698FD101496E5fbDA4bcB58DA78dC4) uses time-weighted average market maker orders to buy or sell collateral over extended periods, helping to expand or contract the FRAX balance sheet.

#### sFRAX

sFRAX is dependent on FinresPBC as the facilitator for off-chain strategies. FinresPBC is [not bankruptcy remote](https://forum.arbitrum.foundation/t/frax-finance-sfrax-fxbs-step-application/23528), and its operations are largely opaque. Since [FIP308 onboarded Centrifuge](https://snapshot.org/#/frax.eth/proposal/0x63c1816b90e9b05e4f801feee8d87070aded7318c5fbc5b947034ef3d7ad43f4) as a potential custodian for up to 20M FRAX, sFRAX is potentially dependent on Centrifuge, though currently [Centrifuge Prime's UI reports no TVL originating from FRAX](https://app.centrifuge.io/#/prime).

sFRAX has an on-chain yield component managed by the core team, with limited documented information. Discussion with Frax team members indicates that most income is derived from the FraxLend AMO. More information can be found about [the AMO here](https://facts.frax.finance/fraxlend/amo), though there is limited traceability on sFRAX's current share.

As a tokenized yield-bearing version of FRAX, sFRAX inherits all of FRAX's dependencies (governance, oracles, the ERC20 contract, and AMOs). sFRAX is supposed to rely on a Federal interest rate (IORB) Oracle as a target APY to match, but this is not documented or listed on Chainlink's website. This prerequisite dependency has yet to be implemented, leaving questions about sFRAX's actual yield target and on-chain representation.

## 4. Counterparty Risk

### 4.1 Governance and Regulatory Risk

#### FRAX

Frax is governed by FXS holders with a very active DAO. However, the vast majority of governance decisions are off-chain via [Snapshot](https://snapshot.org/#/frax.eth), requiring trust in the Frax team to execute on the wishes of the DAO. Nearly all Snapshot votes are passed with the support of [one voter](https://snapshot.org/#/profile/0x724061efDFef4a421e8be05133ad24922D07b5Bf), enjoying roughly 290 times the voting power of the [rest of the voters](https://snapshot.org/#/frax.eth/proposal/0xccdbe736cd70ba9e736eabec93505d61c1750765c8d2b0e8a0a562865bab964f)- this is the Convex voting address, which itself is composed of a multitude of interested parties.

Although Frax has developed an on-chain governance system, [frxGov](https://app.frax.finance/gov/frax), it has not yet been fully implemented. A soft launch has assigned frxGov control over only the Fraxlend Comptroller, and since January 2024, there has been no frxGov governance activity. Core Frax activities involving FRAX continue to be controlled by the Frax Comptroller multisig.

Since token governance involves trusted execution by the Frax team rather than true DAO governance, offering operational flexibility, this model requires vigilant monitoring of regulatory changes and compliance requirements. The discrepancy between documented and actual governance practices underscores the need for clarity in understanding Frax's true operational structure.

Frax operates without a formal legal structure, which is typical of DAOs. This offers flexibility but poses potential legal risks, particularly regarding liability. Under FATF guidelines, while DeFi applications aren't typically classified as VASPs, individuals with significant control might be.

#### sFRAX

sFRAX's governance considerations largely inherit those of FRAX, given that the Frax Comptroller multisig signers manage all underlying collateral and yield distribution. 

sFRAX's regulatory considerations are largely the same as above. In addition, as it is a yield-bearing stablecoin, it is likely to be considered a security by the SEC and other national-level regulators. For this reason, many RWAs do not allow US customers to purchase RWAs. The design of this token infers many characteristics of a financial instrument, which adds a layer of complication to the analysis. 

### 4.2 Access Control Risk

#### FRAX

FRAX is owned by [Frax Comptroller](https://etherscan.io/address/0xB1748C79709f4Ba2Dd82834B8c82D4a505003f27#readProxyContract), a 3/5 multisig. According to DeBank, the address controls $438m worth of Frax protocol funds, including idle funds and LP positions. Although Frax promotes the concept of AMOs to manage protocol funds algorithmically, the multisig signers have unilateral control over the flow of these funds. In addition to managing these funds, its ownership of FRAX allows it to set and configure AMO addresses, giving it essentially supreme authority over the operation of the entire protocol.

![image|2000x1150](upload://aYybBF3X4bZzgRhytxM7dpmwwiP.png)
Source: [DeBank](https://debank.com/profile/0xb1748c79709f4ba2dd82834b8c82d4a505003f27)

#### sFRAX

[sFRAX is owned](https://etherscan.io/address/0xa663b02cf0a4b149d2ad41910cb81e23e1c41c32#readContract) by a 3/6 multisig. Admin privileges are bestowed to the contract `timelockAddress`, which is assigned to a [GnosisSafe](https://etherscan.io/address/0x831822660572bd54ebaa065C2acef662a6277D40#code) (somewhat misleadingly, there is no actual timelock associated with the sFRAX vault). None of these addresses are listed in Frax documentation, indicating private ownership. Three of these addresses are also owners of the FRAX Comptroller multisig. There are notably very limited admin-gated controls in the sFRAX contract itself, which only allows the admin to change the reward rate. The majority of functions involving funds management and yield distribution for sFRAX depositors are managed by the Frax Comptroller multisig.

## 5. Aave V3 Specific Parameters

We concur with aligning FRAX with DAI on the Aave V3 mainnet and the proposed parameters from Chaos Labs for sFRAX.

**Note**: This assessment follows the LLR-Aave Framework, a comprehensive methodology for asset onboarding and parameterization in Aave V3. This framework is continuously updated and [available here](https://github.com/llama-risk/aave-research/blob/main/frameworks/aave_v3_framework.md).
