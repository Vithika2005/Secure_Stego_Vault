from crypto.pqc_wrapper import hybrid_encrypt, hybrid_decrypt

msg = b"post-quantum secrets"

blob = hybrid_encrypt(msg)
print("Encrypted length:", len(blob))

plain = hybrid_decrypt(blob)
print("Recovered:", plain)
