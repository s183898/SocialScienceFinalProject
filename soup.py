import requests
from bs4 import BeautifulSoup
page = requests.get("https://gameofthrones.fandom.com/wiki")

soup = BeautifulSoup(page.content, 'html.parser')

print(list(soup.children))