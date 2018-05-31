#/usr/bin/env python
#coding:utf-8

import requests
import re
import random
import urllib
import string

my_headers = [
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER"
            ]
proxies = {
  "http": "http://127.0.0.1:1080",
  "https": "http://127.0.0.1:1080",
}

random_header=random.choice(my_headers)
headers = {'user-agent':random_header}

"""
    :url: url的地址
    :pro: 如果为空，则不使用代理，要是有传入这个参数就是使用代理
    :auth: zjx
    :date:
    :returns: Html_text，url内容
    :Existing problems : 1.输入不能不输入  2.地址跟匹配规则需要自己根据实际来修改

"""

def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per

class get_Images(object):

    def get_UrlMsg(self, url, pro="n"):
        self.url = url
        self.pro = pro
        if self.pro == "n" :
            try:
                
                Res = requests.get(self.url, headers=headers)
                Html_text = Res.text
                return Html_text
            except Exception,e:
                print e
                return 1
        elif self.pro == "y" :
            try:
                Res = requests.get(self.url,headers=headers,proxies=proxies)
                Html_text = Res.text
                return Html_text
            except Exception,e:
                print e
                return 1
        else:
            print "Because you no choice %s,so no open proxy" % self.pro
            try: 
                Res = requests.get(self.url, headers=headers)
                Html_text = Res.text
                return Html_text
            except Exception,e:
                print e
                return 1


    def deal_Image(self,html,rule):
        self.html = html
        self.rule = rule
        #self.match_rule = match_rule
        try:
            Rulle = self.rule 
            match = re.compile(Rulle)
            images = re.findall(match,self.html)
            x = 0
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 4))
            #print images
            for i in images:
                '''
                :image_link:图片地址修改
                '''
                #print i
                image_link =  i
                image_Name=ran_str + str(x)
                urllib.urlretrieve(image_link,'D:\\images\\%s.jpg' %image_Name)
                x +=1
            return x
        except Exception,e:
            print e
            return 1
        

def main():
    """
    :Rulle: 匹配规则
    :url: 爬取的图片地址

    """

    #Rulle = '<img class="BDE_Image" src="(.+?\.jpg)"'
    #url = "http://tieba.baidu.com/p/4441169460?traceid="
    Rulle = '<img src="(.+?\.jpg)"'
    url = "http://75xxxx.com/htm/2018/4/24/p01/405800.html"
    #url = raw_input('Input you warn to visit Url: ')
    #rule = raw_input('you images rule:  \n')
    #print 'url++++:  ' + url
    #print 'rule+++:  ' + Rulle
    #Rulle = '%s' %rule

    image_object = get_Images()
    raw_data = raw_input('Are You Open proxy:(Yy/Nn) ')
    if raw_data:
        if_proxy = raw_data.strip()[0].lower()
        html=image_object.get_UrlMsg(url,if_proxy)
        
        
           
    
    #print html
    image_num=image_object.deal_Image(html,Rulle)
    print 'you download images number: ' + str(image_num)



if __name__ == '__main__':
    main()
        
