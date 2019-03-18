# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

def myfunc(numbers):
    return [numbers[0], numbers[-1]]

a = [5, 10, 15, 20, 25]
print( myfunc(a))