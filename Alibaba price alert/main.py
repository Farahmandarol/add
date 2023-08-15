import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "haniarol94@gmail.com"
password = "mnqtlysyvhwnqiwv"

URL = "https://www.alibaba.com/product-detail/Wholesale-ready-stock-China-version-CPO_1600839190084.html?spm=a2700.galleryofferlist.normal_offer.d_image.3ce4454cTHfoHO"
response = requests.get(url=URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")
price = soup.find(name="div", class_="price").getText()[1:]
net_price = price.replace(",", "")
actual_price = int(net_price[0:-3])

if True:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="farahmandarol@gmail.com",
                            msg="subject:Good Price\n\nApple Mack book is at a good price and less than $999 you can get it now")
