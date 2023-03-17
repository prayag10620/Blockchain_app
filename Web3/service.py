from web3 import Web3 , HTTPProvider
from dotenv import load_dotenv , find_dotenv
import os

load_dotenv()


INFURA_KEY = os.getenv('INFURA_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')


web3 = Web3(HTTPProvider(f'https://goerli.infura.io/v3/{INFURA_KEY}'))

# print(web3.isConnected())

def get_block_by_num(block_no):
    try:
        block = web3.eth.get_block(int(block_no))
        print(block)
        if block:
            return block
        else:
            return 'Block not found', 404
        
    except Exception as e:
        print(e)
        return 'Server error', 500
    

def get_block_by_hash(block_hash):
    try:
        
        block = web3.eth.get_block(block_hash)
         

        if block:
            return block
        else:
            return 'Block not Found',404
        
    except Exception as e:
        print(e)
        return 'Server Error' , 500



def get_trasaction_data(transaction_hash):
    try:
        tx = web3.eth.get_transaction(transaction_hash)

        if tx:
            return tx
        else:
            return 'Transaction not found', 404
        
    except Exception as e:
        print(e)
        return 'Server error', 500
    

def get_account_balance():
    balance = web3.eth.get_balance('0x125000e5d0092537D52900a87b751260A0F3D9d5')
    return balance
    

