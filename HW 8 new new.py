# Author: Julia Gordon 
# Date:4/12/2022
# HW 8 final: Create an implementation of the El Gamal Encryption.
# this code is a final implemation of the El Gamal Encryption (it works 
# with string messages)

# find out how to convert from letters to numbers and back for next time.


import re
letToNum = {
    "a": '00',
    "b": '01',
    "c": '02',
    "d": '03',
    "e": '04',
    "f": '05',
    "g": '06',
    "h": '07',
    "i": '08',
    "j": '09',
    "k": '10',
    "l": '11',
    "m": '12',
    "n": '13',
    "o": '14',
    "p": '15',
    "q": '16',
    "r": '17',
    "s": '18',
    "t": '19',
    "u": '20',
    "v": '21',
    "w": '22',
    "x": '23',
    "y": '24',
    "z": '25',
    " ": '26'
}

numToLet = {
    "00": "a",
    "01": "b",
    "02": "c",
    "03": "d",
    "04": "e",
    "05": "f",
    "06": "g",
    "07": "h",
    "08": "i",
    "09": "j",
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
    "25": "z",
    "26":" "
}

import secrets
import sympy 

print("-------------------------------------------------------------------")


systemRandomGenerator = secrets.SystemRandom()
P = sympy.randprime(1000000000000000000000, 10000000000000000000000000000)
print('The Prime Number Is: ', P)
M = "Hello World" 
print('The Original Message Is:', M )

def intToText(intVal):
    intVal = str(intVal)
    if not(len(str(intVal)) %2 == 0):
        intVal = '0' + intVal
    plainMessage= ''
    for i in range(0,len(intVal),2):
        tmp = str(intVal[i]+str(intVal[i+1]))
        plainMessage += numToLet[tmp]
    return plainMessage 
       
def getKeys(P):
    g = 7                               
    privateKey = systemRandomGenerator.randint(2, 13)
    #print(privateKey)
    publicKey = (g ** privateKey) % P  
    return {publicKey: privateKey}    

## Key Generation:
aliceKeys = getKeys(P)
print('Alices Keys - ',aliceKeys)

## Encryption:
bobKeys = getKeys(P)
print('Bobs Keys - ',bobKeys)
cKeys1 = list(aliceKeys.keys())[0] # alice public key
cKeys2 = list(bobKeys.values())[0] # bobs private key

# converting the string message from letters to numbers:
cipherMessage = ''
for c in M.lower(): 
        cipherMessage += str(letToNum[c])
print('Cipher Message is: ', cipherMessage)

cipher = int(cipherMessage) * (int(cKeys1) ** int(cKeys2)) % P #cipher = int(M) * (int(cKeys1) ** int(cKeys2) % P)
bobPublicKey = list(bobKeys.keys())[0]
print('(c1,c2): ',bobPublicKey, cipher) # this is that Bob will send to Alice

## Decryption:
alicePrivateKey = list(aliceKeys.values())[0]
# M = (cipherMessage * (sympy.mod_inverse((bobPublicKey ** alicePrivateKey),P)) % P)
commonKey = bobPublicKey ** alicePrivateKey
inverseValue = sympy.mod_inverse(commonKey,P) 
M = (cipher * (inverseValue) % P)
print(M) # this number should be the same as the cipher message 

print('The Decrypted Message Is: ', intToText(M))
print("-------------------------------------------------------------------")