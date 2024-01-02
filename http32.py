import requests

url = "http://ptl-b5052787-da4973d2.libcurl.so/"

response = requests.post(url=url + "pentesterlab",data="<key><value>please</value></key>",headers={'Content-Type': 'application/xml'})

print(response.text)
'''
curl -X POST -H "Content-Type: application/xml" -d '<key><value>please</value></key>' http://ptl-b5052787-da4973d2.libcurl.so/ 
'''