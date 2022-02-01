# Author: Julia Gordon 
# date 2/1/22
# Exercise 2:  
# Write a program that prints the sum of the prime numbers greater than 2 and less than 1000.
print("the sum of the prime numbers between", 3, "and", 1000, "are:")
sum = 0 
for num in range(1000):
   # A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
   if num > 2 and num%2==1 :
        isnotprime=False
        for i in range(num): # primality test, to check of num is prime or not
            if i>1 and (num % i) == 0: #making sure the number is only divisible by 1.
               isnotprime=True
               break
        if not(isnotprime):
            sum+=num
print(sum)
