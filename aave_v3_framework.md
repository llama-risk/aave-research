
![18](https://hackmd.io/_uploads/HyStUbvLR.jpg)

# LLR-Aave Framework

## Introduction

This document outlines our framework for asset onboarding and parameterization for Aave V3. Our approach combines quantitative and qualitative analysis to form a recommendation on whether an asset can be safely onboarded and under what parameters. We place a key focus on qualitative metrics in the context of the dual risk service provider system under Aave, and provide complementary input to the DAO.

The framework begins with a review of the (1) **Asset Fundamental Characteristics**. Subsequently, the risk assessment is divided into three categories to form a comprehensive assessment of the proposed asset's overall risk profile: (2) **Market Risk**, (3) **Technological Risk** and (4) **Counterparty Risk**.

Based on this assessment, (5) **Specific Parameters** are proposed. Our goal is to conduct a thorough analysis, verify claims, and present our findings in a timely and digestible manner for the DAO stakeholders to make informed decisions.

## 1. Asset Fundamental Characteristics
- **Description**: Evaluate the fundamental characteristics of the asset, including its purpose, utility, and value proposition.
- **Metrics**:
  - Token type (e.g., utility token, governance token, stablecoin, LST/LRT)
  - Underlying blockchain (e.g., Ethereum, Polygon, Avalanche) and bridge support
  - System architecture
  - Tokenomics, incentives, and sustainability

## 2. Market Risk
- **Description**: Assess the asset's market-related risks, considering liquidity, volatility, and market depth.
- **Metrics**:
  - Liquidity (e.g., trading volume, liquidity pools, bid-ask spread)
  - Volatility (e.g., price volatility, historical price movements)
  - Trading pairs and exchanges (e.g., centralized and decentralized exchanges)
  - Holders and growth trends

## 3. Technological Risk

### 3.1 Smart Contract Risk
- **Description**: Evaluate the security and reliability of the asset's smart contract code, considering audits, code quality, and potential vulnerabilities.
- **Metrics**:
  - Audits (e.g., number of audits, reputation of auditing firms)
  - Code quality (e.g., code complexity, test coverage, documentation)
  - Potential vulnerabilities (e.g., known issues, attack vectors)
  - Contract upgradability (e.g., proxy patterns, governance mechanisms)

### 3.2 Price Feed Risk
- **Description**: Assess the reliability and robustness of the asset's price feed mechanisms.
- **Metrics**:
  - Price feed sources (e.g., oracles, exchanges, on-chain data)
  - Price feed decentralization and redundancy
  - Historical price feed accuracy and reliability
  - Potential price manipulation risks

### 3.3 Dependency Risk
- **Description**: Evaluate the asset's dependencies on external systems or protocols and the associated risks.
- **Metrics**:
  - External dependencies (e.g., other protocols, infrastructure providers)
  - Dependency risk mitigation measures (e.g., redundancy, failover mechanisms)

## 4. Counterparty Risk

### 4.1 Governance and Regulatory Risk
- **Description**: Assess the governance structure and potential regulatory risks associated with the asset.
- **Metrics**:
  - Governance model (e.g., centralized, decentralized, multi-sig)
  - Governance token distribution (e.g., token holders, voting power)
  - Regulatory compliance (e.g., licenses, registrations, legal opinions)
  - Potential regulatory risks (e.g., securities laws, anti-money laundering regulations)

### 4.2 Access Control Risk
- **Description**: Evaluate the access control mechanisms and privileged roles within the asset's ecosystem.
- **Metrics**:
  - Access control model (e.g., multi-sig, time-locks, role-based access control)
  - Privileged roles and their responsibilities
  - Checks and balances on privileged roles
  - Historical incidents related to access control

## 5. Aave V3 Specific Parameters

This section outlines the specific parameters for Aave V3 that need to be configured when onboarding a new asset or adjusted following changes in its risk profile. These parameters are crucial for defining the asset's behavior within the Aave protocol, including its borrowing and collateral capabilities, risk management settings, and interest rate model.

1. **General**
    1.1 **Borrowable** (`ENABLED/DISABLED`): asset can be borrowed.
    1.2 **Collateral Enabled** (`ENABLED/DISABLED`): asset can be used as collateral.
    1.3 **Flashloanable** (`ENABLED/DISABLED`): asset can be used for flashloans.
2. **Caps**
    2.1 **Supply Cap** (`INTEGER`): maximum asset quantity that can be deposited.
    2.2 **Borrow Cap** (`INTEGER`): maximum asset quantity that can be borrowed.
    2.3 **Debt Ceiling** (`INTEGER`): dollar value limit that can be borrowed against the collateral.
3. **Liquidations**
    3.1 **LTV** (`INTEGER`): maximum percentage that a borrow position can be openned at against a specific collateral.
    3.2 **LT** (`INTEGER`): percentage at which a position is deemed undercollateralized and can be liquidated
    3.3 **Liquidation Bonus** (`INTEGER`): percentage of liquidation proceeds that goes to the liquidator
    3.4 **Liquidation Protocol Fee** (`INTEGER`): percentage of the liquidation bonus that goes to the protocol.
4. **Interest rate model**
    4.1 **Uoptimal** (`INTEGER`): optimal utilization percentage, dictates where slope2 starts.
    4.2 **Base** (`INTEGER`): base interest rate, when utilization is null.
    4.3 **Slope1** (`INTEGER`): rate of increase if utilization is below optimal rate.
    4.4 **Slope2** (`INTEGER`): rate of increase if utilization is above optimal.
    4.5 **Reserve Factor** (`INTEGER`): percentage of interest generated that goes to the protocol.
5. **Isolation**
    5.1 **Isolation Mode** (`ENABLED/DISABLED`): collateral can only be used to borrow stablecoin.
    5.2 **Borrowed in Isolation**  (`ENABLED/DISABLED`): enable stablecoin to be borrowed from isolation mode.
6. **E-Mode**
    6.1 **E-Mode category**  (`CATEGORY NAME`): categorizes correlated assets allowing more aggresive parameters for higher capital efficiency.

### Parameter Considerations

* **Recursive looping**: When an asset can be both borrowed and used as collateral, it enables recursive looping (also known as leveraged yield farming or folding) - a DeFi strategy that maximizes returns by repeatedly borrowing and lending the same asset. The maximum leverage achievable is given by the formula: `Maximum Leverage = 1 / (1 - LTV)` where LTV is the Loan-to-Value ratio expressed as a decimal.
* **Supply and borrow caps**: 
  - Supply cap should be calibrated to ensure sufficient on-chain liquidity for potential liquidations. We concur with Chaos Labs' recommendation of using twice the available liquidity within the liquidation bonus price impact as a baseline metric. Our methodology expands on this approach by incorporating historical liquidity trends and simulated market stress scenarios to provide a comprehensive assessment of appropriate supply cap levels.
  - The borrow cap should be a portion of the supply cap. By using uOptimal to derive the borrow cap, the protocol ensures there are idle assets if the supply cap has been reached.
* **Liquidations**: 
  - Liquidation bonus needs to be high enough to incentivize liquidators, considering factors such as gas fees, asset volatility, and the risk of bridging collateral. The liquidation bonus should be a function of the asset's volatility, with higher bonuses for more volatile assets to compensate for the increased risk taken by liquidators.
  - LTV ratio dictates how much leverage users can take when engaging in recursive looping. A higher LTV allows for more leverage but also increases the risk of liquidation.
  - LT (Liquidation Threshold) should have sufficient buffer from LTV to protect users who have opened a position against sudden market fluctuations, reducing the risk of immediate liquidation.
* **Interest Rate Model (IRM)**:
  - The Aave Interest Rate Model (IRM) is a key component in determining the borrowing and lending rates based on the utilization of an asset. This [IRM calculator](https://www.desmos.com/calculator/10d33ehuhp) helps visualize and simulate different IRM configurations.
  - Goals of the IRM:
    - Limit rates above the optimal utilization rate to minimize negative user experience impact caused by higher rate volatility when utilization exceeds the optimal ratio.
    - Reduce rate volatility, which promotes an increase in borrower participation, as it provides a more stable and predictable borrowing environment.
