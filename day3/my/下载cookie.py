import urllib.request
from http import cookiejar

# 创建文件 保存cookie
filename = "kk.txt"
cookie = cookiejar.LWPCookieJar(filename = filename)

# 创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)

# 创建打开器
opener = urllib.request.build_opener(handler)

headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
}

url = "http://www.baidu.com/"
req = urllib.request.Request(url=url,headers=headers)
response = opener.open(req)
print(response)
print(cookie)
cookie.save()