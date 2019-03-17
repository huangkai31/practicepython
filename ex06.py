# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

string = input("Pls input a string:")
reverse = string[::-1]
if string == reverse :
    print ("Your input is a palindrome")
else:
    print ("Your input is not a palindrome")