# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
# It seems nytimes are hard to connect fom China, so I use foxnews instead
url = 'https://www.foxnews.com/'
r = requests.get(url)
html = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, features="lxml")

titles = soup.find_all('h2')
for title in titles:
    print(title.string)