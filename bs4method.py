import requests
from bs4 import BeautifulSoup


url = "https://www.wscubetech.com"
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text, "lxml")
print(soup)
