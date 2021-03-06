#coding:utf8

class HtmlOutputer(object):
    #初始化
    def __init__(self):
        self.datas=[]
    
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        

    #将数据写入一个html中
    def output_html(self):
        fout=open('output.html','w')
       
       
        fout.write("<html>")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"% data['url'])
            fout.write("<td>%s</td>"% data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"% data['summary'].encode('utf-8'))
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()
    
    
    



