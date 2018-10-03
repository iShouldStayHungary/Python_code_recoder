#-*- coding: utf-8 -*-
#进程是由若干线程组成的，一个进程至少有一个线程
#Python的标准库提供了两个模块：_thread和threading，
# _thread是低级模块，threading是高级模块，对_thread
# 进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
import time ,threading
'''
def loop():
    print('thread %s is runing '% threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s  is runing   ' % threading.current_thread().name)
        time.sleep(1)
        print('thread %s ending'% threading.current_thread().name)

#threading模块有个current_thread()函数，它永远返回当前线程的实例。
# 主线程实例的名字叫MainThread，子线程的名字在创建时指定
print('thread %s is runing'% threading.current_thread().name)
t = threading.Thread(target = loop,name = 'loopthread')
t.start()
t.join()
'''
#进程锁lock
#多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝
# 存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，
# 所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大
# 的危险在于多个线程同时改一个变量，把内容给改乱了
balance = 0
#对线程加锁
lock = threading.Lock()

def save_money(n):
    global balance
    balance = balance + n

def barrow_money(n):
    global balance
    balance = balance - n

def get_balance():
    global balance
    return balance

def many_save(n):
    for i in range(1000000):#当循环次数足够大的时候，两个进程同时对一个变量进行修改，可能出错
        lock.acquire()#加锁
        try:
            save_money(n)
        finally:
            lock.release()#释放锁

def many_barrow(n):
    for i in range(1000000):
        lock.acquire()
#当多个线程同时执行lock.acquire()时，
#只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
        try:
            barrow_money(n)
        finally:
            lock.release()

t1 = threading.Thread(target = many_save,args = (500,))
t2 = threading .Thread(target = many_barrow,args = ( 500,))
t1.start()
t2.start()
t1.join()
t2.join()
print(get_balance())
#Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
