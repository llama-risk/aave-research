"""Chain registry for all known Aave V3 deployments.

The API returns markets (not just chains) — multiple markets can exist on
the same chain (e.g., Ethereum has Core, Lido, EtherFi, Horizon).
We track chain IDs to detect when Aave launches on a new chain.
"""

# All chain IDs observed from the Aave V3 GraphQL API (verified 2026-04-08)
KNOWN_CHAINS: dict[int, str] = {
    1:      "Ethereum",
    10:     "Optimism",
    56:     "BSC",
    100:    "Gnosis",
    137:    "Polygon",
    146:    "Sonic",
    324:    "zkSync",
    1088:   "Metis",
    1868:   "Soneium",
    4326:   "MegaETH",
    5000:   "Mantle",
    8453:   "Base",
    9745:   "Plasma",
    42161:  "Arbitrum",
    42220:  "Celo",
    43114:  "Avalanche",
    57073:  "Ink",
    59144:  "Linea",
    534352: "Scroll",
}

# All known market names (verified 2026-04-08, 22 markets)
KNOWN_MARKETS: set[str] = {
    "AaveV3Ethereum",
    "AaveV3EthereumEtherFi",
    "AaveV3EthereumLido",
    "AaveV3EthereumHorizon",
    "AaveV3Optimism",
    "AaveV3Arbitrum",
    "AaveV3Polygon",
    "AaveV3Avalanche",
    "AaveV3Base",
    "AaveV3Gnosis",
    "AaveV3Metis",
    "AaveV3BNB",
    "AaveV3Linea",
    "AaveV3Scroll",
    "AaveV3ZkSync",
    "AaveV3Celo",
    "AaveV3Mantle",
    "AaveV3Sonic",
    "AaveV3Soneium",
    "AaveV3MegaETH",
    "AaveV3Ink",
    "AaveV3Plasma",
}


def check_coverage(api_chain_ids: set[int], api_market_names: set[str]):
    """Return sets of unknown chains and markets not in our registry."""
    unknown_chains = api_chain_ids - set(KNOWN_CHAINS.keys())
    unknown_markets = api_market_names - KNOWN_MARKETS
    return unknown_chains, unknown_markets
