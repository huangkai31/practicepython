# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

# Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
common = []
for i in a:
    if i in b and i not in common :
        common.append(i)

print(common)
# Extras:

#     Randomly generate two lists to test this
import random
a = []
b = []
for i in range(0, 100):
    a.append(random.randint(0, 1000))
    b.append(random.randint(0, 1000))
common = []
for i in a:
    if i in b and i not in common :
        common.append(i)
print ( common)
#     Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
### TBD