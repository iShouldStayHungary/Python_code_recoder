# -*- coding: utf-8 -*-
'''
print('I\'m \"ok\".')
print('\\n')             #使用\字符来进行转义
print(r"'\\\\\\nn\\n\'")  # r""双引号中的内容不用转义

print(ord('a'))  # ord()函数把字符转换成ASCII码
print(chr(66))   #chr()函数把ASCII码转换成字符

多行注释
%运算符就是用来格式化字符串的。在字符串内部，
%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，
后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。


name  = input()
age  = input()
print("我的名字是：%s,年龄是：%s"% (name ,age))  # input()函数输入都是字符串类型，所以输出都用%s,
print('我的名字是：{0},年龄是：{1}'.format(name,age)) # 也可以用format()函数进行格式化输入输出


#python 列表
#list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates = ['vsdijg','sdggs','sgdew']
classmates.append('sdnyv') #追加元素到末尾
classmate = ['csa', 'asca', 'asf']
a = classmate[-1]
print(a)   #Python代码必须对齐
classmate.insert(1,'联系') #列表的插入
print(classmate)
classmate.pop(-1) #列表的删除
classmate[1] = classmates #列表的替换，列表中也可以插列表
print(classmate)

#元组tuple 一旦初始化就不能改变,所以定义的时候就必须初始化
student = ('csfd ','sdvs','srtg','efgr')
t = (1,2)
print(student)
print(t)
#定义一个空的tuple
s =()
print(s)
#定义只有一个元素的tuple，必须加逗号
h = (2,)#避免和（）的数学含义冲突
print(h)
#定义一个可变的tuple：tuple里面嵌套一list
b  = ('df','dddddd',['ds','dnana'])
print(b)
b[2][1] = 'XXXXXXXX'
print(b)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][2])

#条件判断 if之后的缩进
age = int(input())#input()函数输入的是字符串
if age < 20:
    print("年龄太大了！")
    print("超过了限制年龄！")
elif age > 23:
    print("拜拜！")
else:
    print("家法国人")

#循环
#第一类循环 for   in
names  = ['dsvsss','sdvfe','et5r']
for name in names:  #注意：
    print(name)
#Python提供range（）函数生成一个整数序列,在通过list()函数转换成list
a = list(range(101))
sum  = 0
print(a)
for x in a:
    sum += x
print(sum)

#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
result = 0
n = 99
while n > 0:
    result += n
    n  = n - 2
    if n % 2 == 0:
        continue
    else:
        print(n)
print(result)

#          dic字典也称为键值对
#由于一个key只能对应一个value，所以，
# #多次对一个key放入value，后面的值会把前面的值冲掉：
d = {'lixu':1602,'lidehu':1603,'liangyuhing':1605}
print(d['lixu'])#通过key查找value的值
print(d.get('lixu'))#当key不存在时返回none
print(d.get('assf'))
print(d.get('asf'),-1)#自己制定返回值
print(d)
d.pop('lixu')#删除元素
print(d)
'''

#    set 集合（不重复，重复的key无效），支持集运算
#创建一个set，需要一个list作为输入集合
a = [122,2,3,4]
print(a)
b = ['sdfd','dsg',2,3]
t = ('李旭','safa')
t2 = ('李德华','dwf')
e =set(t + t2)
print(e)
c = set(b)
s = set(a )
s.add(666)#添加元素
s.remove(4)#删除元素
print(s)
print(c)
print(s | c)#集合的并
print(s & c) # 集合的交