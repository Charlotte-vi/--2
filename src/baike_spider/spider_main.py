#coding:utf8
#抓取python百度百科，右键审查元素得到html格式，确定抓去策略
#爬取百度百科ython词条相关1000个页面数据


#入口页面：http://baike.baidu.com/link?url=UKtBUEnrAMjN0W-JWJRDIYYDcgmOpw8stvEBAdpPetTJ11MBGH7n8lj_LtGYKjuuU7Dlv5-ocJw4fFG2zFwb3K
#url格式：词条url:/view/12345.htm
#数据格式：
#   标题：<dd class="lemmaWgt-lemmaTitle-title"><h1>***</h1></dd>
#   简介：<div class="lemma-summary" label-module="lemmaSummary">***<div>
#   页面编码：utf-8

from baike_spider import util_maneger,html_download,html_parser,html_output



class SpiderMain():
    #构造函数：初始化管理器，解析器，输出器,,,,
    def __init__(self):
        self.urls=util_maneger.UrlManager()
        self.downloader=html_download.HtmlDownLoader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_output.HtmlOutputer()
        
    #爬虫的调度程序
    def craw(self,root_url):
        count=1 #记录爬取的第几个url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            #异常处理
            try:
                new_url=self.urls.get_new_url()
                print 'craw%d:%s'%(count,new_url)
                #获取到url后启动下载器
                html_cont= self.downloader.download(new_url)
                #下载好页面后调用解析器来解析这个页面，得到新的url列表（当前爬取的url，下载好的数据）
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                #print 'url:%s\nName:%s\nSummary:%s'%(new_data['url'],new_data['title'],new_data['summary'])
                #分别处理获取到的两个数据（通过解析得到的新的url添加到url管理器中，同时进行数据收集）
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count==10:
                    break
                count=count+1          
            except:
                print 'craw faild'
        self.outputer.output_html()
       


if __name__=="__main__":
    root_url="http://baike.baidu.com/link?url=UKtBUEnrAMjN0W-JWJRDIYYDcgmOpw8stvEBAdpPetTJ11MBGH7n8lj_LtGYKjuuU7Dlv5-ocJw4fFG2zFwb3K"
    obj_spider=SpiderMain() #创建spider
    obj_spider.craw(root_url) #启动爬虫
   
    

