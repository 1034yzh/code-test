import urllib.parse
import urllib.request
import re

def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User_Agent','Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/55.0')
    response = urllib.request.urlopen(url)
    html = response.read()
    response.close()
    return html

def get_txturl(url,start,txt_num = "<dd> <a href="):
    html = url_open(url).decode('utf-8')
    a = 0
    if start == 0:
        for each in range(10):
            a = html.find(".html",a)+10
        start = a
    #使第一次find从第一章（而不是最新章节）开始 
    if txt_num == "<dd> <a href=":
        a = html.find(str(txt_num),start)+14
        b = html.find('"',a)
        get_url = "http://www.biqudu.com"+str(html[a:b])
    else:
        a = html.find(str(txt_num),start)-14
        b = html.find('"',a)
        get_url = url+str(html[a:b])

    return (get_url,b)


def download_txt(url,txtname,txt_num):
    print("正在下载，请稍后！")
    txt_url = get_txturl(url,0,txt_num)
    start = txt_url[1]
    while True:
        try:
            txt_url2 = txt_url[0]
            txt = url_open(txt_url2).decode('utf-8')
            with open(txtname,'a',encoding='gb18030') as f:
                #编码有点问题必须得用encoding='gb18030'
                a = re.search(r'<title>',txt).span()
                b = re.search(r'</title>',txt).span()
                title = txt[a[1]:b[0]]
                #print(title)
                f.write('\n'+title+'\n')
                a = re.search(r'readx()',txt).span()
                #b = re.search(r'chaptererror()',txt).span()
                temp = (a[0],a[1]+12)
                iter = re.finditer(r'<br/>|&nbsp;&nbsp;&nbsp;&nbsp;',txt)
                #使用两个正则规则结合是因为前后章节有两套代码（可能不止），所以有的章节会
                #出现空行的现象
                for i in iter:
                    #print(txt[temp[1]:i.span()[0]])
                    txtline = txt[temp[1]:i.span()[0]]
                    if txtline.split():
                        f.write(txtline+'\n')
                    temp = i.span()
            f.close()
            txt_url = get_txturl(url,start)
            start = txt_url[1]

        except ValueError:
            print("\n下载完成\n")
            break
        

if __name__=='__main__':
    txtname1 = input("输入小说名：")
    txtname = txtname1 + ".txt"
    url = "http://zhannei.baidu.com/cse/search?q="+urllib.parse.quote(txtname1)+"&click=1&s=13603361664978768713&nsid="
    #抓取的网站的网址中含有中文，应该先使用urllib.parse.quote()进行处理一下
    req=urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    html = url_open(url).decode('utf-8')
    txt_num=input("输入章节：")
    try:
        a = html.find('http://www.biqudu.com')
        b = html.find('"',a)
        print("网址："+html[a:b])
        url = html[a:b]
        download_txt(url,txtname,txt_num)
    except urllib.error.HTTPError:
        print("\n该网址出现错误，切换网址中。。。\n")
        a = html.find('http://www.biqudu.com',b)
        a = html.find('<a cpos="img" href=',a)+20
        b = html.find('"',a)
        print("网址："+html[a:b])
        url = html[a:b]
        download_txt(url,txtname,txt_num)

#本版本从目录处爬取小说每章网址，跟原来从每章网页中下一章处爬取下一章网址不同
#优化了下一章处网址错乱导致下载不能继续的bug
#并且删除了文本中的空行
