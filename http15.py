import requests

url = "http://ptl-6c744b20-2d7f679d.libcurl.so/"

response = requests.get(
    url=url + "pentesterlab?key=pretty please"
)

print(response.text)