from stego.lsb_engine import encode_lsb, decode_lsb

encode_lsb("assets/sample.png", b"secret", "data/test.png")
assert decode_lsb("data/test.png") == b"secret"
print("Stego OK")
