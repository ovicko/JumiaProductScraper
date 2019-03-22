# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
import requests
import csv

seller = 'la-colors'
pagination = '3'
siteUrl = 'https://www.jumia.co.ke/'
headers = {'User-Agent': 'Mozilla/5.0'}
page= '?page='+pagination

baseUrl = siteUrl+seller+page
#fullUrl = 
#page = urllib2.urlopen(baseUrl)
# Here, we're just importing both Beautiful Soup and the Requests library
# this is the url that we've already determined is safe and legal to scrape from.
page_response = requests.get(baseUrl, timeout=5)
# here, we fetch the content from the url, using the requests library
soup = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.
section = soup.find('section', attrs={'class':'products'})

dataToCsv = []
for productContainer in section:
    try:
       productName = productContainer.find("span", attrs={'class':'name'}).text
       price = productContainer.find("span", attrs={'class':'price'}).text
       reviews = productContainer.find("div", attrs={'class':'total-ratings'}).text 
       brand = productContainer.find("span", attrs={'class':'brand'}).text 
    except Exception as e:
      productName = "N"
      price = "N"
      reviews = "N"
      brand = "N"
      
    if productName != 'N':
#        print(hotelDesc)
#        print(productName)
#        print(price) #remove ksh
        
#        print(brand) #remove ksh
#        print(reviews) #remove brackets
        dataToCsv.append([productName,brand.replace('\xa0', ''),price[4:],reviews.strip("()")])
        #empty line
#        print("==============================")
#print(dataToCsv)

with open(seller+'_'+pagination+'.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(dataToCsv)

csvFile.close()
