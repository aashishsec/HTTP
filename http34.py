import requests

url = "http://ptl-67b4d380-9dd2c3eb.libcurl.so/"

data="<key><value>&lt;please&gt;</value></key>"

response = requests.post(url=url + "pentesterlab",data=data,headers={'Content-Type': 'application/xml'})

print(response.text)
'''
curl -X POST -H "Content-Type: application/xml" -d '<key><value>&lt;please&gt;</value></key>' http://ptl-67b4d380-9dd2c3eb.libcurl.so/
'''