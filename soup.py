import requests
from bs4 import BeautifulSoup
import json

url = 'https://gameofthrones.fandom.com/wiki/Home'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)


print(soup.find(["h3"]).next_siblings)

target = soup.find('h2',text='Topic 2')
for sib in target.find_next_siblings():
    if sib.name=="h2":
        break
    else:
        print(sib.text)


