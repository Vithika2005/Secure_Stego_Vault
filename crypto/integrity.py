import hmac
import hashlib

HMAC_KEY_SIZE = 32

def generate_hmac(key: bytes, data: bytes) -> bytes:
    """Generate HMAC-SHA256 for data."""
    return hmac.new(key, data, hashlib.sha256).digest()

def verify_hmac(key: bytes, data: bytes, tag: bytes) -> bool:
    """Verify HMAC tag."""
    expected = generate_hmac(key, data)
    return hmac.compare_digest(expected, tag)
