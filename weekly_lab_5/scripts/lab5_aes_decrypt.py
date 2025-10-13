from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import sys
import binascii
import base64

def encrypt(plaintext, key, mode):
    encobj = AES.new(key, mode)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext, key, mode):
    encobj = AES.new(key, mode)
    return(encobj.decrypt(ciphertext))

if __name__ == "__main__":

    ciphertext_base64 = sys.argv[1]
    keys_to_try = ["hello", "ankle", "changeme", "123456"]
    
    ciphertext = base64.b64decode(ciphertext_base64)
    print("Hex: " + binascii.hexlify(ciphertext).decode())
    
    for password in keys_to_try:
        key = hashlib.sha256(password.encode()).digest()
        plaintext = decrypt(ciphertext, key, AES.MODE_ECB)
        try:
            plaintext = unpad(plaintext, 16, style='pkcs7').decode()
            print("Decrypt: " + plaintext)
            print("Key: " + password)
        except:
            print("Error with key: " + password)
