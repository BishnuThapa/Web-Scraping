import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text, features='html.parser')

# find price
price = soup.find("h4", {"class": "float-end price card-title pull-right"})

# another method to use class
description = soup.find("p", {"class": "description card-text"})
print(price.string, description.string)
