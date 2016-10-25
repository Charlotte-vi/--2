#coding:utf8

#方法三在pageDowFunc中

import urllib2
#方法二
url="http://www.baidu.com"
request =urllib2.Request(url)
#将爬虫伪装成一个浏览器.header value
request.add_header("user-agent","Mozilla/5.0")
response1=urllib2.urlopen(request)
print response1.getcode()
print len(response1.read())

#方法一：
print "方法一"
response2=urllib2.urlopen(url)
print response2.getcode()
print len(response2.read())




