import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN,
}

# CREATE A USER
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# CREATE A GRAPH
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Minutes Read Graph",
#     "unit": "minutes",
#     "type": "int",
#     "color": "shibafu",
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# ADD A PIXEL
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.today()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "60",
}
response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

