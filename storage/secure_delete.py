import os

def secure_delete(file_path: str, passes: int = 3):
    if not os.path.exists(file_path):
        return

    size = os.path.getsize(file_path)

    with open(file_path, "ba+", buffering=0) as f:
        for _ in range(passes):
            f.seek(0)
            f.write(os.urandom(size))

    os.remove(file_path)
