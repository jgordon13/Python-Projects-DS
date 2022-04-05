# Author: Julia Gordon 
# date: 3/7/2022
# Homework 6 Cipher Problem
# Create an implementation of the Affine cipher with Python. 
# The Affine cipher is a simple substitution cipher.  Cipher Each character is mapped to 
# its numeric equivalent, encrypted with a mathematical function and then convert to the 
# letter relating to its new numeric value.

import re
lToI = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}

iToL = {
    "0": "a",
    "1": "b",
    "2": "c",
    "3": "d",
    "4": "e",
    "5": "f",
    "6": "g",
    "7": "h",
    "8": "i",
    "9": "j",
    "10": "k",
    "11": "l",
    "12": "m",
    "13": "n",
    "14": "o",
    "15": "p",
    "16": "q",
    "17": "r",
    "18": "s",
    "19": "t",
    "20": "u",
    "21": "v",
    "22": "w",
    "23": "x",
    "24": "y",
    "25": "z"
}

print("------------------")
key = [3,5]
plainText = input("enter plain text: ")
cipherText= input("enter cipher text: ")

def EncodeCipher(plainText, key): # encipher equation E(x)=(ax+b) mod 26
    cipherText = "" 
    for c in plainText.lower(): #for loop that runs every character in the plaintext and makes it capitalized 
        if c.isalpha(): 
            tmp = lToI[c] * key[0] + key[1]
            cipherText += iToL[str((tmp) % 26)] #[((key[0] * L2I[c]) + key[1]) % 26 ] # if the character is in the alphabet we run it through the encryption equation 
        else: 
            cipherText += c # we attach it to the cipher text
    return cipherText


def DecodeCipher(cipherText, key): # D(y) = (a^-1)(y - b) mod 26
    plainText = ""
    inverse = -1 # this is setting the inverse equal to -1 the entire time
    for x in range(26):
        if (key[0] % 2 == 0 or key[0] % 13 == 0):
            raise ValueError("the first key doesn't have an inverse")
        if (key[0] * x) % 26 == 1:
            x = inverse
    for c in cipherText.upper():
        if c.isalpha(): 
            plainText += iToL[str((inverse * (lToI[c] - key[1])) % 26)]
        else: 
            x += c
    return x

#print('Encrypted text: ', EncodeCipher(plainText,key))
print('Decrypted text: ', DecodeCipher(cipherText, key))

print("------------------")


