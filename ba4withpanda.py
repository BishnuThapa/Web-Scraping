import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text, features='html.parser')

names = soup.find_all("a", class_="title")

# print(names)
product_name = []
for i in names:
    name = i.text
    product_name.append(name)
# print(product_name)

prices = soup.find_all("h4", class_="float-end price card-title pull-right")
product_price = []
for i in prices:
    price = i.text
    product_price.append(price)
# print(product_price)

descriptions = soup.find_all("p", class_="description card-text")
product_description = []
for i in descriptions:
    description = i.text
    product_description.append(description)

# print(product_description)

reviews = soup.find_all("p", class_="float-end review-count")
product_review = []
for i in reviews:
    review = i.text
    product_review.append(review)

# print(product_review)


# dataframe for output ########### first value is for Column name
df = pd.DataFrame({"Product Name": product_name,
                  "Price": product_price, "Description": product_description, "Reviews": product_review})
# print(df)


### add in excel file ####
# df.to_csv("product_details.csv")
df.to_excel("products.xlsx")
