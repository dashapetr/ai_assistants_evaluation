# fetch a picture from NASA API

import requests
import shutil

# NASA API endpoint for APOD
url = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": "YOUR_NASA_API_KEY"
}

response = requests.get(url, params=params)
data = response.json()

# Fetch the image
image_url = data['url']
response = requests.get(image_url, stream=True)
with open('nasa_image.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
