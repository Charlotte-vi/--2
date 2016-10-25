# -*- coding: utf-8 -*
#对应opener，，，的py文件

#方法3：在内存中（关系数据库，高速缓存），且是添加特殊情景处理的网页下载

import urllib2,cookielib

#创建cookie容器
cj=cookielib.CookieJar()
#创建一个opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#安装opener
urllib2.install_opener(opener)
#使用带有cookie的urllib2访问网页
url="http://www.baidu.com"
req=urllib2.Request(url)
response=urllib2.urlopen(req)
print response.getcode()
#code=response.read()
#print code
print cj #输出cookie信息
print response.info()

print len(response.read())#输出网页的长度


