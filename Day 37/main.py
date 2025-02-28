from http.client import responses

import requests
from datetime import datetime

USERNAME = "maksymbot"
TOKEN = "ssdgsd4hsd9hsdh9ds7hsdh7"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Coding Graph",
    "unit" : "pages",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}
# --------------------------------------POST--------------------------------------

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2025, month=2, day=27)

date_strftime = today.strftime("%Y%m%d")

pixel_data = {
    "date" : date_strftime,
    "quantity" : "10",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#
# print(response.text)

pixed_edit_data = {
    "quantity" : "5",
    "optionalData" : "10",
}

pixel_editing_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_strftime}"

# ------------------------------------------PUT-------------------------------------------

# response = requests.put(url=pixel_editing_endpoint, json=pixed_edit_data, headers=headers)

# -----------------------------------------DELETE-----------------------------------------

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_strftime}"

response = requests.delete(url=delete_endpoint, headers=headers)

print(response.text)