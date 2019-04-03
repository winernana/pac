from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,  ,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'lxml')
# print(soup)
# print(soup.prettify()) #格式化代码

# print(soup.head)  #获取head标签，返回标签及里面的内容
# print(soup.head.title) #获取head标签下的title标签及内
# print(soup.head.name)  #返回标签的名字

# print(soup.p.attrs) #获取第一个p标签的所有属性 {'class': ['title']}

# print(soup.a.attrs) #获取第一个a标签下的所有属性{'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}

# print(soup.a.attrs['class']) #获取第一个a标签的class属性['sister']
# print(soup.a.attrs.get('id')) #获取第一个a标签的id属性 link1
# print(soup.a['id']) #获取第一个a标签的id属性 link1

# print(soup.p.string) #string 获取某个标签下的非标签字符串。返回的是个字符串。如果这个标签下有多行字符，那么就不能获取到了。The Dormouse's story
# print(soup.p.b.string)   #The Dormouse's story

# print(soup.p.text)  #节点内部的所有文本内容
# print(soup.p.b.get_text()) #节点内部的所有文本内容

# print(soup.a.next_sibling) #下一个节点 包含文本节点 （换行 空白都算文本节点）

# print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling) #上一个文本节点