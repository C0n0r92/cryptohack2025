from Crypto.Cipher import AES
import hashlib

ct = bytes.fromhex("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66")

try:
    words = open("/usr/share/dict/words").read().split()
except:
    words = open("words.txt").read().split()

for word in words:
    key = hashlib.md5(word.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    pt = cipher.decrypt(ct)
    
    if b'crypto' in pt:
        print(pt)
        break
