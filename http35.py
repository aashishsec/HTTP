import requests

url = "http://ptl-f4c91a00-aae0ada9.libcurl.so/"

data="<key><value>&amp;please</value></key>"

response = requests.post(url=url + "pentesterlab",data=data,headers={'Content-Type': 'application/xml'})

print(response.text)
'''
curl -X POST -H "Content-Type: application/xml" -d '<key><value>&amp;please</value></key>' http://ptl-f4c91a00-aae0ada9.libcurl.so/
'''