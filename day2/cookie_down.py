import urllib.request
from http import cookiejar


# 创建文件 保存cookie
filename = "baidu.txt"
# 创建cookiejar对象，与文件交互  （采用LWPCookiejar)
cookie = cookiejar.LWPCookieJar(filename=filename)

# 创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)

# 创建打开器
opener = urllib.request.build_opener(handler)

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.33 Safari/535.11"
}