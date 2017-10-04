import urllib.request
import urllib.parse
import json

p="y"
while p=="y":
    sentence=input("请输入要翻译的部分：")

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'

    data = {
            "type" : "AUTO",
            "i" : sentence,
            "doctype" : "json",
            "xmlVersion" : "1.8",
            "keyfrom" : "fanyi.web",
            "ue" : "UTF-8",
            "action" : "FY_BY_CLICKBUTTON",
            "typoResult" : "true"
        }
    data = urllib.parse.urlencode(data).encode('UTF-8')

    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    #屏蔽python访问，进行伪装
    req=urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('UTF-8')

    #print(html)
    target=json.loads(html)
    #json。。。。。。
    print("翻译结果：%s"%(target['translateResult'][0][0]['tgt']))
    print("\n输入y继续")
    p=input()
    print("\n")

 
