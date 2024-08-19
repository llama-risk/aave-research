## Summary

LlamaRisk endorses integrating steakLRT as ETH-correlated collateral in the Aave V3 Lido instance. We recommend utilizing steakLRT's internal rate with CAPO, considering both wstETH's historical yield and projected returns from Actively Validated Services (AVS) participation. This method is preferred over market pricing due to steakLRT's limited DEX liquidity. While redemptions are operational, prompt withdrawals aren't guaranteed, owing to the lack of an implicit vault buffer and potential third-party protocol deposit delays. Using the internal rate mitigates unwarranted liquidation risks that could cause temporary secondary market depegging if used as immediate exit liquidity.

Currently, underlying tokens remain idle, pending allocation to various AVS via the Symbiotic protocol. An updated risk assessment will be necessary upon strategy activation. Steakhouse's vault has the sole utility for farming points to date. Admission of steakLRT to lending markets opens the door to leveraged farming strategies. These circumstances predicate conservative parameterization.

We would also like to highlight security deficiencies in both underlying protocols used. Mellow's time-limited bug bounty contest with Immunefi offers a maximum $100k payout, which is inadequate given the protocol's TVL (over $600m), codebase complexity (over 1,000 lines of code), and novelty. Symbiotic lacks a bug bounty program entirely. We strongly recommend that both protocols establish bug bounty programs that align with their secured value.

[details="Read full assessment here"]

## 1. Asset Fundamental Characteristics

### 1.1 Asset

