from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import hashlib
import sys
import binascii
import base64

def encrypt(plaintext, key, mode):
    encobj = DES.new(key, mode)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext, key, mode):
    encobj = DES.new(key, mode)
    return(encobj.decrypt(ciphertext))

if __name__ == "__main__":

    ciphertext_base64 = sys.argv[1]
    password = sys.argv[2]
    
    key = hashlib.sha256(password.encode()).digest()[:8]
    ciphertext = base64.b64decode(ciphertext_base64)
    print("Hex: " + binascii.hexlify(ciphertext).decode())
    
    plaintext = decrypt(ciphertext, key, DES.MODE_ECB)
    try:
        plaintext = unpad(plaintext, 8, style='pkcs7').decode()
        print("Decrypt: " + plaintext)
    except ValueError:
        try:
            plaintext = plaintext.decode()
            print("Decrypt: " + plaintext)
        except UnicodeDecodeError:
            print("Decrypt (hex): " + binascii.hexlify(plaintext).decode())
            print("Error: Could not decode - possibly wrong key")
