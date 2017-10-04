import urllib.request
import re

def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User_Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_txturl(url,txt_num = "下一章"):
    html = url_open(url).decode('utf-8')
    a = html.find(str(txt_num))-14
    b = html.find('"',a)
    return (html[a:b],html[b-4:b])


def download_txt():
    txt_num=input("请输入章节：")
    print("正在下载，请稍后！")
    url="http://www.biqudu.com/8_8909/"
    txt_url = get_txturl(url,txt_num)
    #print(txt_url[0])
    #print(txt_url[1])
    while txt_url[1]=="html":
        txt_url2 = url+str(txt_url[0])
        #print(txt_url2)
        txt_url = get_txturl(txt_url2)
        txt = url_open(txt_url2).decode('utf-8')
        with open('hmjq.txt','a',encoding='gb18030') as f:
            #编码有点问题必须得用encoding='gb18030'
            a = re.search(r'<title>',txt).span()
            b = re.search(r'</title>',txt).span()
            title = txt[a[1]:b[0]]
            #print(title)
            f.write(title+'\n')
            a = re.search(r'readx()',txt).span()
            #b = re.search(r'chaptererror()',txt).span()
            temp = (a[0],a[1]+12)
            iter = re.finditer(r'<br/><br/>|&nbsp;&nbsp;&nbsp;&nbsp;',txt)
            #使用两个正则规则结合是因为这本书前后章节有两套代码，所以有的章节会
            #出现空行的现象
            for i in iter:
                #print(txt[temp[1]:i.span()[0]])
                f.write(txt[temp[1]:i.span()[0]]+'\n')
                temp = i.span()
    f.close()
                
        
if __name__=='__main__':
    download_txt()


#输入章节开始下载，至最新章节，但是速度有点慢。在文件中换行没有问题了，
#排版也是ok的，但是有些穿插在代码中的广告，也是没有办法了。
#下一个版本争取爬取该网站所有小说，不能只局限于这个小说。
