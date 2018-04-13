#/usr/bin/env python
#coding:utf-8
'''
date:2018-04-13
@auther:xiaoxin
'''


def showMacFactor(num):
    count = num / 2
    while count > 1:
        if num % count ==0:
            print 'largest factor of %d is %s' %(num,count)
            break
        
        count -=1
    else:
        print num, "is prime"
        
for eachNum in range(10,21):
    showMacFactor(eachNum)    