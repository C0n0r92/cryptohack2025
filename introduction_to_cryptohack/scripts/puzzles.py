import pwn

crack = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for key in range(256):
    decoded = pwn.xor(crack, key).decode('ascii', errors='ignore')
    if 'crypto{' in decoded: print(f"Key: {key}\nFlag: {decoded}")