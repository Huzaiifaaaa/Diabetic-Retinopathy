import requests

url = "http://localhost:5000/api"

params = {
    "module": "DiabeticRetinopathy",
    "token": "naseerbajwa",
    "imagepath": "/path/to/my/image.jpg"
}

files = {
    "image": open(r"path/to/image", "rb")
}

response = requests.post(url,params=params,files=files)

print(response.status_code)   # prints the HTTP status code
print(response.text)          # prints the response body as a string
