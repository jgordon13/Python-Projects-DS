# Author: Julia Gordon 
# Date: 4/1/2022
# HW 8/Hw 9: Create an implementation of the El Gamal Encryption with Python.

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





'''plainText = [dict([key, int(value)]
    for key, value in dicts.items())
    for dicts in letToNum]  '''    
'''plainText = []

for c in M.lower(): 
    if c.isalpha():
        plainText += letToNum[c]
    else: 
        plainText += c '''

# Modular exponentiation (i googled this because the regular power built in functino would not except three input variables)
'''def power(baseVal, powerVal, primeVal):
    x = 1
    y = baseVal
    while powerVal > 0:
        if powerVal % 2 != 0:
           x = (x * y) % primeVal
        y = (y * y) % primeVal
        powerVal = int(powerVal / 2)
    return x % primeVal'''
 
# Encryption
'''def encrypt(M, q, h, g):
    cipherText = []                                 # empty list to store the cipher text 
    keyValues = getKeys(q)                                   # Private key for sender
    s = power(h, k, q)                              # this represents the shared secret key
    p = power(g, k, q)                              # this reprecents the C_1
    for i in range(0, len(M)):                      # starting the encryption for each letter in the range of the length of the message
        cipherText.append(M[i])                     # we are going to append each letter in M to the ciphertext message 
    for i in range(0, len(cipherText)):             # here we are running a loop for each letter in the range of the length of the cipher text 
        cipherText[i] = s * ord(cipherText[i])      # and we are using the shared secret times the order of the cipher text to encrypt it 
    return cipherText, p                            # returning the cipher text the q value

# Decryption
def decrypt(cipherText, p, key, q):                     # here we are starting the decryption process
    plainText = []                                      # this is the empty list to put the plaintext 
    h = power(p, key, q)                                # here we are the inverse of s using the gen key and the shared key
    for i in range(0, len(cipherText)):                 # this is a for loop for each letter in the range of the length of the cipher text
        plainText.append(chr(int(cipherText[i]/h)))     # we are going to append each character of the cipher text divided by h to the plaintext
    return plainText                                    # returing the plain text
 

M = 'Hello World'                                       # the orinal message that we want to send from one party to the other
print("Original Message :", M)                          # here we are just printing out the orignal message we want to send
 
q = random.randint(pow(10, 20), pow(10, 50))             
g = random.randint(2, q)                                
 
privateKey = genKey(q)                                  # Private key for receiver
h = power(g, privateKey, q)                             
 
cipherText, p = encrypt(M, q, h, g)                     
plainText = decrypt(cipherText, p, privateKey, q)       

m = ''.join(plainText)                                  
print("Decrypted Message :", m)  '''                       

print("-----------------------------------------------------------------")

