import requests
from bs4 import BeautifulSoup

url = "https://opentdb.com/api.php?amount=20&difficulty=medium&type=boolean"
response = requests.get(url)
data = response.json()
question_data = data["results"]

