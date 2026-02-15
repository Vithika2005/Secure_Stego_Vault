"""
Post-Quantum Hybrid Encryption (SIMULATION)
-------------------------------------------
This simulates a hybrid scheme:
- AES-GCM encrypts data
- "PQC key" wraps the AES key (simulated)
"""

import os
from crypto.aes_gcm import encrypt, decrypt

# Simulated PQC key wrapping (NOT real PQC)
def _wrap_key(key: bytes) -> bytes:
    return key[::-1]  # reverse bytes (demo only)

def _unwrap_key(wrapped: bytes) -> bytes:
    return wrapped[::-1]

def hybrid_encrypt(data: bytes) -> bytes:
    # generate random AES key
    aes_key = os.urandom(32)

    # encrypt data with AES key
    encrypted = encrypt(data, aes_key.hex())

    # wrap AES key (simulate PQC)
    wrapped_key = _wrap_key(aes_key)

    # final blob = wrapped_key + encrypted
    return wrapped_key + encrypted

def hybrid_decrypt(blob: bytes) -> bytes:
    wrapped_key = blob[:32]
    encrypted = blob[32:]

    aes_key = _unwrap_key(wrapped_key)

    return decrypt(encrypted, aes_key.hex())
