import urllib.parse
import urllib.request
import re

def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User_Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    response.close()
    return html

def get_txturl(url,txt_num = "下一章"):
    html = url_open(url).decode('utf-8')
    a = html.find(str(txt_num))-14
    b = html.find('"',a)
    return (html[a:b],html[b-4:b])


def download_txt(url,txtname,txt_num):
    #txt_num=input("输入章节：")
    print("正在下载，请稍后！")
    #url="http://www.biqudu.com/8_8909/"
    txt_url = get_txturl(url,txt_num)
    #print(txt_url[0])
    #print(txt_url[1])
    while txt_url[1]=="html":
        txt_url2 = url+str(txt_url[0])
        #print(txt_url2)
        txt_url = get_txturl(txt_url2)
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
                f.write(txt[temp[1]:i.span()[0]]+'\n')
                temp = i.span()
        f.close()

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

#该版本已经能实现在笔趣网上爬取小说的功能了，但是每次搜索小说时有个缺陷
#如果第一个和第二个网址都错误，那么就会出现错误。
#本版重点get点就是在所爬取的网站网址含有中文时要使用urllib.parse.quote()进行处理
#这个就是最终版了，也没有什么想加上去的功能了。
