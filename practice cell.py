# Page. 86 - question 2: Find the eighth perfect number
# note: a perfect number is a positive integer that is equal to the sum 
# of its positive divisors, excluding the number itself.

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
