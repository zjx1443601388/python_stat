#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年11月13日

@author: xin
'''

import os,time
import requests
import re,string
import random
import socket

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

class Get_token(object):
    def __init__(self,url):
        self.url=url
    def get_token(self):
        try:
            Res = requests.get(self.url,headers=headers,proxies=proxies)
            Html_text = Res.text
            return Html_text
        except Exception,e:
            print e
            return 1
            
if __name__ == '__main__':
    Url=raw_input('input your url: ')
    get = Get_token(Url)
    print get.get_token()