from urllib import request
import urllib
import urllib.parse
# urllib.request.urlretrieve("http://www.baidu.com/",r"百度.html")

# request.urlretrieve("https://t1.hddhhn.com/uploads/tu/201903/587/3.jpg",r"美女.jpg")

strs = 'http://www.baidu.com/?username=哈哈&password=kkk'
# print(urllib.parse.quote(strs))

strs1 = "http%3A//www.baidu.com/%3Fusername%3D%E5%93%88%E5%93%88%26password%3Dkkk"
print(urllib.parse.unquote(strs1))

