# -*- coding: utf-8 -*-

#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
import itertools
i = 0
'''
#conut创建一个无限的迭代器
natuals =  itertools.count(1)
for i in natuals:
    print(i)
    if i == 100:
        exit()
#可以通过takewhile()函数的判断条件截取一段有用的数列
n  = itertools.takewhile(lambda x : x <= 20 ,natuals)
print(list(n))

#cycle()会把传入的一个序列无限重复下去：
s = itertools.cycle('abcfs')
for n in s:
    print(n)
    i = i + 1
    if i == 20:
        exit()

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
s = itertools.repeat('bob',10)
for n in s:
    print(n)
    i += 1

print(i)


#chain()可以把一组迭代对象串联起来，形成一个更大的迭代对象
for n in itertools.chain('adb','XYZ'):
    print(n)

#groupby()可以把迭代器中相邻的重复元素跳出来放在一起
for key, group in itertools.groupby('AAAHHHIIIIDMWIJNSFFW'):
    print(key,list(group))
'''