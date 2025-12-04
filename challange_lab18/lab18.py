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
    # Based on Wikipedia's LFSR example
    feedback = ((reg >> taps[0]) ^ (reg >> taps[1])) & 1
    output_bit = reg & 1                        # rightmost bit falls out
    shifted = reg >> 1                          # shift everything right
    new_reg = shifted | (feedback << (size - 1))  # put feedback at left end
    return new_reg, output_bit

@jit(nopython=True)
def get_keybyte(lfsr12, lfsr19):
    keybyte = 0
    for i in range(8):
        lfsr12, bit1 = clock(lfsr12, TAPS_12, 12)
        lfsr19, bit2 = clock(lfsr19, TAPS_19, 19)
        keybyte += (bit1 + bit2) << i  # add bits (from diagram)
    return lfsr12, lfsr19, keybyte % 255

@jit(nopython=True)
def find_keys(cipher, header):
    for state12 in range(4096):       # try all 2^12 starting states
        for state19 in range(524288): # try all 2^19 starting states
            # test this key combination
            lfsr12, lfsr19 = state12, state19
            match = True
            for i in range(4):
                lfsr12, lfsr19, keybyte = get_keybyte(lfsr12, lfsr19)
                if (keybyte ^ cipher[i]) != header[i]:
                    match = False
                    break
            if match:
                return state12, state19
    return 0, 0

if __name__ == '__main__':
    cipher = np.frombuffer(open('flag.enc', 'rb').read(), dtype=np.uint8)
    png_header = np.array([0x89, 0x50, 0x4E, 0x47], dtype=np.uint8)  # PNG magic bytes
    
    print("Searching for keys...")
    key12, key19 = find_keys(cipher, png_header)
    print(f"Found keys: LFSR-12={key12}, LFSR-19={key19}")
    
    # decrypt the whole file using the found keys
    lfsr12, lfsr19 = key12, key19
    decrypted = []
    for byte in cipher:
        lfsr12, lfsr19, keybyte = get_keybyte(lfsr12, lfsr19)
        decrypted.append(byte ^ keybyte)
    
    open('flag.png', 'wb').write(bytes(decrypted))
    print("Saved to flag.png")
