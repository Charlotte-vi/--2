#coding:utf8

from bs4 import BeautifulSoup
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""



#根据html网页字符串创建Beautifulsoup对象
soup =BeautifulSoup(
                   html_doc,            #html文档字符串
                   "html.parser",       #html解析器
                   from_encoding='utf8' #html文档的编码   
                  )


#测试一：链接的名字 属性 文字
print '获取所有的链接'
links=soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()
    

#测试二：只获取其中一个链接
print '获取lacie的链接'
link_node=soup.find('a',href='http://example.com/lacie')
print link_node.name,link_node['href'],link_node.get_text()

#测试三：模糊匹配,前面加r表示如果正则表达式中有斜线只用一个即可，否则需要用斜线转义
print '正则匹配'
link_node=soup.find('a',href=re.compile(r"ill"))
print link_node.name,link_node['href'],link_node.get_text()


#测试四：指定P段落文字
print '获取p的文字'
p_node=soup.find('p',class_='title',string='The Dormouse\'s story')
print p_node.name,p_node.get_text()







#方法：find_all(name,attrs,string)域find参数一样
#节点名字，节点属性，节点文字

#查找所有标签为A的节点
soup.find_all('a')

#查找所有标签为a，链接符合/view/123.htm形式的节点
soup.find_all('a',href="/view/123.htm")
#bs4中对于名称，属性，节点文字都可以传入一个人正则表达式
#soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
soup.find_all('div',class_='abc',String="Python")


# #访问节点信息
# #得到节点<a href='1.html'>Python</a>
# 
# #获取查找到的节点的标签名称### node.name

# #获取a节点的href属性### node['href']

# #获取a节点的链接文字### node.get_text()


#以上可以实现对下载的网页的所有的节点的访问



