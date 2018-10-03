#-*- coding:utf-8 -*-
#task_worker.py
import time,queue,sys
from multiprocessing.managers import BaseManager

#从BaseManager继承的QueueManagers
class QueueManager(BaseManager):
    pass

#由于QueueManager只能从网络上获取Queue，所以注册的时候只提名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器，也就是运行task_master.py的机器
server_addr = '10.112.25.129'
print("Connect to sever %s"% server_addr)
#端口设置保持一致
m = QueueManager(address = (server_addr,5000),authkey = b'asd')
#连接网络
m.connect()
#获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()

#从task队列取任务，并把结果写入到result队列
for i in range(10):
    try:
        n = task.get(timeout = 1)
        print('run task %d * %d..'%(n,n))
        r = '%d * %d = %d'%(n,n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('queue is empty')
print('worker exit')