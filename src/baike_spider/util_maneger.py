#coding:utf8

class UrlManager(object):
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()
    
    #向管理器中添加url
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        

    #管路器中是否有url
    def has_new_url(self):
        return len(self.new_urls)!=0
       

    #从管理器中获取新的待爬取的url
    def get_new_url(self):
        #pop方法从列表中获取一个URL，并从列表中移除这个url
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
        

    #添加批量url
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
        
    
    
    
    
    
    
    
    
