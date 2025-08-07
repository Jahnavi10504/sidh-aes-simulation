from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
import os

def sidh_generate_keypair():
    private_key = os.urandom(32)
    public_key = os.urandom(64)
    return private_key, public_key

def sidh_compute_shared_secret(private_key, other_public_key):
    combined = private_key + other_public_key
    combined_rev = other_public_key + private_key
    h1 = SHA256.new(combined).digest()
    h2 = SHA256.new(combined_rev).digest()
    return min(h1, h2)

def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return cipher.iv + ct_bytes

def decrypt(key, ciphertext):
    iv = ciphertext[:16]
    ct = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

def main():
    print("=== SIDH Key Exchange Simulation with AES Encryption ===\n")

    
    alice_priv, alice_pub = sidh_generate_keypair()
    bob_priv, bob_pub = sidh_generate_keypair()


    alice_shared = sidh_compute_shared_secret(alice_priv, bob_pub)
    bob_shared = sidh_compute_shared_secret(alice_priv, bob_pub) 

    assert alice_shared == bob_shared

    print(f"Shared secret (hash): {alice_shared.hex()}")

    aes_key = alice_shared[:16]

    plaintext = input("Enter message to encrypt: ")

    ciphertext = encrypt(aes_key, plaintext)
    print(f"Ciphertext (hex): {ciphertext.hex()}")

    input_hash = input("\nEnter the shared secret hash to decrypt message: ").strip().lower()

    if input_hash == alice_shared.hex():
        decrypted = decrypt(aes_key, ciphertext)
        print(f"Decrypted text: {decrypted}")
    else:
        print("Alert: Hash verification failed! Decryption aborted.")

if __name__ == "__main__":
    main()
