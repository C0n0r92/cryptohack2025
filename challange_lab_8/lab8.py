import hashlib

# Tomtom's hash
tomtom_hash = '06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2'

# Common weak passwords
passwords = ['12345', '54321', '11111', '99999', '123456', '654321', '1234567']

# Try all 5-digit salts (00000 to 99999)
for salt_num in range(100000):
    salt = str(salt_num).zfill(5)  # Make it 5 digits with leading zeros

    for password in passwords:
        # Try salt+password
        test1 = hashlib.sha1((salt + password).encode()).hexdigest()
        if test1 == tomtom_hash:
            print(f"FOUND! Salt: {salt}, Password: {password}, Mode: salt+pass")
            exit()

        # Try password+salt
        test2 = hashlib.sha1((password + salt).encode()).hexdigest()
        if test2 == tomtom_hash:
            print(f"FOUND! Salt: {salt}, Password: {password}, Mode: pass+salt")
            exit()

    # Show progress every 10000
    if salt_num % 10000 == 0:
        print(f"Tested {salt_num} salts...")

print("Not found with these passwords")