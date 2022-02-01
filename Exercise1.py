# Author: Julia Gordon 
# Date: 2/1/22
# Exercise 1:
# write a progeam that asks the user to input 10 integers, and then prints the largest odd number that was entered.
largestValue = int(input('Enter an integer '))
for i in range(9):
    currentValue = int(input('Enter an integer '))
    if (largestValue < currentValue and currentValue % 2 ==1):
        largeValue = currentValue
if (largestValue % 2): # this if statement is true if the number is odd 
    print('the largest odd number is ' + str(largestValue))
else:
    print('you did not enter an odd number')

