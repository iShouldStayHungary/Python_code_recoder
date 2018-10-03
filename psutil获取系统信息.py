#-*- coding:utf-8 -*-

#在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块
import psutil,os
'''
#获取cpu的逻辑数量
print(psutil.cpu_count())


#cpu物理核心，2是双核超线程，4是4核非超线程
print(psutil.cpu_count(logical = False))

#获取cpu当前用户，系统，空闲时间
print(psutil.cpu_times())

#获取cpu的内存大小，和利用率
print(psutil.virtual_memory())

#获取交换区的大小
print(psutil.swap_memory())

#获取磁盘的分区信息
print(psutil.disk_partitions())

#获取磁盘的使用率
print(psutil.disk_usage('c:/'))

#获取磁盘的IO信息
print(psutil.disk_io_counters())

#获取网络读写字节/包的个数
print(psutil.net_io_counters())

#获取网络接口的信息
print(psutil.net_if_addrs())

#获取网路接口的状态
print(psutil.net_if_stats())

#获取当前网络连接信息
print(psutil.net_connections())
'''
#获取所有进程的ID
print(psutil.pids())
p = psutil.Process(6744)
#进程的名称
print(p.name())
#进程的.exe路径
print(p.exe())
#进程启动的命令行
print(p.cmdline())
#父进程的ID
print(p.ppid())
#父进程
print(p.parent())
#子进程
print(p.children())
#进程的状态
print(p.status())
#进程的用户名
print(p.username())
#进程的创建时间
print(p.create_time())

#进程使用的cpu时间
print(p.cpu_times())

#进程使用内存
print(p.memory_info())

#进程打开的文件
print(p.open_files())

#进程相关的网络连接
print(p.connections())

print(psutil.test())