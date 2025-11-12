import requests
from Crypto.Util.strxor import strxor

ciphertext = (b'\x00' * 32).hex()
error = requests.get(f"http://aes.cryptohack.org/lazy_cbc/receive/{ciphertext}/").json()["error"]
CD = bytes.fromhex(error.split("Invalid plaintext: ")[1])

key = strxor(CD[:16], CD[16:])

print(bytes.fromhex(requests.get(f"http://aes.cryptohack.org/lazy_cbc/get_flag/{key.hex()}/").json()["plaintext"]))