steakLRT, launched in June 2024, is an ERC-20 liquid restaking token (LRT) offered by [Steakhouse Financial](https://x.com/steakhousefi), representing wrapped Lido Staked ETH (wstETH) deposited into the [Steakhouse Resteaking Vault](https://app.mellow.finance/restake/ethereum-steaklrt). Leveraging both Mellow and Symbiotic protocols, steakLRT facilitates a flexible staking process that allows users to deposit stETH, wstETH, WETH, or ETH, which are then converted to wstETH - the underlying asset for steakLRT. This LRT aims to prove the efficiency of using Lido stETH in restaking while preserving Ethereum's decentralization. The vault currently allocates to a default strategy, which is idle for now, with plans to propose new allocation strategies as restaked networks come online. A comprehensive overview of the system is provided in the [launch announcement](https://hackmd.io/@SteakhouseFi/steakLRT).

**Key Metrics (as August 15th, 2024)**:
- Token Total Supply: 12,395 
- Total Token Holders: 1,922
- TVL: $39M (12,396 wstETH)
- APR: 3% (based on Lido staking yield)

Source: [Mellow App](https://app.mellow.finance/vaults/ethereum-steaklrt) and [Etherscan](https://etherscan.io/token/0xBEEF69Ac7870777598A04B2bd4771c71212E6aBc)

### 1.2 Architecture

Steak LRT utilizes Mellow Protocol for its liquid restaking token (LRT) issuance and management. It uses Symbiotic Protocol for the underlying vault operations, including asset delegation and restaking strategies across multiple networks. Withdrawal timeframes for Mellow are up to 7 days, while Symbiotic depends on the vault epoch duration, with a maximum of 90 days. It's important to note that the reward distribution mechanism and slashing for operators have yet to be implemented in either protocol.

#### Mellow

Mellow Protocol is an integration layer for DeFi that focuses on liquidity management and yield farming. Its modular architecture enables the creation of liquid restaking tokens for Ethereum-based liquid staking protocols. Mellow vaults are smart contracts that hold and manage assets, supporting the customization of strategies, assets, and risk management techniques. The vault creation framework allows users to create and manage vaults with customizable risk profiles.

In SteakLRT's implementation, Mellow provides the foundation for liquid restaking token management. It enables a vault system where users deposit assets, designed to hold wstETH only. This structure supports yield optimization and liquidity management while allowing users to maintain exposure to the underlying staked ETH.

![image|1200x1399](upload://9d2fs1Edejb2LySY0YVrwanXyiw.jpeg)

Source: [Mellow Docs](https://docs.mellow.finance/mellow-lrt-primitive/overview)

The vault contract utilizes a `configurator` to manage various customizable settings, including withdrawal fees, emergency delays, and deposit/transfer locks. It features a custom withdrawal mechanism using the `registerWithdrawal` and `processWithdrawals` functions. Users must request a withdrawal processed later based on contract conditions. Standard withdrawals have no specified delay, while emergency withdrawals have a mandatory delay set by the `VaultConfigurator`. All withdrawal delays are capped at 90 days.

#### Symbiotic

Symbiotic introduces highly configurable vaults for delegation and restaking management. These vaults handle accounting, delegation strategies, and reward distribution. They can be deployed as immutable or owner-updateable contracts. Vaults use a predefined `ERC20` collateral token and operate with three main modules: Accounting, Slashing logic, and Limits and delegation logic. The protocol uses epochs for withdrawal processes and slashing guarantees. It offers two types of delegators: `FullRestakeDelegator` and `NetworkRestakeDelegator`. Slashing, while designed with instant and veto options, has yet to be implemented. Rewards are calculated using `activeSharesOfAt()` and `activeSharesAt()` for stakers and `Delegator.stakeAt()` for operators, but distribution is managed by external contracts. The [Symbiotic documentation](https://docs.symbiotic.fi/core-modules/vaults) provides more detailed information on these components and their interactions.

![image|2000x1125](upload://jj3oCjqTxd4Biflu5ZVcClEFMKS.png)
Source: [Symbiotic Docs](https://docs.symbiotic.fi/core-modules/vaults)

LlamaRisk covered Symbiotic in detail [here](https://www.llamarisk.com/research/current-state-of-symbiotic).

### 1.3 Tokenomics

steakLRT does not follow the ERC-4626 standard vault token but implements its logic for handling deposits and withdrawals.

Mellow hinted [loyalty points offering](https://docs.mellow.finance/mellow-lrt-lst-primitive/loyalty-points#loyalty-points-logic-for-curators) to curators (Steakhouse potentially benefiting) as extra incentivization to deploy LRTs and pursue broad DeFi integrations. The calculation formula or program logic is not disclosed. 

## 2. Market Risk

### 2.1 Liquidity

Liquidity for steakLRT remains limited, primarily concentrated in the [Balancer Composable Stable Pool](https://app.balancer.fi/#/ethereum/pool/0x4216d5900a6109bba48418b5e2ab6cc4e61cf4770000000000000000000006a1), holding approximately $2.5 million worth of assets as of August 15, 2024. The pool includes various LRT vaults from the Mellow platform and wstETH.

![image|691x472](upload://x6QqgG86FofEvoqUqC4jHkrFoGL.png)
Source: [Balancer Composable Stable Pool](https://app.balancer.fi/#/ethereum/pool/0x4216d5900a6109bba48418b5e2ab6cc4e61cf4770000000000000000000006a1), August 15th, 2024

![image|729x405](upload://AiS8BAc9NimBTQ82toDSeHIZVpw.png)
Source: [Dune Analytics](https://dune.com/queries/3912817/6577461), August 15th, 2024

As of August 15, 2024, swapping 110 steakLRT to wstETH results in over 7.5% slippage, indicating low liquidity depth. Redemptions are possible, subject to certain delays.

![image|486x285](upload://ssOed21WTP4E256Q0TcokyXMh6g.png)
Source: Cow.fi, August 15, 2024

steakLRT is also present on the Pendle platform, where deposits in the Fixed Yield Market (PT tokens) are covered by Nexus insurance.

![image|321x370](upload://hpX9IT43t8E8IFCuRJpIlqrGKoX.png)
Source: [Pendle](https://app.pendle.finance/), August 15th, 2024

### 2.2 Volatility

steakLRT has demonstrated minimal fluctuation in its premium/discount and exchange value relative to ETH. Throughout the observed period, steakLRT has been trading at or very close to its intrinsic value (in ETH terms).

![image|810x439](upload://s6H1G4KgNdL0dGY2XC1E4QRCR1u.png)
Source: [Dune](https://dune.com/queries/3918585/6587645), August 15th, 2025

### 2.3 Growth

steakLRT initially showed significant market activity, reaching 2,000 ETH in just three hours after its launch, indicating strong interest and demand.

As of the latest data, Mellow's total value locked (TVL) stands at $628.59 million, reflecting the protocol's substantial footprint in the DeFi space. Within this context, steakLRT commands a noteworthy $40 million in TVL, equivalent to 12,637 wstETH. This figure, corroborated by Mellow's front-end displayed data and independent Dune analytics queries, represents approximately 6.36% of Mellow's total TVL.

![image|937x747](upload://sGdVlG64ISiqaWGOgfBTJIajbLz.png)
Source: [Defi Llama](https://defillama.com/protocol/mellow-lrt#information)

![image|930x308](upload://8akKLQZWWRtAJRy802oQEtckOUv.png)
Source: [Dune/kodi2227](https://dune.com/kodi2227/mellow-finance-lrt)

After the post-launch spike, the current volume of daily deposits is low.

![image|1180x297](upload://bYRppWUpALFN1UPLISVIuN4ncQE.png)
Source: [Dune](https://dune.com/queries/3993994/6722215), August 16th, 2025

An analysis of the steakLRT token's holder distribution reveals that two of the top three are Pendle yield markets ([SY-steakLRT Token](https://etherscan.io/token/0xbeef69ac7870777598a04b2bd4771c71212e6abc?a=0x998a1d40f097fd36bff15ca78fc0673bd2a8280c)), and the Zircuit Restaking pool. The remaining top holders cannot be identified.

![image|1320x614](upload://Ev1qHV3DAOnNYJIaeUJPTTBpxm.png)
Source: [Etherscan](https://etherscan.io/token/tokenholderchart/0xbeef69ac7870777598a04b2bd4771c71212e6abc)

Mellow Protocol has announced a partnership with ZircuitL2 to curate incoming Symbiotic networks. This collaboration involves steakLRT and tokens like Re7LRT, rstETH, and amphrETH. SteakLRT allows users to earn multiple points within Symbiotic, including Mellow Points, Zircuit Points, and Symbiotic Points. This points system may drive further growth as it incentivizes users to engage with the protocol and potentially attracts new participants to the ecosystem.

## 3. Technological Risk

### 3.1 Smart Contract Risk

Mellow protocol underwent smart contract [security audits](https://docs.mellow.finance/mellow-lrt-primitive/security) by ChainSecurity, and StateMind and Sherlock. The audits revealed several vulnerabilities in the smart contracts, primarily related to reentrancy attacks and improper access controls. The development team promptly addressed these issues and deployed patches to mitigate risks.

ChainSecurity and StateMind [audited](https://docs.symbiotic.fi/security) Symbiotic protocol. Low severity issues were identified and resolved. No critical, high, or medium issues were found.

Mellow's [bug bounty contest](https://immunefi.com/boost/boost-lido/information/) on Immunefi runs briefly from August 15 to September 5, 2024, with a maximum payout of $100k. This sum is inadequate considering the protocol's 1,281 lines of code across 12 smart contracts and the potential value at stake. Symbiotic, with its systems not yet fully operational, has not announced any bug bounty program.

### 3.2 Price Feed Risk

The `VaultConfigurator` contract uses the [Chainlink Oracle](https://etherscan.io/address/0x1Dc89c28e59d142688D65Bd7b22C4Fd40C2cC06d) for price feeds. Mellow employs a ChainlinkOracle wrapper that enforces cross-oracle price checks. It retrieves the token price against an intermediate token (e.g., ETH) before converting to the WETH base token price. For wstETH, the protocol utilizes a custom `WStethRatiosAggregatorV3` contract that returns the wstETH/stETH ratio instead of the direct wstETH price. This implementation assumes 1 stETH = 1 WETH.

### 3.3 Dependency Risk

steakLRT operates on top of Mellow protocol, using Symbiotic as middleware. The performance and security of steakLRT are heavily reliant on the underlying protocol architecture, transaction throughput, and smart contract capabilities. Token growth relies on expansion towards other restaking marketplaces or yield-generating venues for LRTs.

As per the Mellow vault's description, Steakhouse commits to allocating to multiple networks corresponding to the team's core strategy to build strategies with wsETH. No further selection criteria are being provided at this time.

The audit report by ChainSecurity highlights the trust assumptions involved with the dependencies:

> "The bonds used (at the time of this review) is DefaultCollateral of Symbiotic. These contracts are fully trusted to work as expected (i.e., there is no slippage on minting and withdrawal, and the conversion rate is always 1:1)."
>
> "Lido.depositBufferedEther is expected to work correctly as documented. Curators of a vault should continuously monitor and take measures if Lido's oracle is inactive or reports incorrect data. Obol staking module and Lido's Deposit Security Committee are assumed to be trusted. Similarly, Chainlink oracles are considered trusted."

This highlights the trust assumptions placed on Symbiotic's DefaultBond contracts, Lido's depositBufferedEther function, Obol staking module, Lido's Deposit Security Committee, and Chainlink oracles. The security and performance of steakLRT are dependent on these external components functioning as expected.

## 4. Counterparty Risk

### 4.1 Governance and Regulatory Risk

The proposed [governance evolution](https://hackmd.io/@SteakhouseFi/steakLRT) marks a shift towards decentralized control, introducing veto rights for vault depositors through an Aragon DAO guardian setup empowering steakLRT holders.

Steakhouse Financial Limited, incorporated in the Cayman Islands, focuses on crypto financial advisory without licensing requirements in that jurisdiction, affording operational latitude.

Steakhouse's vault curation on Mellow reveals an arms-length relationship with user assets, lacking direct custody. The absence of explicit legal ties between Curators and depositors emphasizes the protocol-centric nature, with Mellow mediating the relationship—curator responsibilities center on risk management and strategy implementation, distinct from traditional fiduciary duties.

Steakhouse lacks control over point distribution for Mellow or Symbiotic vaults. [Mellow documentation](https://docs.mellow.finance/mellow-lrt-lst-primitive/loyalty-points) details points calculation, but Terms of Service don't cover it. [Symbiotic's Terms of Use](https://app.symbiotic.fi/terms_of_use.pdf) clarify points' non-monetary, adaptable nature.

### 4.2 Access Control Risk

The Mellow LRT system uses the `DefaultAccessControl` contract for role-based access control. Key roles and addresses for the [steakLRT Vault](https://etherscan.io/address/0xBEEF69Ac7870777598A04B2bd4771c71212E6aBc) are:

- [**Configurator**](https://etherscan.io/address/0xe6180599432767081beA7deB76057Ce5883e73Be) 
- [**Validator**](https://etherscan.io/address/0xdB66693845a3f72e932631080Efb1A86536D0EA7)

**Roles**:
- [**ADMIN_ROLE**](https://etherscan.io/address/0x9437B2a8cF3b69D782a61f9814baAbc172f72003): 5/8 multisig 
  - Can add/remove tokens and TVL modules and configure vault settings.
- [**ADMIN_DELEGATE_ROLE**](https://etherscan.io/address/0x9437B2a8cF3b69D782a61f9814baAbc172f72003): Same 5/8 multisig as ADMIN_ROLE.
- [**OPERATOR**](https://etherscan.io/address/0x7a14b34a9a8EA235C66528dc3bF3aeFC36DFc268) ([DefaultBondStrategy](https://etherscan.io/address/0x7a14b34a9a8ea235c66528dc3bf3aefc36dfc268))
  - Can execute external/delegate calls and process withdrawals.

The 5/8 multisig has signers from Mellow Protocol, Gearbox, and Lido contributors ([details](https://research.lido.fi/t/mellow-lido-alliance-proposal/7557/30)).

Other contracts:
- **DepositWrapper**: `0x24fee15BC11fF617c042283B58A3Bda6441Da145`
- **UpgradeableProxyAdmin**: `0xed792a3fDEB9044C70c951260AaAe974Fb3dB38F`
- [**TimelockController**](https://etherscan.io/address/0x9cd146FC4A7019fC3610CFC8c72D55f364afCef4): Delay 0 (no timelock)

The privileged roles are fully trusted and can perform critical operations like external calls, configuration changes, and withdrawal processing. Users should understand the risks of these trusted roles before depositing them into the vault.

**Note**: This assessment follows the LLR-Aave Framework, a comprehensive methodology for asset onboarding and parameterization in Aave V3. This framework is continuously updated and [available here](https://github.com/llama-risk/aave-research/blob/main/frameworks/aave_v3_framework.md).

[/details]

## Aave V3 Specific Parameters

| Parameter                 | Recommendation |
|---------------------------|----------------|
| Isolation Mode            | No             |
| E-mode                    | Yes (ETH-correlated)|
| Borrowable                | Yes            |
| Borrowable in Isolation   | No             |
| Collateral Enabled        | Yes            |
| Stable Borrowing          | Disabled       |
| Supply Cap                | 240            |
| Borrow Cap                | 24             |
| Debt Ceiling              | -              |
| LTV                       | 72%            |
| LT                        | 75%            |
| Liquidation Bonus         | 7.5%           |
| Liquidation Protocol Fee  | 10%            |
| Reserve Factor            | 15%            |
| Base Variable Borrow Rate | 0%             |
| Variable Slope 1          | 7%             |
| Variable Slope 2          | 300%           |
| Uoptimal                  | 45%            |

### CAPO

We recommend using the same CAPO rate as wstETH, [currently 9.68%](https://etherscan.io/address/0xB4aB0c94159bc2d8C133946E7241368fc2F2a010#readContract#F13), and a minimum snapshot delay of 7 days.
