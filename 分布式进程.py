# -*- coding: utf-8 -*-
#task_master.py
#发送任务的进程，
import random ,time ,queue
from multiprocessing.managers import BaseManager
#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列
result_queue = queue.Queue()
#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

#把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue',callable = lambda : task_queue)
QueueManager.register('get_result_queue',callable =  lambda : result_queue)

#绑定端口4000，设置验证码'asd'
manager = QueueManager(address = ('',5000),authkey = b'asd')
#启动Queue
manager.start()
#获取通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#发布任务
for i in range(10):
    n = random.randint(0,1000)
    print('put task %d'% n)
    task.put(n)

#从Queue中读取结果
print('Try get result...')
for i in range(10):
    r = result.get(timeout = 10)
    print('Result : %s'% r)

#关闭
manager.shutdown()
print('manager exit')

