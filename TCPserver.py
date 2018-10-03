#-*- coding:utf-8 -*-
#TCP网络服务器
import socket,threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定端口
s.bind(('127.0.0.1',9999))
#监听端口,参数为连接客户端的最大数量
s.listen(5)
print('Waiting for connection....')

def TcpLink(sock,addr):
    print('Accept a new connection from %s:%s' % addr)
    sock.send(b'Welcome to my server ')
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send((b'Hello %s' % data.decode('utf-8').encode('utf-8')))
        sock.close()
        print('Connection from %s:%s closed!' % addr)

while True:
    #接受连接
    sock,addr = s.accept()
    #没接受一个连接就创建一个线程来处理
    t = threading.Thread(target = TcpLink,args = (sock,addr))
    t.start()

