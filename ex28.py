# https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html
# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

def max(a,b,c):
    if a >= b :
        if a >= c : 
            return a
        else :
            return c
    else :
        if b >= c :
            return b
        else :
            return c

print( max(1,2,3))
