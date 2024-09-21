# Grabbing a class 
import requests
from bs4 import BeautifulSoup
import lxml

r = requests.get(url='https://en.wikipedia.org/wiki/Grace_Hopper')

soup = BeautifulSoup(r.text,'lxml')

# print(soup.prettify())

print(soup.select('title')[0].getText())
div = soup.find_all(class_="vector-header mw-header")
# for divs in div :
#      print(divs.text)
# print(soup.select('.toctext'))

# print(soup.select('class_'))