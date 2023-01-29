from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib #helps you write emails to yourself

#tell beautiful soup what website I want to parse

URL = 'https://www.amazon.co.uk/ASUS-Vivobook-X1500EA-i5-1135G7-Windows/dp/B09X6RWTWZ/ref=sr_1_4?crid=T43P8XS54R4B&keywords=laptop&qid=1675020671&sprefix=laptop%2Caps%2C83&sr=8-4'
