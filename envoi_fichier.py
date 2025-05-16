from web3 import Web3
import json

RPC_URL = "http://10.229.43.182:8545"
PRIVATE_KEY = "8cbe7c612e2a0f636008d64c0f2983b89ffb89b1fcb0f0a89cf438c8b68e727b"
SENDER_ADDRESS = "0x75f81784678369d1C71B2EE3C0edAa6E0aFB48Ad"

web3 = Web3(Web3.HTTPProvider(RPC_URL))
if not web3.is_connected():
    print("Connexion échouée à la blockchain")
    exit()

print("Connecté à la blockchain")
nonce = web3.eth.get_transaction_count(SENDER_ADDRESS)

metadata = {
    "name": "hash_joel.pdf",
    "hash": "7518adb0c87101e93813dbf28f21764d4549406942bb5478016baf9e5c12c4e5",
    "path": r"N:\Commun\ELEVE\INFO\SI-C2b\4emeTrimestre\C107\hast_joel-pdf",
    "description": "Exemple de fichier PDF"
}

transaction = {
    'from': SENDER_ADDRESS,
    'to': "0x0000000000000000000000000000000000000000",
    'value': 0,
    'gas': 200000,
    'gasPrice': web3.to_wei('20', 'gwei'),
    'nonce': nonce,
    'chainId': 32383,
    'data': json.dumps(metadata).encode('utf-8')
}

signed_tx = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

print(f"Transaction envoyée à la blockchain avec le hash : {web3.to_hex(tx_hash)}")

with open("tx_hash.txt", "w") as file:
    file.write(web3.to_hex(tx_hash))