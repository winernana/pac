from urllib import  request
import urllib.parse

headers = {
    "User-Agent":" Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10"
}

# https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3&rsv_spt=1&rsv_iqid=0xee3fb7da000e135f&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=13&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&inputT=4899&rsv_sug4=6409

# https://www.baidu.com/s?wd=

kw = input("请输入查找的内容")
params = {
    'wd':kw
}
#将字典解析成参数字符串
params = urllib.parse.urlencode(params)
print(params)

# 创建url
url = 'http://www.baidu.com/?'+params
# print(url)

# 创建请求对象
req = urllib.request.Request(url,headers=headers)

# 获取响应
response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))
print(response.__dict__)