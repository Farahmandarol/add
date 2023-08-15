import requests
import datetime

pixel_endpoint = "https://pixe.la/v1/users"
user_token = "lskfjsaljflasjfhsdfisjfdlkjsd"
user_name = "ljdslfkjasdlkfjs"
user_params = {
    "token": user_token,
    "username": "ljdslfkjasdlkfjs",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixel_endpoint, json=user_params)
# print(response.text)
# ----------------  graph definition -------------------#
graph_endpoint = f"{pixel_endpoint}/{user_name}/graphs"
graph_id = "upcomingworld"
graph_config = {
    "id": graph_id,
    "name": "arol",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
header = {
    "X-USER-TOKEN": user_token
}
# graph_response = requests.post(graph_endpoint, json=graph_config, headers=header)
# print(graph_response.text)
# ------------------- post a pixel ------------------#
date = datetime.datetime.today()
today = date.strftime("%Y%m%d")
post_endpoint = f"{pixel_endpoint}/{user_name}/graphs/{graph_id}"
post_config = {
    "date": today,
    "quantity": "90"
}
print(today)
# post_response = requests.post(url=post_endpoint, json=post_config, headers=header)
# print(post_response.text)
# -------------- update the existing pixel --------------------#
put_endpoint = f"{pixel_endpoint}/{user_name}/graphs/{graph_id}/{today}"

put_config = {
    "quantity": "7"
}
put_response = requests.put(put_endpoint, json=put_config, headers=header)
print(put_response.text)


# delete_responses = requests.delete(url=put_endpoint, headers=header)
# print(delete_responses.text)
