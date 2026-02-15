from crypto.aes_gcm import encrypt, decrypt

data = b"hello vault"
pwd = "test123"

blob = encrypt(data, pwd)
assert decrypt(blob, pwd) == data
print("Crypto OK")
