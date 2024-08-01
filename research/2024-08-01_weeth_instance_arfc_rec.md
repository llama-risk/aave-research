# Summary

LlamaRisk supports the parameters recommended by @ChaosLabs for the launch of the Aave V3 EtherFi instance. We discussed these parameters jointly during our review process. Although we initially had larger supply caps in mind, we agree that the demand for weETH/stablecoin borrowing still needs to be proven. Therefore, an iterative approach is preferable.

An Aave V3 EtherFi instance should facilitate the weETH/stablecoin borrowing use case, which currently accounts for 0.45% of the borrowed assets against weETH on the main instance due to the fully utilized supply cap. If weETH exhibits behavior similar to wstETH on the main instance, given the current value borrowed against weETH, we estimate that the potential borrowing demand for stablecoins could exceed $500m. A higher LTV/LT for weETH, an incentive program for USDC deposits, and a slightly lower borrowing rate for GHO will help bootstrap this new instance. Meanwhile, a borrowing cap of $5.25m for GHO will limit the relative weight of weETH as GHO collateral. 

We will keep a close watch on the deployment of new Aave V3 standalone instances to ensure maximum incentive effectiveness and to make sure it serves its intended purpose. Additionally, we are excited about the new EtherFi Cash program and its potential integration with this EtherFi-specific instance.

# Detailed remarks

## Background on Lido instance as a comparative basis

The Aave V3 Lido instance, the first isolated deployment on Ethereum mainnet, was tailored for Lido's wstETH looping use case. Although it focuses on WETH looping, it offers valuable insights for bootstrapping the new EtherFi instance. This separate instance was created to address the fully utilized supply cap on the main instance, which hindered stablecoin borrowers from managing liquidation risks. weETH depositors can borrow WETH using efficiency mode (eMode) with higher LTV and LT parameters. Additionally, it helps reduce the concentration of Lido-related assets in the main Aave V3 system.

![image|1109x508](upload://qG8xYFuyueIjXP5lq2PpmkrQBH6.png)
Source: Aave V3 - Lido Instance, August 1st, 2024

To attract WETH deposits over wstETH holdings, the WETH lending rate was set higher than wstETH's, supplemented by liquidity incentives. The strategy proved successful, with TVL reaching around $275m by August 1st, 2024. Consequently, [WETH was removed as collateral](https://governance.aave.com/t/arfc-deploy-a-lido-aave-v3-instance/18047/18?u=exaparsec) to prevent incentive farming. While the market's bootstrapping succeeded, it remains to be seen how sticky this liquidity will be over time after incentives cease.

## Potential demand for weETH/stablecoin borrowing

While the demand for weETH/stablecoin borrowing remains unproven, we can draw insights from stETH on the main instance. stETH, which we consider a safer and more mature asset compared to weETH, has a similar profile on the LSD side. The use cases for stETH on the main instance ($2.04b in borrowed assets) are:

- 48.4% for WETH looping
- 39.2% for stablecoin borrowing
- 12.4% for borrowing other volatile assets

Source: [stETH collateral split](https://community.chaoslabs.xyz/aave/risk/markets/Ethereum/listed-assets/wstETH)

The main use case is WETH looping, but stablecoin borrowing follows closely at 39.2% of the borrowed value. Currently, stablecoin borrowing against weETH on the main instance is only 0.45%. This low figure likely results from the fully utilized supply cap of weETH on the main instance. Using stETH on the main instance as a reference, a specific weETH/stablecoin instance could serve a stablecoin borrowing demand against weETH of over $500m, based on the current total borrowed value against weETH of $2b.

## GHO collateral composition

The GHO borrowing cap currently sits at $105m and is backed by a diverse basket of assets. We recognize the importance of maintaining this diversification as the GHO supply grows to limit GHO's reliance on a single collateral. In that sense, we support the proposed GHO borrow cap of $5.25m for weETH. This borrowing cap should be increased along with the borrowing caps of other collaterals backing GHO, thus maintaining a healthy relative weight for each collateral.

![image|762x500](upload://fe17YA56gYPdcWZDi5e95aielEu.png)
Source: [ChaosLabs's dashboard](https://community.chaoslabs.xyz/aave/risk/GHO/overview), August 1st, 2024

To successfully bootstrap the new market, it needs to be economically attractive for weETH and USDC holders to deposit on this market for the stablecoin borrowing use case. For weETH holders, since the supply cap is reached on the main instance, depositing into the new instance will be the only venue for borrowing against it. Therefore, we expect significant weETH deposits upon launch.

Currently, only 0.45% of the assets borrowed against weETH are stablecoins on the main instance, so we don't anticipate significant transfers from the main instance to the new EtherFi instance. Nevertheless, we support using higher LTV/LT values for weETH, adding an incentive program for USDC, and a lower GHO borrowing rate to kickstart this new Aave V3 instance successfully. To prevent incentive farming and avoid rapid exhaustion of supply caps, asset looping should be prohibited for both weETH and USDC.
