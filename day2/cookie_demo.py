import urllib.request
from http import cookiejar

#第一步创建cookiejar对象，用来管理cookie
cookies = cookiejar.CookieJar()

# 创建cookie 处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookies)

# 创建opener打开器
opener = urllib.request.build_opener(cookie_handler)

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.33 Safari/535.11"
}
url = 'http://www.baidu.com'

# 创建请求对象
req = urllib.request.Request(url,headers=headers)
response = opener.open(req)
print(cookies)