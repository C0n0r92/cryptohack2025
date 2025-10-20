import requests

url = "http://aes.cryptohack.org/triple_des"

k = (b'\x00'*8 + b'\xff'*8).hex()

r = requests.get(f"{url}/encrypt_flag/{k}/")
flag_enc = bytes.fromhex(r.json()["ciphertext"])

r = requests.get(f"{url}/encrypt/{k}/{flag_enc.hex()}/")
result = bytes.fromhex(r.json()["ciphertext"])

print(result)
