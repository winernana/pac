import urllib.request

#创建处理器对象
# HTTPSHandler支持https/ HTTPHandler支持http
http = urllib.request.HTTPHandler()
# 创建打开器对象
opener = urllib.request.build_opener(http)

# 打开url 相应数据
# url = "https://www.baidu.com/s?wd=柳岩"
response = opener.open("http://www.baidu.com/s?wd=liuyan")
print(response.read().decode())