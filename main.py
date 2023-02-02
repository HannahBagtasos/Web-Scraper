from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib #helps you write emails to yourself

#tell beautiful soup what website I want to parse

URL = 'https://www.amazon.co.uk/ASUS-Vivobook-X1500EA-i5-1135G7-Windows/dp/B09X6RWTWZ/ref=sr_1_4?crid=T43P8XS54R4B&keywords=laptop&qid=1675020671&sprefix=laptop%2Caps%2C83&sr=8-4'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL , headers=headers)

#where we start getting the data
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify("utf-16"), "html.parser") 

title = soup2.find(id='productTitle').get_text()

price = soup2.find("div", {"class":'a-offscreen'}).get_text()
# price tag is not working, find another element later

print(title)
print(price)

#list at least 5 products with their prices then compare specs side by side

