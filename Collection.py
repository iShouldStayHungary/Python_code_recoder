#-*- coding:utf-8 -*-

#nametuple()是一个函数，用来自定义创建一个tuple，并规定tuple元素的个数
#我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，
# 又可以根据属性来引用
from collections import namedtuple
Point = namedtuple('point',['x','y'])
p = Point(1,2)
print(p.x)

#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了
# ，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque([1,2,3,4])
q.append('x')
print(q)
q.appendleft(100)
print(q)

#Counter是一个简单的计数器,可以统计字符出现的个数
from collections import Counter
c = Counter()
for i in 'asfdsafetdasasadsdsa':
    c[i] = c[i] + 1
print(c)

import base64

def safe_base64_decode(s):
    ADDCOUNT =  4  - len(s)%4
    s = s + b'=' * ADDCOUNT
    return base64.b64decode(s)

if __name__ == '__main__':
    assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
    assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
    print('ok')