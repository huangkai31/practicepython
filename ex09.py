# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

n = random.randint(1,10)
print("My number is: ", n)
guess_count =0 
while True:
    i = input("Pls guess the number or type exit:")
    if i == 'exit':
        break
    i=int(i)
    guess_count += 1
    if i == n :
        print ("Correct ! You tried", guess_count, "times.")
        n = random.randint(1,10)
        print("My number is: ", n)
    elif i < n :
        print ("Your guess is too low")
    elif i > n :
        print ("Your guess is too high")