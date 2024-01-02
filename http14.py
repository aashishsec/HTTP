import requests

url = "http://ptl-8ccf2959-8c532d57.libcurl.so/"

response = requests.get(
    url=url + "pentesterlab??key=please"
)

print(response.text)