import os

def write_file(path, data: bytes):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)

def read_file(path) -> bytes:
    with open(path, "rb") as f:
        return f.read()
