# LlamaRisk Network Qualification Framework

**Version:** 0.1 **Last Updated:** December 18th 2024

**Note:** This live document will be continuously updated and improved over time. Future revisions will incorporate new insights, methodologies, and community feedback to ensure the framework remains current and effective.


## Introduction

Aave DAO often proposes deploying the protocol to new networks. As a risk provider, LlamaRisk would like to qualify its recommendation with the potential risks of such an action in mind. 

Our approach combines quantitative and qualitative analysis to form a recommendation on whether a network can safely host an Aave protocol deployment and suitable parameters for assets on that network. We place a key focus on qualitative metrics in the context of the dual risk service provider system under Aave and provide complementary input to the DAO.

The framework begins with a review of the (1) Network Fundamental Characteristics. Subsequently, the risk assessment is divided into three categories to form a comprehensive evaluation of the proposed networks's overall risk profile and protocol suitability: (2) Liquidity, (3) Asset outlook, and (4) Transparency.

Based on this assessment, (5) Parameters Suggestions are proposed. Our goal is to conduct a thorough analysis, verify claims, and present our findings in a timely and digestible manner for the DAO stakeholders to make informed decisions.

This review system may be modified as required to meet the needs of the particular network. 

## 1. Network Fundamental Characteristics

- **Description:** Evaluate the fundamental technical configuration of the network to qualify whether it is suitable to host an Aave deployment including its architecture, how decentralized it is and what level of activity it hosts.
- **Metrics:** 
   - Network architecture, [L2Beat network "stage"](https://medium.com/l2beat/introducing-stages-a-framework-to-evaluate-rollups-maturity-d290bb22befe), consensus mechanism, virtual machine support, dependencies, network security model and change management, audits, bug bounties, open source repositories
   - Decentralization, geographical decentralization, client count, consensus evaluation, upgrade control processes, revenue distribution
   - Activity benchmarks: TVL, market capitalization, stablecoin TVL / dominance, number and concentration of protocols, DEX volumes, perpetuals open interest, total value borrowed, value at risk, bad debt accrued, supply APY (stable or volatile) and utilization rates

### 1.1 Network Overview

### 1.2 Decentralization and Legal Evaluation

### 1.3 Activity Benchmarks

## 2. Network Market Outlook
- **Description:** Review a network's liquidity outlook and assess growth potential and its resilience in the face of periods of high volatility. 
- **Metrics:** 
    - Market infrastructure: a variety of DeFi needs covered (lending, DEXs, stablecoins, derivatives), LP fragmentation, bridge accessibility, wallet / portfolio support, on / offramps, oracles
    - Liquidity landscape: incentives programs, fee structures, market depth for majors, competing lending markets, swap volume concentration
    - Ecosystem resilience: community initiatives for liquidity crisis management, deep DEX and lending liquidity, an appointed entity ready to restore confidence to the network, grants programs, partnerships with other ecosystems
    - - Native token, presence of major tokens, collateralization rates, price stability, DEX volume distribution, availability of collateral

### 2.1 Market Infrastructure

### 2.2 Liquidity Landscape

### 2.3 Ecosystem Resilience

### 2.4 Ecosystem Growth Potential

### 2.5 Major and Native Asset Outlook
 

## 3. Onchain discoverability
- **Description:** Verify the availability of accurate, relevant information to ensure that Aave's deployment is well monitored and maintained. 
- **Metrics:**
    - Broad range of tools such as Dune, DeFiLlama, Etherscan equivalent, theGraph, Flipside, Nansen, TokenTerminal

### 4.2 Monitoring Impact


## 5. Asset suggestions
- **Description:** Provisional suggestions for assets (with parameters pending later alignment with Risk Providers) to onboard to Aave on the proposed network. This will reflect a leaner version of our [asset framework.](https://github.com/llama-risk/aave-research/blob/main/frameworks/aave_v3_framework.md)
- **Metrics:**
    - Asset fundamentals
    - Bridge risk (if applicable)
    - Liquidity analysis
    - Technical risk analysis
    - Counterpart risk analysis
    - Price feed recommendation



## Change Log



| Version | Date | Summary |
| -------- | -------- | -------- |
| 0.1     | 18.13.24     | Introduced NQF    |
