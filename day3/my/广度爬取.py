import re
import requests

headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
}
# 获取主页面内容
def get_content(url):
    try:
        res = requests.get(url,headers = headers)
        print(res.text)
        return res.text
    except:
        return ""

#获取子url列表
def get_son_url(url):
    contents1 = get_content(url)
    href_re = '<a.*?href="(.*?)".*?>'
    herf_list = re.findall(href_re, contents1, re.S)
    # print(herf_list)
    return herf_list


def width_crawer(start_url):
    #入队列 append() 出队列pop()
    url_quene = []
    url_quene.append(start_url)
    while len(url_quene)>0:
        url = url_quene.pop(0)
        print("\t" * width_dict[url], "当前层级:%d" % width_dict[url])
        if width_dict[url] <= 3:
            # 获取子url列表
            son_urls = get_son_url(url)
            for son_url in son_urls:
                #过滤有效的链接地址
                if son_url.startswith('http'):
                    # 去重
                    if son_url not in width_dict:
                        width_dict[son_url] = width_dict[url]+1
                        url_quene.append(son_url)
if __name__ == "__main__":
    url = "http://www.baidu.com/s?wd=柳岩"
    # 将key存放url  value存放层级1 2 3
    width_dict = {} #这里面存放我们所有的别表
    width_dict[url] = 1
    #开始爬取
    width_crawer(url)