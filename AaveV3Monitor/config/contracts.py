from __future__ import annotations

"""Contract addresses and RPC endpoints for on-chain sanity checks.

Pool and DataProvider addresses are resolved at runtime from the
PoolAddressesProvider, but we cache them after first resolution.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

BLOCKPI_KEY = os.environ.get("BLOCKPI_KEY", "")
INFURA_KEY = os.environ.get("INFURA_KEY", "")

# ── Market → PoolAddressesProvider ───────────────────────────────────────
# Verified 2026-04-08 by resolving Pool.ADDRESSES_PROVIDER() on-chain.
MARKETS: dict[str, dict] = {
    # Ethereum (chain 1) — 4 markets
    "AaveV3Ethereum": {
        "chain_id": 1,
        "pool_addresses_provider": "0x2f39d218133AFaB8F2B819B1066c7E434Ad94E9e",
    },
    "AaveV3EthereumLido": {
        "chain_id": 1,
        "pool_addresses_provider": "0xcfBf336fe147D643B9Cb705648500e101504B16d",
    },
    "AaveV3EthereumEtherFi": {
        "chain_id": 1,
        "pool_addresses_provider": "0xeBa440B438Ad808101d1c451c1c5322c90BEFcDA",
    },
    "AaveV3EthereumHorizon": {
        "chain_id": 1,
        "pool_addresses_provider": "0x5D39e06B825c1f2B80bf2756A73e28efAA128bA0",
    },
    # Other chains
    "AaveV3Optimism": {
        "chain_id": 10,
        "pool_addresses_provider": "0xa97684ead0e402dC232d5A977953DF7ECBaB3CDb",
    },
    "AaveV3Arbitrum": {
        "chain_id": 42161,
        "pool_addresses_provider": "0xa97684ead0e402dC232d5A977953DF7ECBaB3CDb",
    },
    "AaveV3Polygon": {
        "chain_id": 137,
        "pool_addresses_provider": "0xa97684ead0e402dC232d5A977953DF7ECBaB3CDb",
    },
    "AaveV3Avalanche": {
        "chain_id": 43114,
        "pool_addresses_provider": "0xa97684ead0e402dC232d5A977953DF7ECBaB3CDb",
    },
    "AaveV3Base": {
        "chain_id": 8453,
        "pool_addresses_provider": "0xe20fCBdBfFC4Dd138cE8b2E6FBb6CB49777ad64D",
    },
    "AaveV3Gnosis": {
        "chain_id": 100,
        "pool_addresses_provider": "0x36616cf17557639614c1cdDb356b1B83fc0B2132",
    },
    "AaveV3Metis": {
        "chain_id": 1088,
        "pool_addresses_provider": "0xB9FABd7500B2C6781c35Dd48d54f81fc2299D7AF",
    },
    "AaveV3BNB": {
        "chain_id": 56,
        "pool_addresses_provider": "0xff75B6da14FfbbfD355Daf7a2731456b3562Ba6D",
    },
    "AaveV3Linea": {
        "chain_id": 59144,
        "pool_addresses_provider": "0x89502c3731F69DDC95B65753708A07F8Cd0373F4",
    },
    "AaveV3Scroll": {
        "chain_id": 534352,
        "pool_addresses_provider": "0x69850D0B276776781C063771b161bd8894BCdD04",
    },
    "AaveV3ZkSync": {
        "chain_id": 324,
        "pool_addresses_provider": "0x2A3948BB219D6B2Fa83D64100006391a96bE6cb7",
    },
    "AaveV3Celo": {
        "chain_id": 42220,
        "pool_addresses_provider": "0x9F7Cf9417D5251C59fE94fB9147feEe1aAd9Cea5",
    },
    "AaveV3Mantle": {
        "chain_id": 5000,
        "pool_addresses_provider": "0xba50Cd2A20f6DA35D788639E581bca8d0B5d4D5f",
    },
    "AaveV3Sonic": {
        "chain_id": 146,
        "pool_addresses_provider": "0x5C2e738F6E27bCE0F7558051Bf90605dD6176900",
    },
    "AaveV3Soneium": {
        "chain_id": 1868,
        "pool_addresses_provider": "0x82405D1a189bd6cE4667809C35B37fBE136A4c5B",
    },
    "AaveV3MegaETH": {
        "chain_id": 4326,
        "pool_addresses_provider": "0x46Dcd5F4600319b02649Fd76B55aA6c1035CA478",
    },
    "AaveV3Ink": {
        "chain_id": 57073,
        "pool_addresses_provider": "0x4172E6aAEC070ACB31aaCE343A58c93E4C70f44D",
    },
    "AaveV3Plasma": {
        "chain_id": 9745,
        "pool_addresses_provider": "0x061D8e131F26512348ee5FA42e2DF1bA9d6505E9",
    },
}

# ── Chain ID → RPC URL ──────────────────────────────────────────────────
# BlockPI key is Ethereum-only. Use Infura for supported chains, public RPCs for others.
RPC_URLS: dict[int, str] = {
    1:      f"https://ethereum.blockpi.network/v1/rpc/{BLOCKPI_KEY}",
    10:     f"https://optimism-mainnet.infura.io/v3/{INFURA_KEY}",
    42161:  f"https://arbitrum-mainnet.infura.io/v3/{INFURA_KEY}",
    137:    f"https://polygon-mainnet.infura.io/v3/{INFURA_KEY}",
    43114:  f"https://avalanche-mainnet.infura.io/v3/{INFURA_KEY}",
    8453:   f"https://base-mainnet.infura.io/v3/{INFURA_KEY}",
    100:    "https://rpc.gnosischain.com",
    1088:   "https://andromeda.metis.io/?owner=1088",
    56:     f"https://bsc-mainnet.infura.io/v3/{INFURA_KEY}",
    59144:  f"https://linea-mainnet.infura.io/v3/{INFURA_KEY}",
    534352: "https://rpc.scroll.io",
    324:    "https://mainnet.era.zksync.io",
    42220:  f"https://celo-mainnet.infura.io/v3/{INFURA_KEY}",
    5000:   "https://rpc.mantle.xyz",
    146:    "https://rpc.soniclabs.com",
    1868:   "https://rpc.soneium.org",
    4326:   "https://rpc0.megaeth.com",
    57073:  "https://rpc-gel.inkonchain.com",
    9745:   "https://rpc.plasma.digital",
}


def get_rpc_url(chain_id: int) -> str | None:
    """Get the RPC URL for a chain, or None if not available."""
    return RPC_URLS.get(chain_id)
