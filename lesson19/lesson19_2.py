import requests

image_path = "C:\\Users\\o.bogachenko\\Downloads\\Frame8564.jpg"
upload_url = 'http://127.0.0.1:8080/upload'

with open(image_path, 'rb') as file:
    files = {'image': file}
    response = requests.post(upload_url, files=files)

    if response.status_code == 201:
        created_data = response.json()
        image_url = created_data['image_url']
        print('Upload image:', image_url)
    else:
        print('Download error. Status-cod:', response.status_code)
        exit()


get_url = 'http://127.0.0.1:8080/image/Frame8564.jpg'
headers = {'Content-Type': 'text'}
response = requests.get(get_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Request error:', response.status_code)


delete_url = 'http://127.0.0.1:8080/delete/Frame8564.jpg'
response = requests.delete(delete_url)

if response.status_code == 200:
    print('Data successfully delete')
else:
    print('Delete error. Status-cod:', response.status_code)