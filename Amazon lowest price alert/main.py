import requests
from bs4 import BeautifulSoup
import smtplib

#
my_email = "haniarol94@gmail.com"
password = "mnqtlysyvhwnqiwv"

# URL = "https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5KWB9H/ref=sr_1_5?crid=9JUNVNQDQPNB&keywords=macbook+pro+2021&qid=1691245256&sprefix=macbook+pro+2021+%2Caps%2C368&sr=8-5"
# response = requests.get(url=URL)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# print(soup.findAll(class_="a-span12"))

url = "https://www.amazon.in/Midkart-Plastic-Compatible-MacBook-Transparent/dp/B09PGH7WQ6/ref=sr_1_14?crid=7W62VMNW2KSS&keywords=macbook%2Bpro%2B2019%2B16%2Binch%2Blaptop%2Bin%2B%24%2Bprice&qid=1691246149&sprefix=macbook%2Bpro%2B2019%2B16%2Binch%2Blaptop%2Bin%2Bpric%2Caps%2C290&sr=8-14&th=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

price_tag = soup.find("span", class_="a-price-whole").getText()
net_price = float(price_tag.replace(",", "")[0:-1])
if net_price > 999:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="farahmandarol@gmail.com",
                            msg="subject:Good Price\n\nApple Mack book is at a good price and less than $999 you can get it now")
        print("eamil sent")


