from crypto.integrity import generate_hmac, verify_hmac

data = b"secret vault data"
key = b"masterkey"

mac = generate_hmac(data, key)
print("MAC:", mac.hex())

# Valid case
print("Valid:", verify_hmac(data, key, mac))

# Tampered case
tampered = b"secret vault data!"
print("Tampered:", verify_hmac(tampered, key, mac))
