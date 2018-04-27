#/usr/bin/env python
#coding:utf-8

import requests


proxies = {
  "http": "http://127.0.0.1:1080",
  "https": "http://127.0.0.1:1080",
}

#爬取百度搜索结果
def getBdMsg(keyword,page):
    headers = {"User-Agent": "{Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",}
    #获取百度的源代码
    res = requests.get('https://www.baidu.com/s?&wd={}&pn={}'.format(keyword,page),headers = headers).text
    return res

def getGgMsg(keyword,page):
    headers = {"User-Agent": "{Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",}
    Res = requests.get('https://www.google.co.jp/search?&q={}&start={}'.format(keyword,page),headers=headers,proxies=proxies)
    print Res.headers['content-type']
    return Res
if __name__ == "__main__":
    print getGgMsg('python',0)
