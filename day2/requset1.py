import requests

#GET请求
response = requests.get("http://www.qfedu.com/")
# print(response)  #<Response [200]>
# print(response.status_code)   #200
# print(response.url)   #http://www.qfedu.com/
# print(response.encoding)  #编码
# print(response.cookies)  #cookie
# print(type(response.text))  #字符串
# print(response.content)   #二进制
# print(response.content.decode())

headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

params = {
    "wd":"岛国教育片"
}
