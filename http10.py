import requests

url="http://ptl-9f2d269d-88d37ac3.libcurl.so/"

# headers={}

data={"key":"please","key":"please"}

# get_response=requests.get(url=url+"/pentesterlab?key=please&key=please")

# print(get_response.text)

post_response=requests.post(url=url+"pentesterlab",data="key=please&key=please")

print(post_response.text)