# https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

# Extras:

#     Ask the user to specify the name of the output file that will be saved.
import requests
r = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
html = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, features="lxml")

# using css select
div = soup.select('div[class="content paywall drop-cap"]')
print("Article content length:", len(div[0].get_text()))

import sys
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "content.txt"

print ("Write article content to:", filename)
with open(filename, 'a') as fh:
    fh.write(div[0].get_text())