import requests

url = "http://ptl-8767dc0a-8296fe51.libcurl.so/"

data='{"key":"please"}'

response = requests.post(url=url + "pentesterlab",data=data,headers={'Content-Type': 'application/json'})

print(response.text)
