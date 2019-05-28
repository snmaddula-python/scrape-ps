import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.pluralsight.com/authors/orin-thomas' # Example URL

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
author = soup.find('div', {'class': 'author__name'}).h1.text
for link in soup.find_all('a', href=True):
    if 'courses/' in link['href']:
        title = link.find_all('div', {'class': 'title__course'})[0].text
        info = link.find_all('div', {'class': 'title__info'})[0]
        level = info.findNext('div')
        duration = level.findNext('div')
        releaseday = duration.findNext('div')
        print(author + ',' + title + ',' + level.text + ',' + duration.text + ',' + link['href'].replace('/courses/', '') + ',' + releaseday.text)
