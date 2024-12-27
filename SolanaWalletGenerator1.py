import solders
import base58



def generate_wallet():
    keypair = solders.keypair.Keypair() 
    generated_address = keypair.pubkey()
    return keypair, generated_address

def get_pubkey(keypair):
    rawPublicKey = bytes(keypair)
    PublicKey58 = base58.b58encode(rawPublicKey).decode()    
    return rawPublicKey, PublicKey58

def get_keypair_list(keypair):
    keypair_bytes = base58.b58decode(keypair)
    keypair_list = list(keypair_bytes)
    return keypair_list

def keypair_list_to_keypair(keypair_list):
    keypair = solders.keypair.Keypair.from_bytes(bytes(keypair_list))
    return keypair

def restore_keypair(public_key):
    restoredKeypair = solders.keypair.Keypair.from_base58_string(public_key)
    restoredAddr = restoredKeypair.pubkey()
    return restoredKeypair, restoredAddr
    

keypair, generated_address = generate_wallet()
print("keypair", keypair)
print("generated_address", generated_address, "\n")

rawPublicKey, PublicKey58 = get_pubkey(keypair)
print("rawPublicKey", rawPublicKey, "\n")
print("PublicKey58", PublicKey58, "\n")

keypair_list = get_keypair_list(PublicKey58)
print("keypair_list", keypair_list, "\n")

keypair = keypair_list_to_keypair(keypair_list)
print("keypair", keypair, "\n")
wallet_address = keypair.pubkey()
print("wallet_address", wallet_address, "\n")

restoredKeypair, restoredAddr = restore_keypair(PublicKey58)
print("restoredKeypair", restoredKeypair)
print("restoredAddr", restoredAddr)
