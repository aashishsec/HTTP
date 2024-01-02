import requests

url = "https://ptl-7ec26bd4-9676b60c.libcurl.so/"

response = requests.get(
    url=url + "pentesterlab?key==please"
)

print(response.text)
