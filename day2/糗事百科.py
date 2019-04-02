import urllib
import re
from urllib import request

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.33 Safari/535.11"
}

url = "https://www.qiushibaike.com/text/"

# 抓取数据
# 创建请求对象
req = urllib.request.Request(url,headers = headers)
# 获取响应
response = urllib.request.urlopen(req)
msg1 = response.read().decode()

text1_re ='<div class="content">(.*?)</div>'

strs = re.findall(text1_re,msg1,re.S)
# print(strs[0])

# text2_re = '<span>(.*?)</span>'
# strs1 = re.findall(text2_re,strs[0],re.S)
# print(strs1[0].strip())

for str in strs:
    text2_re = '<span>(.*?)</span>'
    strs1 = re.findall(text2_re, str, re.S)
    print(strs1[0].strip())
    # with open('1.txt','a+') as fp:
    #     fp.write(strs1[0].strip())