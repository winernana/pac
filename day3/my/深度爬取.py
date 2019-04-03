import re
import urllib
from urllib import request
import requests

headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
}
# 获取网页内容
def get_content(url):
    try:
        res = requests.get(url,headers=headers)
        return res.text
    except:
        return ""
# 获取子url列表
def get_son_url(url):
    contents1 = get_content(url) #页面内容
    href_re = '<a.*?href="(.*?)".*?>'
    herf_list = re.findall(href_re,contents1,re.S)
    return herf_list

def deep_crawer(url):
    if deep_dict[url]>8:
        return
    print("+" * 20)
    print("\t" * deep_dict[url], "当前层级:%d" % deep_dict[url])
    son_urls = get_son_url(url)
    for son_url in son_urls:
        #http开头的才是有效的链接
        if son_url.startswith('http'):
            if son_url not in deep_dict:
                # 子url的层级就是父url的层级+1
                deep_dict[son_url] = deep_dict[url]+1
                deep_crawer(son_url)
                print(son_url)



if __name__ == "__main__":
    url = "http://www.baidu.com/s?wd=美女"
    # 将key存放url  value存放层级1 2 3
    deep_dict = {} #这里面存放我们所有的别表
    deep_dict[url] = 1
    #开始爬取
    deep_crawer(url)