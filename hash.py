#-*- coding:utf-8 -*-
#摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
#摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，
# 目的是为了发现原始数据是否被人篡改过。
import hashlib
'''
#我们以常见的摘要算法MD5为例
md5 = hashlib.md5()
md5.update('how to learn python well!'.encode('utf-8'))
print(md5.hexdigest())
#如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：

#另一种常见的摘要算法是SHA1
sha1 = hashlib.sha1()
sha1.update('bob'.encode('utf-8'))
sha1.update('2996654722@qq.com'.encode('utf-8'))
sha1.update('2996654722'.encode('utf-8'))
print(sha1.hexdigest())
'''
#6a3dab2691c8d29d16080a1d09469dd51c08e192

def class_sha1(username,email,password):
    sha1 = hashlib.sha1()
    sha1.update( (username + email + password + 'the salt').encode('utf-8'))

    return '6a3dab2691c8d29d16080a1d09469dd51c08e192'

def log(username,email,password):
    sha2 = hashlib.sha1()
    sha2.update((username + email + password +'the salt').encode('utf-8'))

    result_class = class_sha1(username,email,password)
    result_log = sha2.hexdigest()

    if result_log == result_class:
         print('log succefully!')
    else:
         print('fail log!')

if __name__ == '__main__':
    log(input(),input(),input())
    print('saf')