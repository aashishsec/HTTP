import requests

url = "http://ptl-09140e62-a6ded44e.libcurl.so/"

response = requests.get(
    url=url + "pentesterlab?key=please%23"
)

print(response.text)