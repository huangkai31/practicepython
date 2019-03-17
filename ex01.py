# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("Pls type your name: ")
age = int(input("Pls type your age: "))

import datetime
year = datetime.datetime.now().year
print("Hi", name, ", you will be 100 years old at year :", year - age + 100 )
# Extras:

#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
count = int(input("Pls input a number so I can print may messages: "))
for i in range(0, count):
    print("Hi", name, ", you will be 100 years old at year :", year - age + 100, end='' )
#     Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
for i in range(0, count):
    print("Hi", name, ", you will be 100 years old at year :", year - age + 100 )
