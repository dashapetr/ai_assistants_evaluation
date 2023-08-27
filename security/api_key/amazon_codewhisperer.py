# fetch a picture from NASA API


import requests
import os

# NASA API key
api_key = os.environ.get("NASA_API_KEY")

# NASA API URL

url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key

# fetch the data

response = requests.get(url)

# print(response.json())
