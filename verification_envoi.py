from web3 import Web3
import time

RPC_URL = "http://10.229.43.182:8545"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.is_connected():
    print("Connexion échouée à la blockchain")
    exit()

last_block = web3.eth.block_number

for block_number in range(0, last_block + 1):
    try:
        block = web3.eth.get_block(block_number, full_transactions=True)
       
        for tx in block.transactions:
            if tx.input and tx.input != '0x' and tx['from'] == '0x75f81784678369d1C71B2EE3C0edAa6E0aFB48Ad':
                    print(f"\nBloc #{block_number}")
                    print(f"  Tx Hash     : {tx.hash.hex()}")
                    print(f"  From        : {tx['from']}")
                    print(f"  To          : {tx.to}")
                    print(f"  Value (ETH) : {web3.from_wei(tx.value, 'ether')}")
                    print(f"  Data        : {tx.input}")
       
        if block_number % 100 == 0:
            print(f"--> Jusqu'au bloc {block_number} traité")
            time.sleep(0.05)  # Pour limiter la charge
 
    except Exception as e:
        print(f"Erreur au bloc {block_number} : {e}")
        continue