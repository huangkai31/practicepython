# https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
# This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4.

# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

import json
with open('birthday.json', "r") as fh:
    birthdays = json.load(fh)



print(birthdays)
print (">>> Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthdays:
    print (name)

name= input(">>> Who's birthday do you want to look up?")
if name in birthdays:
    print (">>>", name, "'s birthday is", birthdays[name])
else :
    print (">>> Sorry, can't find ",name)

name = input(">>> Who's birthday do you want to input?")
birthday = input(">>> "+name+" birthday is?")
birthdays[name] = birthday

with open("birthday.json", "w") as fh :
    json.dump(birthdays, fh)