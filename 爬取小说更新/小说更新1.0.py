import urllib.request
from html.parser import HTMLParser

class hp(HTMLParser):  
    div_text = False  
      
    def handle_starttag(self,tag,attr):  
        if (tag == 'div'and attr[0][1]=='content') or tag == 'title':  
            self.div_text = True
            #print (dict(attr))  
              
    def handle_endtag(self,tag):  
        if tag == 'div'or tag == 'title':  
            self.div_text = False  
              
    def handle_data(self,data):  
        if self.div_text:  
            print (data) 

def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User_Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_txt(url,txt_num = "下一章"):
    html = url_open(url).decode('utf-8')
    a = html.find(str(txt_num))-14
    b = html.find('"',a)
    return (html[a:b],html[b-4:b])


def download_txt():
    txt_num=input("请输入章节：")
    url="http://www.biqudu.com/8_8909/"
    txt_url = get_txt(url,txt_num)
    print( txt_url[0])
    print( txt_url[1])
    while txt_url[1]=="html":
        txt_url2 = url+str(txt_url[0])
        print(txt_url2)
        txt_url = get_txt(txt_url2)
        txt = url_open(txt_url2)
        yk = hp()
        yk.feed(txt.decode('utf-8'))
        yk.close
        #print(txt.decode('utf-8'))
        
        
if __name__=='__main__':
    download_txt()
#只能实现《寒门崛起》这本小说的更新，输入章节，可以显示出本章节一直到最新章节
#的所有内容。但是，无法保存显示的内容，暂时不知道怎样将feed()函数所打印出来的
#内容进行保存。下一版本，想使用正则表达式进行优化，实现保存。
