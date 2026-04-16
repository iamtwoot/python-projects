import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"Environment variable '{name}' is not set")
    return value


class DataManager:

    def __init__(self):
        self.sheety_url = get_env_variable("SHEETY_API")
        self.sheety_token = get_env_variable("SHEETY_TOKEN")

        self.headers = {"Authorization": f"Bearer {self.sheety_token}"}
        self.data = None

    def get_data(self):
        response = requests.get(url=self.sheety_url, headers=self.headers)
        self.data = response.json()
        print(self.data)
