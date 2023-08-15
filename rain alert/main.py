import requests

# API_KEY = "2a50c594ba6e7e14635d3e56c77eb556"
# CITY = "kabul"
# END_POINT = "https://api.openweathermap.org/data/2.5/onecall"
# weather_params = {
#     "lat": 34.555347,
#     "lon": 69.207489,
#     "appid": API_KEY
# }
#
# response = requests.get(END_POINT, params=weather_params)
# print(response.json())


from twilio.rest import Client

account_sid = 'ACce9d073ee07602ca5d89fa7352b8885f'
auth_token = '77d6775167fdb4e1efa8621c1cdd273b'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="to day is really hot dont forget to take an ️☂️",
    from_='+14705180502',
    to='+93780599071'
)

print(message.sid)
