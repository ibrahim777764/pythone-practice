from urllib import response
import requests
from bs4 import BeautifulSoup
import datetime

url = "https://ibrahim777764.github.io/project-capstone/" 
response = requests.get(url)
html =  response.content
soup = BeautifulSoup(html,'html.parser')
heading = soup.find_all('car',class_="old-cars stacks")


print(heading)