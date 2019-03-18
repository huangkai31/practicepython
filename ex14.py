# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = { n for n in a }
print (b)
# Extras:

#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
def remove_dup(alist):
    return { n for n in alist }

def remove_dup2(alist):
    b = []
    for n in alist:
        if n not in b:
            b.append(n)
    return b
print(remove_dup(a))
print(remove_dup2(a))
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.
