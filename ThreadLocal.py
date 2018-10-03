#-*- coding : utf-8 -*-
#在多线程环境下，每个线程都有自己的数据。局部变量只有线程自己能看见，
# 不会影响其他线程，而全局变量的修改必须加锁
import threading
class Student(object):
    def __init__(self,name):
        self.name = name
## 创建全局ThreadLocal对象:
#ThreadLocal解决了参数在一个线程中的各个函数之间的传递问题
local_sutdent = threading.local()
#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰

def process_student():
    #获取当前线程关联的student
    std = local_sutdent.student
    print('Hello %s(in %s)'% (std,threading.current_thread().name))

def process_thread(name):
    local_sutdent.student = name
    process_student()

t1 = threading.Thread(target = process_thread, args = ('lixu',),name = "Thread-A")
t2 = threading.Thread(target = process_thread,args = ('lidehu',),name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()