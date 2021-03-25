import requests
from bs4 import BeautifulSoup
import lxml

g = requests.get('https://www.google.com/').text

soup = BeautifulSoup(g, 'lxml')
link = soup.a.get('href')
print(link)