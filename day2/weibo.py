import urllib.request
import  http.cookiejar
import urllib.parse

#创建cookiejar对象
cookie = http.cookiejar.CookieJar()

# 创建处理器对象
handler = urllib.request.HTTPCookieProcessor(cookie)

#根据处理器对象 创建打开对象
opener = urllib.request.build_opener(handler)

