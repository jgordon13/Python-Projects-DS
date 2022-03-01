# Author: Julia Gordon 
# Date: 2/19/2022
# Homework 4 
# page 35 problem 2: Find the smallest five consecutive composite integers.
# 
#n = 6
# definition to find the factorial of given number (5)
#def factorial(n):
#    Sum = 1
#    for i in range(2, n + 1):
#        Sum += i
#    return Sum
# here we are defining the 5 consecutive numbers 
#def printNComposite(n):
#    fact = factorial(n + 1)
#    for i in range(3, n + 3): # for this i played around with the range untill i got the answer i needed 
#        print(fact + i, end = " ") # printing the consecutive factorials 
#printNComposite(n)

# solution: 
import math
def isPrime(i):
    isPrime = True
    for j in range(math.floor(math.sqrt(i)) + 1):
        if(j > 1 and i % j == 0):
            isPrime = False
            break
    return isPrime

def findConseCompo(n):
    i  = 4
    l1 = []
    while len(l1) < n:
        if(not(isPrime(i)) and (len(l1) == 0 or (i - 1 in l1))):
            l1.append(i)
        else: 
            l1.clear()
        i += 1
    print(l1)

findConseCompo(5)
findConseCompo(6)
findConseCompo(7)
findConseCompo(10)