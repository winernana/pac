import json
import urllib
from urllib import request

headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

for i in range(20):
    url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=%d"%(i)

    #创建请求对象
    req = urllib.request.Request(url,headers=headers)
    #响应
    response = urllib.request.urlopen(req)
    jsontxt = response.read().decode()
    data = json.loads(jsontxt)
    # print(data)
    data_list = data.get('data')
    print(data_list)
    for movie in data_list:
        title = movie['title']
        casts = movie['casts']
        # with open('2.txt', 'a+') as fp:
        #     fp.write(title )
        #     fp.write(casts)

        print(title,casts)
