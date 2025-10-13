import pwn
from itertools import cycle

# Challenge 1: Single-byte XOR
cipher1 = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for key in range(256):
    decoded = pwn.xor(cipher1, key).decode('ascii', errors='ignore')
    if 'crypto{' in decoded:
        print(f"Challenge 1 - Key: {key}, Flag: {decoded}")

# Challenge 2: Multi-byte repeating XOR
cipher2 = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

partial_key = pwn.xor(cipher2[:7], b"crypto{")
for char in "abcdefghijklmnopqrstuvwxyz":
    key = (partial_key.decode() + char).encode()
    extended_key = bytes(k for k, _ in zip(cycle(key), cipher2))
    decoded = pwn.xor(cipher2, extended_key).decode('ascii', errors='ignore')
    print(f"Challenge 2 - Key: {key}, Flag: {decoded}")