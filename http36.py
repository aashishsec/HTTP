import requests

url = "http://ptl-0295d1f1-52ba5ae3.libcurl.so/"

data='<key value="please"></key>'

response = requests.post(url=url + "pentesterlab",data=data,headers={'Content-Type': 'application/xml'})

print(response.text)

'''
curl -X POST -H "Content-Type: application/xml" -d '<key value="please"></key>' http://ptl-6875cb8a-41987af3.libcurl.so/
'''