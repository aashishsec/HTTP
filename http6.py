import requests

url="https://ptl-8693339b6e24-c158b6716227.libcurl.me/"

# headers={}

# get_response=requests.get(url=url+"/pentester",headers=headers)

# print(get_response.text)

data={"key":"please"}

post_response=requests.post(url=url+"pentesterlab",data=data)

print(post_response.text)