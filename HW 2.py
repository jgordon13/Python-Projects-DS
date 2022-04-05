# Author: Julia Gordon
# Date: 2/8/2022
# HW 2 
## Exercise 1: use find to implement a function satisfying the specification 
# def find_last(s,sub):
    # s and sub are non-empty strings.
    # returns the index of the last occurence of sub in s. 
    # returns None if sub does not occure in s. 
def find_last(s, sub):
    # default condition
    if(len(sub) > len(s) or ((s.find(sub)) == -1)):
        return None
    currentIndex = s.find(sub)
    while(True):
        index = s.find(sub, currentIndex + len(sub))
        if(index == -1):
            break
        else:
            currentIndex = index
    return currentIndex
print(find_last("testnowtest", "test"))

## Exercise 2: given a number n, determing what the nth prime number is.
import math
def isPrime(i):
    isPrime = True
    for j in range(math.floor(math.sqrt(i)) + 1):
        if(j > 1 and i % j == 0):
            isPrime = False
            break
    return isPrime 
n = int(input("Please enter a positive integer "))
def findNthPrime():
    currentPrime = 2
    if(n == 1):
        return currentPrime
    index = 1
    i = 3
    while(index < n):
        if(i % 2 != 0 and isPrime(i)):
           currentPrime = i
           index += 1
        i += 1
    return currentPrime    
print(f"The {n}th prime is {findNthPrime()}")


## Exercise 3: Find the difference between the square of the sum and the sum
# of the squares of the first N natural numbers. 
def Square_Diff(n):
    # sum of the squares of the first n natural numbers is
    SumOfSquares = (n * (n + 1) * (2 * n + 1)) / 6
    # sum of n naturals numbers squared
    SquareOfSums = ((n * (n + 1)) / 2)**2
    # Differences between the square of sums and the sum of squares
    DifferenceOfTwo = abs(SquareOfSums - SumOfSquares) #dont need the abs
    return int(DifferenceOfTwo)
while (True): 
    try:  
        n = int(input('Please enter a positive integer '))
        if n < 1:
            raise Exception('n must be a positive integer')
    except:
        print('The value you have entered is not a positive integer')
    else:
        print('thank you')
        break
print(Square_Diff(n))