#-*- coding: utf-8 -*-
#multiprocessing 模块提供了一个process类来代表个进程
'''
from multiprocessing import Process

import os

#getpid()得到子进程的ID
#getppid()得到父进程的ID

def run_rpoc(name):
    print('Run child process %s(%s)'%(name,os.getpid()))

#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，
# 用start()方法启动
if __name__ == '__main__':
    print('Parent process %s.'% os.getpid())
    p = Process(target = run_rpoc,args = ('test',) )
    print('Child process will start')
    p.start()
    p.join()
#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
#如果要启动大量的子进程，可以用进程池的方法批量创建子进程

from multiprocessing import Pool

import os ,time,random

def long_time_task(name):
    print('Run task %s(%s)'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f secondds.'%(name,(end - start)))

if __name__ == '__main__':
    print('Parent process %s'% os.getpid())
    p = Pool(4)#用进程池创建4个进程
    for i in range(5):
        p.apply_async(long_time_task,args = (i,))
    p.close()#进程全部关闭，
#对Pool对象调用join()方法会等待所有子进程执行完毕，
# 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()#
'''
#subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
import subprocess

print('$nslookuo www.python.org')
#r = subprocess.call(['nslookup','www.pyhton.org'])
#如果子进程还需要输入，则可以通过communicate()方法输入：
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code',p.returncoed)
p.close()
p.join()

