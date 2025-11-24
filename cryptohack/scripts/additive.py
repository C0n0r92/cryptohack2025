from pwn import *
from Crypto.Cipher import AES
import hashlib, json

r = remote('socket.cryptohack.org', 13380)
r.recvuntil(b'Alice: ')
a = json.loads(r.recvline())
r.recvuntil(b'Bob: ')
b = json.loads(r.recvline())
r.recvuntil(b'Alice: ')
f = json.loads(r.recvline())
r.close()

p = int(a['p'], 16)
A = int(a['A'], 16)
B = int(b['B'], 16)
g = int(a['g'], 16)

shared = A * B * pow(g, -1, p) % p
key = hashlib.sha1(str(shared).encode()).digest()[:16]
print(AES.new(key, AES.MODE_CBC, bytes.fromhex(f['iv'])).decrypt(bytes.fromhex(f['encrypted'])))
