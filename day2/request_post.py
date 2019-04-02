import requests

headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url = "http://fanyi.youdao.com/?keyfrom=fanyi.logo"
english = 'hello'
data={
    'i': '你好',
    'from': 'zh-CHS',
    'to': 'en',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': 15541932932027,
    'sign': 'fe00469f2d34c1f26915e4ec7ddadfe5',
    'ts': '1554193293202',
    'bv': 'dd2b93e81878a34395ababe256bd5d0b',
    'doctype': 'json',
    'version': 2.1,
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': False,
}
response = requests.post(url,headers=headers,data=data)
print(response.status_code)
print(response.text)
