import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
# soup = BeautifulSoup(r.text,"lxml")
soup = BeautifulSoup(r.text, features='html.parser')

# print(soup.title)


# attributes print
# print(soup.div.ul)

tag = soup.div.p.string
print(tag)
