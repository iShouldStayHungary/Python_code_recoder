#-*- coding: utf-8 -*-
import socket
#TCP网络客户端
#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET指定使用IPv4协议，SOCK_STREAM指定使用面向流的TCP协议
s.connect(('127.0.0.1',9999))
#参数是一个tuple,包含地址和端口（80是web服务的标准端口）

#发送数据
s.send(b'I am lixu ,I just is a little client!')

#接收数据
buffer = []
while True:
    #指定一次最多接收的字节数
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)
print(data.decode('utf-8'))
#关闭连接
s.close()
#分离HTTP头
#header,html = data.split(b'\r\n\r\n',1)
#print(header.decode('utf-8'))

#with open(r'E:\sina.html','wb') as f:
   # f.write(html)