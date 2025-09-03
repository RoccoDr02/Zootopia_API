import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name, api_key=API_KEY):
    """ Asks for input and seachring the input using API"""
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {"X-Api-Key": api_key}
    params = {"name": animal_name}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
      print("Error: ", response.status_code, response.text)
      return []

print(API_KEY)