import requests
#
# response = requests.get("http://www.baidu.com/s",params="wd=接口测试")
# response.encoding = "utf-8"
# print(response.text)


url = "http://ihrm-test.itheima.net/api/sys/login"
jsonData= {"mobile":"13800000002","password":"123456"}
header = {"Content-Type":"application/json"}
response = requests.post(url,json =jsonData,headers=header)
response.encoding = "utf-8"
data = response.json().get("data")
print(data)
#
url2 = "http://ihrm-test.itheima.net/api/sys/profile"
Authorization = "Bearer " + data
header2 = {"Content-Type":"application/json","Authorization":Authorization}
#
response = requests.post(url,headers = header2 )
# url，encoding，cookies，headers
print(response.text)
print(response.url)
print(response.encoding)
print(response.cookies)
print(response.headers)
