# -*- coding:utf-8 -*-

#UDP网络服务器

import socket,threading

#SOCK_DGRAM指定socket是面对UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定端口
s.bind(('127.0.0.1',8888))


print('bind udp on 8888')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)