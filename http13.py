import requests

url = "https://ptl-b06c34b0-4d072115.libcurl.so/"

response = requests.get(
    url=url + "pentesterlab?key=please%26"
)

print(response.text)