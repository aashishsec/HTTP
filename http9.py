import requests

url="https://ptl-0603ceb6edab-ca4a5413b1c4.libcurl.me/"

# headers={}

# data={"key":"please","key":"please"}
# data={"key":"please","key":"please"}

get_response=requests.get(url=url+"/pentesterlab?key=please&key=please")

print(get_response.text)



# post_response=requests.post(url=url+"pentesterlab",data=data)

# print(post_response.text)