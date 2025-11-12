import requests
from Crypto.Util.number import long_to_bytes, bytes_to_long

def xor(a, b):
    return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))

cookie = bytes.fromhex(requests.get("http://aes.cryptohack.org/flipping_cookie/get_cookie/").json()["cookie"])

given = b'admin=False;expi'
expected = b'admin=True;\x05\x05\x05\x05\x05'

iv = cookie[:16]
block1 = cookie[16:32]

new = xor(xor(given, expected), iv)

url = f"http://aes.cryptohack.org/flipping_cookie/check_admin/{block1.hex()}/{new.hex()}/"
print(requests.get(url).json())