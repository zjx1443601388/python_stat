#/usr/bin/env python
#coding:utf-8

import requests
import os
import string,sys
import random

image_Save_Dir = 'D:\\images\\downImage\\'

loginData={'username': 'xxx',
           'userpass': 'xxxx'
           }

my_headers = [
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER"
            ]

random_header=random.choice(my_headers)
headers = {'user-agent': random_header}

url='xxxxxx'
urlVer= '{}/?module=admin_rndcode&rndkey=rndcode'.format(url)
urlLogin= '{}/?module=login'.format(url)

#获取cookie
def getVerCode(urlY):
    try:
        valcode = requests.get(urlY)
        f = open('D:\\valcode.png', 'wb')
        f.write(valcode.content)
        cook=requests.utils.dict_from_cookiejar(valcode.cookies)
        return cook
        f.close()
    except Exception, e:
        print e
        exit(1)

if __name__ == '__main__':
    cook= getVerCode(urlVer)
    #print cook
    valcode = requests.get(urlVer)
    #cook = requests.utils.dict_from_cookiejar(valcode.cookies)
    for key in cook:
        co = key + "=" + cook[key]
    print co
    headers['Cookie']= co
    #验证码打开
    from PIL import Image
    im = Image.open('D:\\valcode.png')
    im.show()
    vcode = raw_input('验证码：')
    loginData['rndcode'] = str(vcode)
    #登陆页面
    session = requests.session()
    resp = session.post(urlLogin, headers=headers, data=loginData)
    print session.get('{}'.format(url),headers= headers ).content
    for num in range(1, 3):
        resp1 = session.get('{}/?module=multimedia_img&id={}'.format(url,num), headers= headers)
        imageName = image_Save_Dir + str(num) + ".jpg"
        with open(imageName, 'wb') as f:
            f.write(resp1.content)

    print session.get('{}'.format(url), headers= headers).text

