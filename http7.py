import requests

url="https://ptl-b3adfec1-5bc38eba.libcurl.so/"

# headers={}

# get_response=requests.get(url=url+"/pentester",headers=headers)

# print(get_response.text)

data={}

post_response=requests.post(url=url+"pentesterlab",data=data)

print(post_response.text)