# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

primenumbers =[]
with open('primenumbers.txt', 'r') as fh:
    l = fh.readline()
    while l:
        primenumbers.append(int(l.strip()))
        l= fh.readline()

happynumbers =[]
with open('happynumbers.txt', 'r') as fh:
    l = fh.readline()
    while l:
        happynumbers.append(int(l.strip()))
        l= fh.readline()

commonnumbers = [n for n in primenumbers if n in happynumbers]
print("Common numbers:", commonnumbers)