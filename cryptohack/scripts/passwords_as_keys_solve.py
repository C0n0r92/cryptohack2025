from Crypto.Cipher import AES
import hashlib
import requests

ciphertext = bytes.fromhex(requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/').json()['ciphertext'])

words = requests.get("https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words").text.split()

for word in words:
    key = hashlib.md5(word.encode()).digest()
    plaintext = AES.new(key, AES.MODE_ECB).decrypt(ciphertext)
    if plaintext.startswith(b'crypto{'):
        print(plaintext.decode())
        break
