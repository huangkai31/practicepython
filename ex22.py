# https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!
filename= "nameslist.txt"
names = {}
with open(filename, 'r') as fh:
    line = fh.readline().strip()
    while line:
        if line not in names:
            names[line] = 1
        else:
            names[line] += 1
        line = fh.readline().strip()

print(names)
# Extra:

#     Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.

filename = "Training_01.txt"
categories= {}
with open(filename, 'r') as fh:
    line = fh.readline().strip()
    while line:
        fields= line.split('/')
        category = fields[2]
        if category in categories :
            categories[category] +=1
        else:
            categories[category] = 1
        line = fh.readline().strip()

print(categories)