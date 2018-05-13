#/usr/bin/env python
#coding:utf-8

from multiprocessing import Pool
import  os
import time
import random


def run_Task(name):
    print('Task %s (pid=%s) is Running...') %(name, os.getpid())
    time.sleep(random.random() * 3)
    print('Task %s end. ' %name)


if __name__ == '__main__':
    print('Current process %s. ' %os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_Task, args=(i, ))
    print('Wait for a all subprocesses done ...')
    p.close()
    p.join()
    print('All sybprocesses done. ')