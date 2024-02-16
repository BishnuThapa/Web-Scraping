import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text, features='html.parser')
prices = soup.find_all("h4", class_="float-end price card-title pull-right")
# print(prices)
# print(len(prices))

# to pring all prices
for i in prices:
    print(i.string)
