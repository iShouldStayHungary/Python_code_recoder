#-*- coding: utf-8 -*-
#进程之间的通信
#Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
#以Queue为例，在父进程中创建两个进程，一个往Queue中写数据，一个往Queue中读数据
from multiprocessing import Process , Queue

import os,time,random

#写数据执行的函数
def write(q):#需要传入一个进程作为参数
    print('process will write: %s',os.getpid())
    for value in ['Q','W0','E']:
        print('Put %s in queue'% value)
        q.put(value)#put()函数把数据加入进程中
        time.sleep(random.random())#主进程暂停100ms

#读数据的函数
def read(q):
    print("Process will read:%s"% os.getpid())
    while True:
        value  = q.get(True)#由于参数是True ,所以是一个死循环
        print("Get %s from queue"% value)

if __name__ == '__main__':#main是所有进程的父进程
    q = Queue()#创建子进程
    qw = Process(target=write, args=(q,))
    qr = Process(target=read, args=(q,))
    qw.start()
    qr.start()
    qw.join()#等待qw结束
    qr.terminate() #死循环强行结束
