# Asset Notes & Alert Suppressions

> Edit this file to suppress alerts or add analyst notes for specific assets.
> The monitor reads this file on each run.

## Suppressions

<!-- Format: SYMBOL/Chain/Market — one per line. These assets won't trigger alerts. -->
<!-- Example: -->
<!-- - BAL/Ethereum/AaveV3Ethereum: uncapped intentionally — ignore cap alerts -->
<!-- - CELO/Celo/AaveV3Celo: deprecated, supply cap set to 1 — ignore -->

## Notes

<!-- Format: free-form notes per asset. Shown in verbose output. -->
<!-- Example: -->
<!-- - WETH/Ethereum/AaveV3Ethereum: largest market, watch closely -->
<!-- - PT-sUSDe-*/Plasma: fast-growing, may need frequent cap increases -->
