from Crypto.PublicKey import RSA

f = open('../misc/key.pem','r')
key = RSA.importKey(f.read())

print(key.d)