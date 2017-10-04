import re
import urllib.request
import random

def get_agentip():
    url = "http://www.xicidaili.com/nn/"
    head = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "Host":"www.xicidaili.com",
            "Referer":"http://www.xicidaili.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
            
        }
    req = urllib.request.Request(url,headers = head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    #print(html)
    iter = re.finditer(r'\d+\.\d+\.\d+\.\d+',html)
    iplist = []
    for i in iter:
        a = html.find('<td>',i.span()[1])+4
        b = html.find('</td>',a)
        port = html[a:b]
        ip = str(i[0])+":"+str(port)
        iplist.append(ip)

    return random.choice(iplist)


if __name__ == "__main__":
    print(get_agentip())

        
