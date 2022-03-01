# Author: Julia Gordon 
# Date: 2/8/2022
# Homework 3
## Exercise 1: Add exceptions handeling to your homework 2 solutions, making
# sure to include the try block. 
    # Exercise 1(hw2): use find to implement a function satisfying the specification 
    # def find_last(s,sub):
        # s and sub are non-empty strings.
        # returns the index of the last occurence of sub in s. 
        # returns None if sub does not occure in s. 
def find_last(s, sub):
    # default condition
    if(len(sub) > len(s) or ((s.find(sub)) == -1)):
        return None
    currentIndex = s.find(sub)
    while True:
        try: 
            if (len(sub) < len(s) or ((s.find(sub)) == -1)):
                break
        except:
            print('there was an error found')
        else:  # while(True):
            index = s.find(sub, currentIndex + len(sub))
            if(index == -1):
                break
            else:
                currentIndex = index
        return currentIndex
print(find_last("testnowtest", "test"))
 

    ## Exercise 2(hw2): given a number n, determing what the nth prime number is.
import math
def isPrime(i):
    isPrime = True
    for j in range(math.floor(math.sqrt(i)) + 1):
        if(j > 1 and i % j == 0):
            isPrime = False
            break
    return isPrime 
#n = int(input("Please enter a positive integer "))
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
while True:
    try: 
        n = int(input("Please enter a positive integer "))
        if n < 0:
            raise Exception('There was an error with your input - try again')
    except: 
        print('Input should be an integer bigger than zero ')
    else: 
        print('Thank you!')
        break
print(f"The {n}th prime is {findNthPrime()}") 

    ## Exercise 3(hw2): Find the difference between the square of the sum and the sum
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
        n = int(input('Please enter a integer '))
        if n < 1:
            raise Exception('Error - Please try again')
    except:
        print('Please enter a positive integer ')
    else:
        print('thank you! ')
        break
print(Square_Diff(n))

## Exercise 2: implement a function satisfying the following specification.
# Hint: it will be convenient to use lambda and map functions in the body 
# of the implemation. 

# just using lambda: 
L1 =[3,2]
L2= [2,2]
Squared = [] #empty list to store the rised integer set.

def ElementL1Sqr(n): # the lambda function to raise elements in L1 by elements in L2.
    return lambda a: a ** n 

Element1L2 = ElementL1Sqr(L2[0]) # first element in L1 that is raised to the first element in L2. 
Element2L2 = ElementL1Sqr(L2[1]) # second element in L1 raise to the power of the second element in L2.

#print(Element1L2(L1[0])) #this is just so I could see if the lambda was working.
#print(Element2L2(L1[1]))

Squared.append(int(Element1L2(L1[0]))) # here I am appending what lambda found to the empty list. 
Squared.append(int(Element2L2(L1[1])))
print(sum(Squared)) # printing the sum of what lambda found. 

# just using map: 
L1 = [3,2]
L2 = [2,2]

SumPow = list(map(pow,L1,L2)) # using map the apply the power function to raise every element in list 1 to that of list 2. 
print(sum(SumPow)) # printing the sum of the map 

#using both? :
L1 = [2,2]
L2 = [2,3]

SumPow = list(map(lambda a,b: a ** b, L1, L2)) # using map to apply the lambda to each element 
print(sum(SumPow)) # printing the sum 

#solution: 
def MyFunction(L1,L2):
    sum = 0 # the sum is stating at zero
    for i in map(lambda x,y: x ** y, L1,L2):
        sum += i #this is where it is taking the sum 
    return sum
print(MyFunction([1,2],[2,3])) 


## Exercise 3: read chapter 1 and 2 in the textbook