# 🔐 SIDH Key Exchange with AES Encryption

This project simulates a simplified version of the SIDH (Supersingular Isogeny Diffie–Hellman) key exchange using random key generation, combined with AES encryption for secure messaging.

## 📌 Features

- Simulated SIDH key pair generation  
- Shared secret computed using SHA-256  
- AES encryption using the shared secret as key  
- Message decryption after verifying shared hash  

## 🚀 How It Works

1. Generates key pairs for Alice and Bob.
2. Computes shared secret from keys (using SHA-256).
3. Encrypts user message with AES (CBC).
4. Decrypts only if the correct shared secret hash is provided.

## ▶ Usage

Make sure pycryptodome is installed:

```bash
pip install pycryptodome
python sidh_1.py
