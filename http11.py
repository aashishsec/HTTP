import requests

url = "https://ptl-64ae7ebb-29f242c5.libcurl.so/"

response = requests.post(
    url=url + "pentesterlab?key=please",
    data={"key": "please"} 
)

print(response.text)
