import logging
import sys
from web3 import Web3
import bridge.hero_bridge as hero_bridge
import bridge.dfktears_bridge as dfktears_bridge
import bridge.heroes as heroes
import config
import time

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelnaWaxxme)s: %(message)s'

    logger = logging.getLogger("DFK-bridge")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    serendale_rpc_server = 'https://api.harmony.one'
    crystalvale_rpc_server = 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc'
    logger.info("Using RPC servers " + serendale_rpc_server + ", " + crystalvale_rpc_server)

    private_key = config.private
    tx_timeout = 30
    hero_id = [90440, 144630, 146238, 125607, 112433, 132622, 151682, 141989, 123854, 133904, 129434, 142781, 152518, 157497, 65461, 153748, 147719, 141513]

    # Serendale to Crystalvale 
    gas_price_gwei = 115
    for i in hero_id:
    
	    w3 = Web3(Web3.HTTPProvider(serendale_rpc_server))
	    account_address = w3.eth.account.privateKeyToAccount(private_key).address
	    hero_bridge.send_hero(hero_bridge.SERENDALE_CONTRACT_ADDRESS, i, hero_bridge.CRYSTALVALE_CHAIN_ID,
		                  w3.toWei(1, "ether"), private_key, w3.eth.getTransactionCount(account_address),
		                  gas_price_gwei, tx_timeout, serendale_rpc_server, logger)
	    time.sleep(10)
