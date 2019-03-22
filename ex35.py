# https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html
# This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 4.

# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.

# Your program should output something like:

# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }

import json
import datetime

with open("birthday.json", "r") as fh:
    birthdays = json.load(fh)
    monthes =[]
    for name in birthdays :
        day = datetime.datetime.strptime( birthdays[name], "%m/%d/%Y")
        monthes.append( day.strftime("%B"))
    
    from collections import Counter
    monthes= Counter(monthes)
    monthes= dict(monthes)
    print(monthes)
