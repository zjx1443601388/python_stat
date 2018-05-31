#/usr/bin/env python
#coding:utf-8

import hashlib
import os
import sys

filelist= []
fileMd5={}
imagesDir = 'D:\\images\\z'

#imagesDir = 'D:\\images\\testImage'

def getImage(imageDir):
    #dir = root + 'images/'
    filenames = os.listdir(imageDir)  # 返回指定目录下的所有文件和目录名
    for fn in filenames:
        fullfilename = os.path.join(imageDir, fn)    # os.path.join--拼接路径
        filelist.append(fullfilename)           # filelist里存储每个图片的路径
    return filenames

#print getImage(imagesDir)

def getFirlMd5(filename):
    md5Name = hashlib.md5(filename).hexdigest()
    return md5Name

if __name__ == '__main__':
    filrList = getImage(imagesDir)
    for i in filelist:
        with open(i,'rb') as f:
            tmpMd5 = getFirlMd5(f.read())
            if fileMd5.has_key(tmpMd5):
                fileMd5[tmpMd5].append(i)
            else:
                fileMd5[tmpMd5]=[i]
    for key in fileMd5:
        if len(fileMd5[key]) > 1:
            print fileMd5[key]
            #os.remove(fileMd5[key][1])



