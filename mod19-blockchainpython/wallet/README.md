# Multi-Blockchain Wallet in Python

## Overview

This supports a user's ability to derive testnet BitCoin and Ethereum crypto wallets from a cryptocurrency account and send transactions between wallets via Python in a command line interface. 

## Dependencies

In order to run, you must ensure that:
* The [hd-wallet-derive](https://github.com/dan-da/hd-wallet-derive) repo is added into the "wallet" directory. It was not possible to push the repo to GitHub with this included in it.  
* The following libraries and technologies are installed in your developer environment:
  * Web3
  * Bit
  * PHP
  * [Ganache](https://www.trufflesuite.com/ganache)
  

### 1. Generate Mnemonic Code

Go to BIP39 mnemonic code converter [tool](https://iancoleman.io/bip39/) and generate mnemonic phrase. 


### 2. Launch private ETH blockchain

Download, install and use **Ganache** to launch private ETH blockchain through the pre-generated mnemonic phrase.
- url: http://127.0.0.1:7545
- network ID: 5777
- coin: ETH
    
!['ganache'](Images/Ganache_Mod19.png)
	
	
### 3. Clone `hd-wallet-derive` Github
Clone `hd-wallet-derive` to local directory and install by entering the following commands in git-bash:
    ```bash
    - git clone https://github.com/dan-da/hd-wallet-derive
    - cd hd-wallet-derive
    - php -r "readfile('https://getcomposer.org/installer');" | php
    - php -d pcre.jit=0 composer.phar install
    ```
	
!['hd-derive-wallet'](Images/hd-wallet-derive.png)
	
    Use `pypl` to install python library `bit` and `web3` are installed thru:
    ```shell
    pip install bit
    pip install web3
    ```

###  4. Setting Mnemonic Phrase
Within wallet directory, create `.env file` (no extension type) to store your mnemonic phrase under an object named `MNEMONIC`.

- Set this mnemonic as an environment variable, and include the one you generated as a fallback using:
  `mnemonic = os.getenv('MNEMONIC', 'insert mnemonic here')`

```python
mnemonic = os.getenv('MNEMONIC')
print(mnemonic)
```

###  5. Install wallet.py

Within wallet directory, run `wallet.py` in Anaconda Prompt.
- `python wallet.py`

The [wallet.py](wallet.py) file supports the following coins:

    | Coin | Symbol | Global Variable |
    | --- | --- | --- |
    | Ethereum | `eth` | `ETH` |
    | Bitcoin Testnet | `btc-test` | `BTCTEST` |


###  6. How to use functions to transfer coins?

To transfer coins, use these functions in Anaconda Prompt,
- `from wallet import *`

- `create_tx(COIN_NAME,"ADD SENDER ACCOUNT","ADD RECIPIENT ACCOUNT",AMOUNT)`
```send_tx(ETH, eth_pk_acct1, eth_pk_acct2.address, 1)```

- `send_tx(COIN_NAME,"ADD SENDER ACCOUNT","ADD RECIPIENT ACCOUNT",AMOUNT)`
```# send_tx(BTCTEST, btc_pk_acct1, btc_pk_acct2.address, 0.001)```


###  7. Expand the Wallet!

To expand the account, update the number of accounts desired in variable `number` in `wallet.py`.

Add different coins in `wallet.py` to expand access to various cryptos.
