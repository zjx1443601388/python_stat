#/usr/bin/env python
#coding:utf-8
'''
date:2018-04-17
@auther:xiaoxin
'''

import os
import shutil

for tmpdir in ('/tmp',r'c:\temp'):
    #判断文件是否存在
    if os.path.isdir(tmpdir):
        print '%s is existence' %tmpdir
        break
    
else:
    print 'no temp directory available'
    tmpdir=''
    
if tmpdir:
    os.chdir(tmpdir)
    cwd=os.getcwd()
    print '*** current temporary directory'
    print cwd
    
    print '** creating tempoary directory***'
    if os.path.isdir('example'):
        print 'example is existence' 
        shutil.rmtree('example')
    os.mkdir('example')
    os.chdir('example')
    cwd=os.getcwd()
    print '*** new working directory:'
    print cwd
    print '** original directory listing'
    print os.listdir(cwd)
    
    print '*** creating test file...'
    fobj =open('test','w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print '*** update directory listing'
    print os.listdir(cwd)
    
    
    
