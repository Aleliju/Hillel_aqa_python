import requests
import json

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params)
data = response.json()

first_photo = data['photos'][0]['img_src']
second_photo = data['photos'][1]['img_src']

first_photo_img = requests.get(first_photo)
with open('mars_photo1.jpg', 'wb') as file:
    file.write(first_photo_img.content)

second_photo_img = requests.get(second_photo)
with open('mars_photo2.jpg', 'wb') as file:
    file.write(second_photo_img.content)
