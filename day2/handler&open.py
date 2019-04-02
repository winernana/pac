import  urllib.request

#创建处理器对象
http = urllib.request.HTTPHandler()   #支持http
# https = urllib.request.HTTPSHandler()  #支持https

# 调用方法使用这个对象   创建打开器对象
opener = urllib.request.build_opener(http)

# 打开url
# response = opener.open('http://www.baidu.com/')
# print(response.read().decode())
# 创建 全局打开器

urllib.request.install_opener(opener)
response = urllib.request.urlopen("http://www.qfedu.com/")
print(response.read().decode())