import requests
from bs4 import BeautifulSoup
page = requests.get("https://gameofthrones.fandom.com/wiki")

soup = BeautifulSoup(page.content, 'html.parser')

print(list(soup.children)[2].get_text())


episode = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())