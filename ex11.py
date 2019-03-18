# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1 ):
        if num % i ==0 :
            return False

    return True

num = int(input("Pls input a number:"))
if isPrime(num):
    print("The number is a prime number")
else:
    print("The number is not a prime number")