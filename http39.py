import requests

url = "http://ptl-16ec8d7a-4f276583.libcurl.so/"

data='{"key": "please\u0022"}'

response = requests.post(url=url + "pentesterlab",data=data,headers={'Content-Type': 'application/json'})

print(response.text)

'''
curl -X POST -H "Content-Type: application/json" --data '{"key":"please\u0022"}' https://ptl-16ec8d7a-4f276583.libcurl.so/pentesterlab
'''