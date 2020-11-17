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


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
w3.middleware_onion.inject(geth_poa_middleware, layer =0)
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)


print(w3.isConnected())
print(w3.eth.blockNumber)


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



def priv_key_to_account (coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)


def create_raw_tx(account, recipient, amount):
    gasEstimate = web3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": web3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": web3.eth.getTransactionCount(account.address),
    }


def create_tx(coin,account,to,amount):
    if (coin==ETH):
        return create_raw_tx(account,to,amount)
    else:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])


def send_tx(coin, account, recipient, amount):
    
    raw_tx = create_tx(coin, account, recipient, amount)
    signed_tx = account.sign_transaction(raw_tx)
    
    if coin == ETH:
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return result
    elif coin == BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(signed_tx)


eth_pk_acct1 = priv_key_to_account(ETH, coins['eth'][0]['privkey'])
eth_pk_acct2 = priv_key_to_account(ETH, coins['eth'][1]['privkey'])
eth_pk_acct3 = priv_key_to_account(ETH, coins['eth'][2]['privkey'])

btc_pk_acct1 = priv_key_to_account(BTCTEST, coins['btc-test'][0]['privkey'])
btc_pk_acct2 = priv_key_to_account(BTCTEST, coins['btc-test'][1]['privkey'])
btc_pk_acct3 = priv_key_to_account(BTCTEST, coins['btc-test'][2]['privkey'])

# sending ETH transaction
# send_tx(ETH, eth_pk_acct1, eth_pk_acct2.address, 1)

# sending BTCTEST transaction
# send_tx(BTCTEST, btc_pk_acct1, btc_pk_acct2.address, 0.001)