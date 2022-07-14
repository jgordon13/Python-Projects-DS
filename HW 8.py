# Author: Julia Gordon 
# Date: 4/1/2022
# HW 8/Hw 9: Create an implementation of the El Gamal Encryption with Python.
# This is a rough code implementing the El Gamal Encryption (it does not work)

print("-----------------------------------------------------------------")

import random
from math import pow
import sympy 

import re
letToNum = {
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

numToLet = {
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

P = sympy.randprime(1000000, 100000000) 
print('The prime is- ',P)
M = '396' # this is the message that we want to send
print('Original Message- ', M)

# Key Generation: 
def getKeys(P): 
    g = 7   # the particular generator                          
    privateKey = random.randrange(2, 13) # this is private key format
    #print(privateKey)
    publicKey = (g ** privateKey) % P  # this is the public keys format
    return {publicKey: privateKey}     

aliceKeys = getKeys(P)  
X = list(aliceKeys.keys())[0] # alice Public Key
x = list(aliceKeys.values())[0] # alice Private key
print('Alices keys- ', aliceKeys)

# Encryption:
bobKeys = getKeys(P) 
Y = list(bobKeys.keys())[0] # bobs Public key
y = list(bobKeys.values())[0] # bobs Private key
print('Bobs keys- ', bobKeys) 

# i need to find a way to use the dictionary to transform M into numbers so it will run in the next step.
plainText = []
print(plainText)
        
c1 = Y     
c2 = (X ** y) * M         

# Decryption: 
cipher = (c1,c2)  
print(cipher)

cipherText = []
for i in range(0,len(M)):
    if M.isalpha ():
         m = c2 * ( (Y ** x) ) # = M
         m =+ cipherText
print('Decrypted Message- ', cipherText) 

print('---------------------------------------------------------------')