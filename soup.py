import requests
from bs4 import BeautifulSoup
page = requests.get("https://gameofthrones.fandom.com/wiki")

soup = BeautifulSoup(page.content, 'html.parser')

print(list(soup.children)[2].get_text())

episode = soup.find(id="seven-day-forecast")

print("GI")