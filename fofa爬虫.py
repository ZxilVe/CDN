import requests
from lxml import etree
import random
import time
import urllib
import base64

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
}

#这里的代理IP需要自己去爬取或者添加
proxylist = [
    {'HTTP': '112.84.54.35:9999'},
    {'HTTP': '175.44.109.144:9999'},
    {'HTTP': '125.108.119.23:9000'}
]

proxy = random.choice(proxylist)

def loadpage(url,begin,end):
    for page in range(begin,end+1):
        print("正在爬取第"+str(page)+"页：")
        fullurl = url+"&page="+str(page)
        response = requests.get(fullurl,headers=headers,proxies=proxy).text
        html = etree.HTML(response)
        req = html.xpath('//div[@class="fl box-sizing"]/div[@class="re-domain"]/a[@target="_blank"]/@href')
        result = '\n'.join(req)
        with open(r'url.txt',"a+") as f:
            f.write(result+"\n")
            print("----------------第"+str(page)+"页已完成爬取----------------"+'\n')


if __name__ == '__main__':
    q = input('请输入关键字,如 "app="xxx" && country="CN"：等等')
    begin = int(input("请输入开始页数 最小为1："))
    end = int(input("请输入结束页数 最大为5："))
    cookie = input("请输入你的Cookie：")

    cookies = '_fofapro_ars_session='+cookie+';result_per_page=20'
    headers['cookie'] = cookies

    url = "https://fofa.so/result?"
    key = urllib.parse.urlencode({"q":q})
    key2 = base64.b64encode(q.encode('utf-8')).decode("utf-8")

    url = url+key+"&qbase64="+key2

    loadpage(url,begin,end)
    time.sleep(5)