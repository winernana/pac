import random
import urllib.request

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.33 Safari/535.11"
}

proxy = {
    "http":"http://58.249.55.222:9797"
}


# 设置代理
proxy_handler = urllib.request.ProxyHandler(proxies=proxy)

# 创建打开服务器
opener = urllib.request.build_opener(proxy_handler)

url = "http://www.qfedu.com/"

req = urllib.request.Request(url,headers=headers)

response = opener.open(req)
print(response)