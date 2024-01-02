import requests

url = "http://ptl-9bc3a492-27a15474.libcurl.so/"

response = requests.get(
    url=url + "pentesterlab",headers={"X-Forwarded-Host":"pentesterlab.com"}
)

print(response.text)
