# Author: Julia Gordon 
# date: 3/2/2022
# Homework 6
# this code will tell you if a positive number is a perfect number
print('--------------------------------------')
i = int(input("Enter any positive number: "))
PerSum = 0
for x in range(1, i): # here we are listing out the divisors of i in a for loop 
    if(i % x == 0): # if i is divisible by our i then it is prime 
        PerSum = PerSum + x # so we add it to the sum 
if (PerSum == i): # when the sum is equal to our number we know its a perfect number 
    print(i, "Is a Perfect number!")
else: # if the sum does not equal to our i then n is not a perfect number
    print(i, "Is not a Perfect number!")
print('--------------------------------------')

# this code will list perfect numbers in a given range
def PrintPerNum(start, end):
    for i in range(start, end+1): #for the integer within the given range
        PerSum = 0
        for x in range(1, i): # here we are listing out the divisors of the integer in a for loop 
            if(i % x == 0): # if i is divisible by our x indice then it is prime 
                PerSum = PerSum + x # so we add it to the sum 
        if (PerSum == i): # when the sum is equal to our integer we know its a perfect number 
            print(i)
print('In the range',(1,2000), 'the perfect numbers are: ')
PrintPerNum(1,2000)
print('--------------------------------------')

# This code will tell you the 8th perfect number only: 

def PrintPerNum8(start, end):
    for i in range(start, end+1): #for the integer within the given range
        PerSum = 0
        for x in range(1, i): # here we are listing out the divisors of the integer in a for loop 
            if(i % x == 0): # if i is divisible by our x indice then it is prime 
                PerSum = PerSum + x # so we add it to the sum 
        if (PerSum == i): # when the sum is equal to our integer we know its a perfect number 
            print(i)
print('the 8th perfect number is: ',)
PrintPerNum8(1,300000000000000000) # here I thought i could isolate the range of te 8th perfect number 
print('--------------------------------------')

print('--------------------------------------')
# Create an implementation of the Affine cipher with Python. 
# The Affine cipher is a simple substitution cipher.  Cipher Each character is mapped to 
# its numeric equivalent, encrypted with a mathematical function and then convert to the 
# letter relating to its new numeric value.
# 
import re
alphaMatches = {
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

numMatches = {
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

