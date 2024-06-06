LlamaRisk is in favour of @ChaosLabs's recommendation for cautious onboarding of Kelp's rsETH, including exclusion from e-Mode (as opposed to weETH and osETH), a limited supply cap of 8,000 rsETH, and a conservative LT of 75%. This recommendation stems from our initial review of rsETH, with a particular focus on its internal exchange rate (probed by @MarcZeller), and associated dependancies.

We share our preliminary findings below, emphasizing **using rsETH market price** for its integration with Aave. We are working on a comprehensive assessment of rsETH and will update the Aave community accordingly.

## rsETH Exchange Rate Mechanism

The rsETH exchange rate is determined by the underlying assets (ETH, stETH, ETHx, sfrxETH) and the accumulated staking rewards. The [`LRTOracle`](https://etherscan.io/address/0x349A73444b1a310BAe67ef67973022020d70020d) contract stores the Oracle contract for each asset.

* **stETH** ([oracle contract](https://etherscan.io/address/0x4cB8d6DCd56d6b371210E70837753F2a835160c4#code)): price is hardcoded to 1:1 with ETH.
* **ETHx** ([oracle contract](https://etherscan.io/address/0x3D08ccb47ccCde84755924ED6B0642F9aB30dFd2)): price relies on the `getExchangeRate` function of the `StaderStakePoolsManager` contract, which Stader updates via a permissioned function. The oracle does not independently check for price anomalies or liveness, and it is a proxy contract that the Stader team can upgrade. The `getExchangeRate` function, operated by Stader, returns a state variable called `exchangeRate`, updated by the `submitExchangeRateData` function, callable only by whitelisted addresses controlled by Stader. The ETHx price is determined by the "book value" of ETHx, calculated as `totalAssets` / `totalSupply`, similar to the ERC-4626 accounting method. 
* **sfrxETH** ([oracle contract](https://etherscan.io/address/0x8546A7C8C3C537914C3De24811070334568eF427)): price is obtained from Frax's sfrxETH `pricePerShare` function, an ERC-4626 tokenized vault. The price feed assumes frxETH to be 1:1 with ETH.

## Market Price vs. rsETH exchange rate

The rsETH exchange rate calculation includes several assumptions, resulting in a considerable spread between the computed exchange rate and the market price of rsETH. This can be seen in the chart below (data from March 8th May 31st):

![image|1572x556](upload://datA8dhdNMRERV3bVFpVefTclje.png)
Source: [rsETH internal rate](https://etherscan.io/address/0x349A73444b1a310BAe67ef67973022020d70020d), [Redstone](https://etherscan.io/address/0xA736eAe8805dDeFFba40cAB8c99bCB309dEaBd9B) & [Chainlink](https://etherscan.io/address/0x03c68933f7a3F76875C0bc670a58e69294cDFD01) feeds and [Uniswap V3 rsETH / ETH Pool](https://etherscan.io/address/0x059615EBf32C946aaab3D44491f78e4F8e97e1D3) (blocks 19390000 to 19987000)

## Risks with dependencies

The main risk factors associated with rsETH's dependencies are:

1. **sfrxETH/stETH oracle assumptions**: If the market price of stETH or frxETH falls below the ETH price, the collateral backing rsETH could be worth less than expected by the rsETH system. This could lead to a depreciation in the market price of rsETH.
2. **ETHx oracle centralization**: The ETHx price is obtained from a relatively centralized source. If a malicious actor manipulates the price feed, they could unjustly inflate the rsETH supply up to the ETHx deposit limit.
3. **`LRTManager` permissioned function**: The [Kelp External Admin (6/8)](https://etherscan.io/address/0xb3696a817D01C8623E66D156B6798291fa10a46d) is whitelisted as the `LRTManager`, which can `updatePriceOracleFor` without a timelock. This centralization could lead to mistakes or malicious actions that could brick the protocol or cause a loss of funds. For example, adding a new supported token requires calling three different functions in a specific sequence. If the calls are contained in other transactions, the protocol could be in an intermediate state, blocking the `updateRSETHPrice()` function.