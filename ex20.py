# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.


# easist way
def search(numbers, n):
    return n in numbers

# compare with a loop
def search2(numbers, n):
    for i in numbers:
        if i == n:
            return True
    return False

# Extras:

#     Use binary search.
def binarySearch(numbers, n):
    length = len(numbers)
    if length == 1 and n != numbers[0]:
        return False
    middle = int(length / 2)
    
    if n == numbers[middle]:
        return True
    elif n < numbers[middle]: 
        return binarySearch(numbers[:middle], n)
    else :
        return binarySearch(numbers[middle:], n)

a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = int(input("Pls input a number to search:"))
print( search(a, n))
print( search2(a, n))
print( binarySearch(a, n))