#!/usr/bin/env python
#encoding:utf-8

from flask import Flask
from flask import render_template
from spider import getBdMsg
from flask import request
from spider import getGgMsg


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/s')
def searchBd():
    #获取用户输入的关键字搜索
    keyword = request.args.get('wd')
    page = request.args.get('pn')
    html = getBdMsg(keyword,page)
    return html

@app.route('/search')
def searchGg():
    keyword = request.args.get('q')
    page = request.args.get('start')
    html = getGgMsg(keyword,page)
    return html


if __name__ == '__main__':
    app.run(debug=True,port=8000)