import requests
from datetime import datetime
import os

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"



# https://pixe.la/v1/users/akilesh/graphs/graph1.html
today = datetime(year=2021, month=12, day=28)
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "490"
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)







put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{pixel_config['date']}"

put_config = {
    "quantity": "100"
}

# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
