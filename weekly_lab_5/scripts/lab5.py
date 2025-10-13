from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import sys
import binascii

def encrypt(plaintext, key, mode):
    encobj = AES.new(key, mode)
    return(encobj.encrypt(plaintext))

def decrypt(ciphertext, key, mode):
    encobj = AES.new(key, mode)
    return(encobj.decrypt(ciphertext))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python lab5.py <plaintext> <key>")
        sys.exit(1)
    
    val = sys.argv[1]
    password = sys.argv[2]
    plaintext = val
    
    key = hashlib.sha256(password.encode()).digest()
    plaintext = pad(plaintext.encode(), 16, style='pkcs7')
    print("After padding (CMS): " + binascii.hexlify(bytearray(plaintext)).decode())
    
    ciphertext = encrypt(plaintext, key, AES.MODE_ECB)
    print("Cipher (ECB): " + binascii.hexlify(bytearray(ciphertext)).decode())
    
    plaintext = decrypt(ciphertext, key, AES.MODE_ECB)
    plaintext = unpad(plaintext, 16, style='pkcs7').decode()
    print("Decrypt: " + plaintext)
    
    plaintext = val
