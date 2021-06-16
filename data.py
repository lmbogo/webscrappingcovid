# webscrappingcovid

Created on Sat Apr 18 20:42:53 2020

@author: linnetmbogo
"""


#py -3 -m pip install BeautifulSoup4

import json
import requests, ast
from urllib.request import Request, urlopen
from lxml import html
import pandas as pd

website_url = requests.get('https://en.wikipedia.org/wiki/Template:2019%E2%80%9320_coronavirus_pandemic_data').text

from bs4 import BeautifulSoup
# parse the HTML from our URL into the BeautifulSoup parse tree format
soup = BeautifulSoup(website_url,'lxml')
print(soup.prettify())

My_table = soup.find('table',{'id':'thetable'})
My_table

tbody = My_table.find('tbody')
tbody


#to find results of one country, specify cell as below'
#rows = tbody.findAll('tr')
#print(rows[225].text)

#to find content of specific cell'
#cell = rows[2].findAll('th')
#print(cell[1].text)

#to find values in cells'
#cell = rows[2].findAll('td')
#print(cell[0].text)


#create a loop to find results for multiple countries, as below'
rows = tbody.findAll('tr')
for i in range(2,5):
    country = rows[i].findAll('th')
    #print(country[1].text)
    cell = rows[i].findAll('td')
   # print(cell[0].text)
    #print(cell[1].text)
    #print(cell[2].text)
    print('Countries and territories = '+(country[1].text)+'Cases = '+(cell[0].text)+'Deaths = '+(cell[1].text)+'Recov. = '+(cell[2].text))    

#this loop is a Dataframe that will create a table for all values in the range
#specified, the strip command truncates the \n that existed to show a new line

Countries = []
Cases = []
Deaths = []
Recoveries = []


for i in range(2,226):
    row=rows[i]
    country_cell = row.findAll('th')
    country=country_cell[1]
    Countries.append(country.text.strip())
    
    cells = row.findAll('td')
    case = cells[0].text.strip()
    Cases.append(case)
    
    death=cells[1].text.strip()
    Deaths.append(death)
    
    recov=cells[2].text.strip()
    Recoveries.append(recov)
            
df1 = pd.DataFrame(Countries, index= Countries, columns = ['Countries'])
df1['Cases'] = Cases
df1['Deaths'] = Deaths
df1['Recov.'] = Recoveries

#this command prints the dataframe table
df1.head(10)
#end of table dataframe

#export dataframe to excel
df1.to_excel (r'C:\Users\LMbogo\Desktop\PROJECTS\Covid-19\export_dataframe.xlsx', index = False, header=True)
#create a loop to find results for cells, as below
