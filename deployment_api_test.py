import requests

url = "https://aeyecheck.pythonanywhere.com/api"

params = {
    "module": "DiabeticRetinopathy",
    "token": "naseerbajwa",
    "imagepath": r"C:\Users\huzai\Pictures\Saved Pictures\Isb.jpeg"
}

files = {
    "image": open(r"C:\Users\huzai\Pictures\Saved Pictures\Isb.jpeg", "rb")
}

response = requests.post(url,params=params,files=files)

print(response.status_code)   # prints the HTTP status code
print(response.text)          # prints the response body as a string
