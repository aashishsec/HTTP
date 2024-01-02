import requests

url="http://ptl-5ccc870954a1-289ee21bcc42.libcurl.me/"

# headers={}

data={"key":"please"}

get_response=requests.get(url=url+"pentesterlab",data=data)

print(get_response.text)



# post_response=requests.post(url=url+"pentesterlab",data=data)

# print(post_response.text)