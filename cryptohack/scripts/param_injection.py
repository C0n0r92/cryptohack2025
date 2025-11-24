from pwn import *
from Crypto.Cipher import AES
import hashlib
import json

conn = remote('socket.cryptohack.org', 13371)

conn.recvuntil(b'Intercepted from Alice: ')
alice = json.loads(conn.recvline())

conn.sendlineafter(b'Send to Bob: ', json.dumps({"p": alice["p"], "g": alice["g"], "A": alice["p"]}).encode())
conn.recvuntil(b'Intercepted from Bob: ')
conn.recvline()

conn.sendlineafter(b'Send to Alice: ', json.dumps({"B": alice["p"]}).encode())
conn.recvuntil(b'Intercepted from Alice: ')
flag_data = json.loads(conn.recvline())

conn.close()

key = hashlib.sha1(b'0').digest()[:16]
cipher = AES.new(key, AES.MODE_CBC, bytes.fromhex(flag_data['iv']))
print(cipher.decrypt(bytes.fromhex(flag_data['encrypted_flag'])))
