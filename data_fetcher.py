import requests

def fetch_data(animal_name):
    """ Asks for input and seachring the input using API"""
    api_key = "UG/NNIDCLpv0fariq0cTsA==O1RjeABZAL0iwScZ"
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