import requests

url = "http://aes.cryptohack.org/ecbcbcwtf"

r = requests.get(url + "/encrypt_flag/")
ct = r.json()["ciphertext"]

iv = ct[:32]
cipher = ct[32:]

r = requests.get(url + f"/decrypt/{cipher}/")
dec = r.json()["plaintext"]

iv_bytes = bytes.fromhex(iv)
dec_bytes = bytes.fromhex(dec)
cipher_bytes = bytes.fromhex(cipher)

result = []
for i in range(16):
    result.append(dec_bytes[i] ^ iv_bytes[i])

for block in range(1, len(dec_bytes)//16):
    for i in range(16):
        idx = block*16 + i
        prev_idx = (block-1)*16 + i
        result.append(dec_bytes[idx] ^ cipher_bytes[prev_idx])

flag = bytes(result).decode()
print(flag)
