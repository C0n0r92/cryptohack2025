from Crypto.PublicKey import RSA

f = open('../misc/bruce_rsa.pub','r')
key = RSA.importKey(f.read())

print(key.n)
