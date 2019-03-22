# https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
# This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.

# You can start your Python journey anywhere, but to finish this exercise you will have to have finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).

# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.

# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

#     Only let the user guess 6 times, and tell the user how many guesses they have left.
#     Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.

# Optional additions:

#     When the player wins or loses, let them start a new game.
#     Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!

# Your solution will be a lot cleaner if you make use of functions to help you!

print(">>> Welcome to Hangman!")

import random
def randomword():
    with open('sowpods.txt', 'r') as fh:
        lines = fh.readlines()
        return random.choice(lines).strip()

word = randomword()
print ("my word is ", word)
def hangman(word, guess):
    isWinning = True
    for w in list(word):
        if w in guess :
            print (w,end=" ")
        else:
            print ("_ ", end="")
            isWinning = False
    print ()
    return isWinning

guess = []

import string
while True:
    winning = hangman(word, guess)
    if winning :
        print ("You win! ")
        break
    
    if len(guess) < 6 :
        print ("You have ", 6 - len(guess), "guesses left.")
    else :
        print ("Game over!")
        if input(">>> Do you want to play again? (y/n)") == "y" :
            word = randomword()
            print ("My word is ", word)
            guess = []

        else: 
            break
    
    letter = input (">>> Guess your letter: ")
    if letter in string.ascii_letters:
        letter= letter.upper()
        if letter in guess :
            print ("You have tryed ",letter,"already.")
        else:
            guess.append(letter)
