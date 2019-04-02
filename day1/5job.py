import re
from urllib import request
import urllib

headers = {
    "User-Agent":" Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10"
}

url="https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

# 创建请求
req = urllib.request.Request(url,headers=headers)
# 获取服务器响应数据
# print(req.get_full_url())

response = urllib.request.urlopen(req)
# print(response)
# 解码
res = response.read().decode('utf-8')
print(res)
# print(type(res))

# 处理数据 拿到标签中间所有的内容
# 获取需要的div对象
jobnum_re = '<p class="result"></p>'
# 生成正则表达式对象
obds = re.compile(jobnum_re,re.S)
strs = obds.findall(res)[0]
# print(strs)