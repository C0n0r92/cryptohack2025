#!/usr/bin/env python3
import string
from base64 import b64decode

INTERCEPTED_FILE = '/Users/conor.mcloughlin/Downloads/intercepted.txt'


def reverse_1(text):
    cipher_map = str.maketrans(
        "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON",
        "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA"
    )
    return text.translate(cipher_map)


def reverse_2(text):
    
    return b64decode(text).decode('utf-8', errors='ignore')


def reverse_3(text):
    loweralpha = string.ascii_lowercase
    shifted = loweralpha[-4:] + loweralpha[:-4]
    return text.translate(str.maketrans(loweralpha, shifted))


def decrypter(encrypted):
    ops = {'1': reverse_1, '2': reverse_2, '3': reverse_3}
    message = encrypted
    while message and message[0] in ops:
        message = ops[message[0]](message[1:])
    return message


if __name__ == '__main__':
    with open(INTERCEPTED_FILE, 'r') as f:
        print(decrypter(f.read().strip()))
