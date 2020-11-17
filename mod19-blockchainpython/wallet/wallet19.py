from constants import *
import subprocess
import json
import os
import requests
from dotenv import load_dotenv
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from bit import wif_to_key, PrivateKeyTestnet
from bit.network import NetworkAPI
from eth_account import Account

load_dotenv()



def derive_wallets (coin, number):
    mnemonic = os.getenv('MNEMONIC')
    command = f"php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic='{mnemonic}' --coin='{coin}' --numderive='{number}' --cols=address,index,path,address,privkey,pubkey,pubkeyhash,xprv,xpub --format=json"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = process.communicate()
    process_status = process.wait()
    keys = json.loads(output)
    return keys


def coins ():

    coin_dict = {
        'btc-test' : derive_wallets(mnemonic, BTCTEST, 3),
        'eth' : derive_wallets(mnemonic, ETH, 3)
        }
    return coin_dict


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
w3.middleware_onion.inject(geth_poa_middleware, layer =0)
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

print(w3.isConnected())

print(w3.eth.blockNumber)

def priv_key_to_account (coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

eth_pk_acct1 = priv_key_to_account(ETH, coins['eth'][0]['privkey'])
eth_pk_acct2 = priv_key_to_account(ETH, coins['eth'][1]['privkey'])
eth_pk_acct3 = priv_key_to_account(ETH, coins['eth'][2]['privkey'])

btc_pk_acct1 = priv_key_to_account(BTCTEST, coins['btc-test'][0]['privkey'])
btc_pk_acct2 = priv_key_to_account(BTCTEST, coins['btc-test'][1]['privkey'])
btc_pk_acct3 = priv_key_to_account(BTCTEST, coins['btc-test'][2]['privkey'])