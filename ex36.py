# https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html
# This exercise is Part 4 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 3.

# In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.

# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday JSON file. Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.

# If you are using a purely web-based interface for coding, this exercise won’t work for you, since it requires installing the bokeh Python package. Now might be a good time to install Python on your own computer.


import json
import datetime

with open("scientist_birthdays.json", "r") as fh:
    birthdays = json.load(fh)
    monthes =[]
    for name in birthdays :
        day = datetime.datetime.strptime( birthdays[name], "%m/%d/%Y")
        monthes.append( int(day.strftime("%m")))
    
    from collections import Counter
    monthes= Counter(monthes)
    monthes= dict(monthes)

print(monthes)
print(list(monthes.keys()))
from bokeh.plotting import figure, show, output_file
output_file("scientist_birthdays.html")
p = figure()
p.vbar(x= list(monthes.keys()), top=list(monthes.values()), width=0.5)
show(p)
