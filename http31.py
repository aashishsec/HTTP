import requests

url = "http://ptl-c9ce5d3d-eb4dab10.libcurl.so/"

response = requests.post(url=url + "pentesterlab",data="<key><value>please</value></key>",headers={'Content-Type': 'application/xml'})

print(response.text)
'''
curl -X POST -H "Content-Type: application/xml" -d '<key><value>please</value></key>' http://ptl-c9ce5d3d-eb4dab10.libcurl.so/ 
'''