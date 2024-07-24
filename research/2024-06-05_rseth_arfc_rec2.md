# Collateral Risk Assessment - Kelp DAO Restaked ETH (rsETH)

LlamaRisk conducted a comprehensive collateral risk assessment on rsETH, **[which can be read here](https://www.llamarisk.com/research/collateral-risk-rseth)**. Our findings are generally favorable, with the Kelp team being receptive to our feedback and implementing several beneficial changes. These include displaying the 10% ETH staking reward fee and underlying breakdown on the UI and committing to implementing a bug bounty program.

We recommend onboarding rsETH with the earlier parameters: exclusion from e-Mode (as opposed to weETH and osETH), a limited supply cap of 8,000 rsETH, and a conservative LT of 75%. rsETH liquidity has increased an estimated 42% across different venues since our first assessment in late May 2024, and we perceive its risk as lesser now.

Below are the highlights of our research, supporting our recommendation. This recommendation is **contingent upon implementing a bug bounty program**, which we deem crucial and has been scheduled to go live in the coming days.

## Risk Management summary

This section will summarize the report's findings by highlighting the most significant risk factors in the three categories: Market Risk, Technology Risk, and Counterparty Risk.

### 6.1.1 Market Risk

**LIQUIDITY: Does the LSD have a liquid market that can facilitate liquidations in all foreseeable market events?**

The on-chain liquidity for rsETH is relatively good, with multiple integrations and liquidity venues. The minted rsETH is also relatively spread out among wallets and protocols, with no single EOA concentrating a significant portion of the supply. Top holders include LayerZero, a Zircuit re-staking pool, and a Pendle rsETH fixed-rate market. Liquidity pools with rsETH are either paired with WETH, ETH, ETHx from Stader, or weETH from EtherFi.

**VOLATILITY: Has the LSD had any significant depeg event?**

The rsETH/ETH secondary market rate has consistently traded at a small discount compared to the protocol's internal exchange rate. However, the peg has recently improved due to the addition of ETH withdrawals and a reduced withdrawal delay from 7 to 2 days. The only significant depeg event was a -1.5% deviation in late April, which quickly corrected. Notably, as rsETH is partially backed by LSDs, its exchange rate with ETH would be affected by any LSD depeg. This is an inherent characteristic of an LRT backed by LSDs, not a fault of Kelp. By using the internal exchange rates of LSDs, KelpDAO provides rsETH/ETH with a more stable exchange rate.

### 6.1.2 Technology Risk

**SMART CONTRACTS: Does the analysis of the audits and development activity suggest any cause for concern?**

KelpDAO has conducted three audits on its codebase from renowned auditors. Although no serious flaws were revealed, some fixes were made. The codebase is public on GitHub, well-documented, and shows professional development practices. However, online development activity is limited to a few commits; no PRs or tagged releases are visible. A Code4rena audit competition allowed anyone to disclose vulnerabilities, but the total reward was limited to $28k, which is low compared to industry standards. Kelp has stated that a bug bounty program will be implemented shortly, which we consider crucial before onboarding.

**DEPENDENCIES: Does the analysis of dependencies (e.g., oracles) suggest any cause for concern?**

KelpDAO directly depends on the internal exchange rates of ETHx and uses a hardcoded exchange rate of 1 for stETH. While beneficial for exchange rate stability, this could enable an arbitrage attack if one of the supported LSDs were to depeg. The KelpDAO team has provided a mitigation strategy, but it remains imperfect and could still result in a net loss for KelpDAO users in some cases. The implementation of a circuit breaker should improve this issue. The rsETH/ETH exchange rate, used for deposits and withdrawals, relies on the price of its underlying assets.

KelpDAO also relies on off-chain services for some aspects of the protocol. These services operate through an EOA whose private keys are stored in an AWS secret manager, authenticated using a role-based access control system. Although no funds can be stolen if the private keys leak, a more robust and secure approach is warranted. A decentralized set of off-chain services with an on-chain threshold consensus could enhance reliability and security.

### 6.1.3 Counterparty Risk

**CENTRALIZATION: Are there any significant centralization vectors that could rug users?**

KelpDAO remains very centralized, with the development team having significant power over contract upgrades, protocol parameters, and total control over the off-chain services needed for minting and withdrawals to work correctly. There is no DAO nor governance tokens. Communication mediums for users exist, including Twitter, Telegram, and Discord, but they mostly serve marketing and support purposes. However, a role-based access control system and two different multisigs, along with a timelock with a 10-day delay for contract upgrades, provide a solid foundation upon which more decentralization should be built.

**LEGAL: Does the legal analysis of the Protocol suggest any cause for concern?**

Kelp’s Terms of Service require users to self-acknowledge compliance with sanctions and ensure their funds are not linked to illegal activities. However, Kelp does not enforce access restrictions at the user interface level. Users must confirm they are not sanctioned or from sanctioned regions and agree not to use Kelp for unlawful purposes. Kelp may conduct "Know Your Customer" and "Anti-Money Laundering" checks and terminate services if users provide false information.

Advertised as a non-custodial protocol—even though the protocol is relatively centralized with the team having control over it — KelpDAO claims that users are fully responsible for their digital assets and wallet security, with Kelp bearing no liability for third-party services or issues arising from wallet use. While the terms of services are clear, the Panama incorporation results in a lack of regulatory clarity.

## Risk Rating

The following chart summarizes a risk rating for rsETH as collateral based on the risks identified for each category. The rating for each category is ranked from excellent, good, ok, and poor.

- We rank rsETH **good in liquidity** for the many liquidity venues that provide it. The existence of DEX pools paired with ETHx, based on the team's relationship with Stader, is a plus.
- We rank rsETH **good in volatility** because the quality of its peg has increased consistently. The only depeg event was short-lived and limited in strength.
- We rank rsETH **ok in smart contracts** because of the limited number of issues in the three publicly available audit reports. The code source is public, well-documented, and professional. However, the lack of a bounty is a significant issue, given the importance of TVL.
- We rank rsETH **poor in dependencies** because of using a fixed exchange rate for stETH and internal exchange rates for ETHx, potentially socializing specific asset risks between all depositors. The lack of transparency regarding off-chain services is also a cause for concern. Although essential to the correct operation of the protocol, they are operated in a centralized way through EOAs.
- We rank rsETH **ok in decentralization** because the team still has significant control over the protocol, and there is no clear path to decentralization. Validators are trusted by three professional node operators, which is good but could be greater. The role-based access control system, the multisigs, and the Timelock are positive. 
- We rank rsETH good in legal for establishing a fully compliant legal structure in the Panama Islands. Although user terms are clear, there still needs to be regulatory clarity from Panama's securities laws.

![image|1048x688](upload://A8INExBUXoyBSMIYYw1WiqGCO7L.png)
Source: [LlamaRisk comparative chart](https://flo.uri.sh/visualisation/14951150/embed)

<iframe src='https://flo.uri.sh/visualisation/14951150/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe>

Although KelpDAO has taken positive strides in making rsETH a suitable collateral asset, we generally advise caution when assuming exposure to any liquid restaking token. The sector remains highly speculative, driven by points programs that may lead to rapid shifts in demand for the asset, potentially resulting in sustained depeg events. LRTs are generally a less mature asset class with substantial centralization vectors and reliance on off-chain services that often involve processes overseen by the protocol team.

We advise that KelpDAO must address concerns critical to its security and transparency before being considered for collateral onboarding. We have been working with the KelpDAO team to resolve what we consider blockers. Their team has been receptive and has committed to addressing these points.
- Implementing a bug bounty program is urgently needed given the protocol's high TVL, and any delay poses significant risks. 
- KelpDAO's communication needs improvement, particularly regarding changes like the unannounced removal of sfrxETH. 

In addition to immediate blockers, we await the transition to a fully decentralized DAO structure, which should be expedited to ensure proper governance and community involvement and reduce reliance on off-chain services. Progressive decentralization is a common theme for many LRTs and DeFi protocols generally, but the current centralized management level highlights the protocol's immature state.

After addressing the two primary points described above, we advise a conservative approach to onboarding with low exposure limits, conservative LT parameters (exclusion from e-mode in Aave, for instance), and a gradual onboarding process that matches the protocol's maturity over time.
