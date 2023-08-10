# fetch a picture from NASA API

import requests
import json
import os


def fetch_picture():
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    response = requests.get(url)
    data = response.json()
    print(data["url"])

    # download the picture
    os.system(f"wget {data['url']}")
    os.system("mv apod.jpg ~/Pictures/")
    os.system("rm apod.jpg")


fetch_picture()
