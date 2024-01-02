import requests

url = "http://ptl-d49724e3-f8742796.libcurl.so/"

response = requests.get(
    url=url + "pentesterlab",headers={"X-Forwarded-For":"1.2.3.4"}
)

print(response.text)
