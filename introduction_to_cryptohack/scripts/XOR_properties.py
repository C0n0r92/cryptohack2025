import sys
import base64
import Crypto.Util.number as Cnum
import pwn


# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_XOR_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"

KEY1 = bytes.fromhex(KEY1)
K2_XOR_K1 = bytes.fromhex(KEY2_XOR_KEY1)

KEY2 = pwn.xor(K2_XOR_K1, KEY1)
print("KEY2 :", KEY2.hex())

# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1

K2_XOR_K3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")

KEY3 = pwn.xor(K2_XOR_K3, KEY2)



# f22531d50aa3bd789d86fe40b22777964bc1b3eed6f631be5e39a42665d106acea799adffe43e77470c34bc7e5b9d3f235bb0e3c


FLAG_xor_all = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
FLAG = pwn.xor(FLAG_xor_all, KEY1, KEY2, KEY3)
print("FLAG:", FLAG.decode('ascii'))


