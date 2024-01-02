import requests

url = "http://ptl-46401a1e-7bfcca18.libcurl.so/"

response = requests.get(
    url=url + "pentesterlab",headers={"X-HTTP-Method-Override":"HACK"}
)

print(response.text)
