# CryptoHack Lab 11 - Multi-layer Decryption

## Challenge
Decrypt an intercepted message that has been encrypted using multiple layers of:
- Character substitution cipher
- Base64 encoding
- Caesar cipher (shift 4)

## Solution

**Decrypted Message:** `Why do elephants have big ears?`

## Approach

The encryption prepends an operation number (1, 2, or 3) before each layer:
- `1` = Character substitution
- `2` = Base64 encoding
- `3` = Caesar cipher

To decrypt:
1. Read the first digit
2. Remove that digit
3. Apply the reverse operation
4. Repeat until no more leading digits

## Implementation

```python
# Three reverse operations
reverse_step1()  # Undo character substitution
reverse_step2()  # Base64 decode
reverse_step3()  # Reverse Caesar cipher
```

## Execution

```bash
python3 lab11.py
```

## Results

- **Encryption layers:** 68
- **Original message length:** 35,138 characters
- **Decrypted message length:** 31 characters
- **Final message:** Why do elephants have big ears?

## Verification

The final base64 string before decryption:
```
V2h5IGRvIGVsZXBoYW50cyBoYXZlIGJpZyBlYXJzPw==
```

Verify independently:
```bash
echo "V2h5IGRvIGVsZXBoYW50cyBoYXZlIGJpZyBlYXJzPw==" | base64 -d
```

Output: `Why do elephants have big ears?`
