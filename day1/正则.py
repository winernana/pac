import urllib
from urllib import request
headers = {
    "User-Agent":" Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10"
}

url = "http://www.baidu.com/"
# 创建请求对象
req = urllib.request.Request(url,headers = headers)
# 获取响应
response = urllib.request.urlopen(req)

# print(response)
# print(response.read())

# 解码
print(response.read().decode('utf-8'))