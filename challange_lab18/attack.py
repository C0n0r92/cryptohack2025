#!/usr/bin/env python3
"""
LFSR cracker - brute forces the key by checking against known PNG header.
Uses numba because pure python was way too slow (~2hrs vs ~1min)
"""
from numba import jit
import numpy as np

# tap positions from the diagram (had to convert - diagram counts from left, we count from right)
TAPS_12 = (10, 5)  
TAPS_19 = (14, 8)

@jit(nopython=True)
def clock(reg, taps, size):
    # standard LFSR: xor taps -> feedback, shift right, feedback goes to top bit
    feedback = ((reg >> taps[0]) ^ (reg >> taps[1])) & 1
    return (reg >> 1) | (feedback << (size-1)), reg & 1

@jit(nopython=True)
def get_keybyte(reg1, reg2):
    keybyte = 0
    for i in range(8):
        reg1, bit1 = clock(reg1, TAPS_12, 12)
        reg2, bit2 = clock(reg2, TAPS_19, 19)
        keybyte += (bit1 + bit2) << i  # bits get added, not xored (weird but thats how it works)
    return reg1, reg2, keybyte % 255

@jit(nopython=True)
def crack(cipher, header):
    for key1 in range(4096):       # 2^12
        for key2 in range(524288): # 2^19
            reg1, reg2 = key1, key2
            for i in range(4):
                reg1, reg2, keybyte = get_keybyte(reg1, reg2)
                if (keybyte ^ cipher[i]) != header[i]:
                    break
            else:
                return key1, key2  # found it
    return 0, 0

if __name__ == '__main__':
    cipher = np.frombuffer(open('flag.enc', 'rb').read(), dtype=np.uint8)
    png_header = np.array([0x89, 0x50, 0x4E, 0x47], dtype=np.uint8)  # PNG magic bytes
    
    print("Cracking...")
    key1, key2 = crack(cipher, png_header)
    print(f"Keys: {key1}, {key2}")
    
    # decrypt
    reg1, reg2 = key1, key2
    decrypted = []
    for byte in cipher:
        reg1, reg2, keybyte = get_keybyte(reg1, reg2)
        decrypted.append(byte ^ keybyte)
    
    open('flag.png', 'wb').write(bytes(decrypted))
    print("Done!")
