#!/usr/bin/env python3
import hashlib

hashes = {
    'Security': 'fafa4483874ec051989d53e1e432ba3a6c6b9143',
    'Tomtom': '06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2',
    'Sparky': '2834da08d58330d8dafbb2ac1c0f85f6b3b135ef',
    'Mark123': '92e54f10103a3c511853c7098c04141f114719c1',
    'superman': '437fbc6892b38db6ac5bdbe2eab3f7bc924527d9',
    'JillC': 'f44f3b09df53c1c11273def13cacd8922a86d48c'
}

salt = 'www.exploringsecurity.com'

print(f"Cracking {len(hashes)} passwords with salt: {salt}")
print(f"Testing 6-digit passwords (000000-999999)...\n")

found = 0

for i in range(1000000):
    password = f"{i:06d}"
    test_hash = hashlib.sha1((salt + password).encode()).hexdigest()
    
    for username, user_hash in hashes.items():
        if test_hash == user_hash:
            print(f"FOUND: {username} | Password: {password}")
            found += 1
            if found == len(hashes):
                print(f"\nAll {len(hashes)} passwords cracked!")
                exit(0)

print(f"\nDone. Cracked {found}/{len(hashes)} passwords.")
