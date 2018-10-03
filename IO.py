#-*- coding: utf-8 -*-
'''
#文件打开之后必须关闭
try:
    f = open('E:/WorldFile/test.txt','r')
    print(f.read())
finally:
    if f:
        f.close()


with open("E:/微信宣传稿/图片/gr.jpg",'rb') as f:
    print(f.read())

#StringIO顾名思义就是在内存中读写str
#要把str写入StringIO，我们需要先创建一个StringIO，
# 然后，像文件一样写入即可
from io import StringIO
f = StringIO()
f.write('hello,world! fesdgdsgrsgareggdg')
print(f.getvalue())#getvalue()函数直接获取写入的str
d = StringIO('hello\nhi\nGoodbye!\n')
s = d.read()
print(s.strip())
#函数strip()可以去掉\n换行符


#二进制数据的操作，需要使用BytesIO

#os.walk()的使用说明
#该方法返回一个三元tupple(dirpath, dirnames, filenames)
#dirpath是一个string，代表目录的路径
#dirnames是一个List，代表dirpath下的所有子目录的名字
#filenames是一个list，包含了非目录文件的名字.这些名字不包含路
# 径信息,如果需要得到全路径,需要使用os.path.join(dirpath, name).

#os.path.abspath(path)，显示path在操作系统中的绝对路径
#os.path.join(path, x)，将path和x拼接成当前操作系统兼容的路径形式
#os.listdir(path)，输出当前目录下的文件及子目录为list类型
#os.path.isdir(path) and os.path.isfile(path)判断路径为目录还是文件
import os

def dec_walk(path):
    for dirpath,dirnames,filenames in os.walk(path):
        for dir in dirnames:
            print('%s'% dir)

        for files in filenames:
            print('%s' % files)

if __name__ == '__main__':
    dec_walk('E:/微信宣传稿/图片')

#我们把变量从内存中变成可存储或传输的过程称之为序列化
#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
#Python提供了pickle模块来实现序列化
import pickle

d = dict(name = 'bob',age = 21,gender = 'male',score =  199)
c =  pickle.dumps(d)
#pickle.dumps()函数把任意对象序列化成一个bytes
#pickle.dump()函数可以把bytes写入一个file-like Object

try:
    f = open('E:/微信宣传稿/图片/dump.txt', 'wb')
    pickle.dump(d,f)
except:
    raise IOError(r"file don't exist")
f.close()
f = open('E:/微信宣传稿/图片/dump.txt','rb')
a = pickle.load(f)
#pickle.load()函数可以反序列化出对象
f.close()
print(a)
print(c)

import pickle
s = 'sgrewghreiohdfnb'
c = pickle.dumps(s)
try:
    f = open('E:/微信宣传稿/图片/test.txt', 'wb')
    pickle.dump(c,f)
except:
    raise FileExistsError
finally:
    if f:
        f.close()

with  open('E:/微信宣传稿/图片/test.txt','rb') as f:
    d = pickle.load(f)
print(d)
if s == d:
    print(True)
else:
    print(False)
'''
#JSON标准格式的转换
import json

d = dict(name = 'fds',age = 21,gender = 'female',score =329)
c = json.dumps(d)
#dumps()函数返回一个str,dump()函数可以把json写入一个file-like Object中
a = json.loads(c)
#loads（）函数把json的字符串反序列化
#load()函数从file-like Object中读取字符串并反序列化
print(a)
print(c)

class Student(object):
    def __init__(self,name ,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

s = Student('李旭',21,'female')

def StudentToDict(std):
    return{
       'name' : std.name,
        'age':std.age,
        'gender':std.gender,
    }
#ensure_ascii= False设置可以转化中文
print(json.dumps(s,ensure_ascii= False,default= StudentToDict))
#Student对象不是一个可序列化为JSON的对象,
#可选参数default就是把任意一个对象变成一个可序列为JSON的对象
#class的实例都有__dict__属性，它就是一个dict，用来存储实例变量,省去自己写转换函数
print(json.dumps(s,ensure_ascii= False,default= lambda obj:obj.__dict__))