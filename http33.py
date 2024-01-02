import requests

url = "https://ptl-50a6d84a-9f8a1f65.libcurl.so/"

data="<key><value>>please</value></key>"

response = requests.post(url=url + "pentesterlab",data=data,headers={'Content-Type': 'application/xml'})

print(response.text)
'''
curl -X POST -H "Content-Type: application/xml" -d '<key><value>&gt;please</value></key>' https://ptl-50a6d84a-9f8a1f65.libcurl.so/
'''