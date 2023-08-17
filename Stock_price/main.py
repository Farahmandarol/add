import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "IQ1BH6M14NOEKRO7."
url = "https://www.alphavantage.co/query?"
NEW_API_KEY = "f3a9d21e503f407185f28deac766f74a"
NEW_API_END_POINT = "https://newsapi.org/v2/everything?q=TSLA\&apiKey=f3a9d21e503f407185f28deac766f74a"

my_email = "haniarol94@gmail.com"
password = "mnqtlysyvhwnqiwv"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "datatype": "json",
    "apikey": API_KEY
}

response = requests.get(url=url, params=parameters)
daily_stock_data = response.json()["Time Series (Daily)"]
daily_stock_price = [value for (key, value) in daily_stock_data.items()]

percentage = (float(daily_stock_price[0]["2. high"]) / float(daily_stock_price[1]["2. high"]))

new_response = requests.get(url=NEW_API_END_POINT)
news_data = new_response.json()["articles"]
news = ""
for i in range(2):
    news_title = news_data[i]["title"]
    news_description = news_data[i]["description"]
    news_link = news_data[i]["url"]
    news += f"{i + 1}.\nTitle:{news_title}\nDescription:{news_description}\nNews_link:{news_link}\n"

if percentage:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="farahmandarol@gmail.com",
                            msg=f"Subject:TSLA New Time to deal \n\n{news}")
        print("Email Alert Sent!")
