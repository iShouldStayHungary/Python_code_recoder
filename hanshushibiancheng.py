# -*- utf-8 -*-
'''
#Python内建了map()和reduce()函数。
#map()接收两个参数，一个是函数，另一个是Interable,
#map()将传入的函数依次作用于序列的每一个元素，
# 并把结果作为新的Interor返回
def f(x):
    return x * x
a = list(map(f,[1,2,3,4,5]))
#Iterator是惰性序列，因此通过
# list()函数让它把整个序列都计算出来并返回一个list。
print(a)


#reduce(）函数的用法
#reduce()把一个函数作用在一个序列上，这个函数必须接收两个参数
#reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x,y):
    return x + y
a = reduce(add,[1,2,3,4,5])
print(a)

#将字符串转化为数字
def str_to_int(s):
    def fn(x,y):#可以将[1,2,3,4,5]转化为数字12345
        return x * 10 + y
    def  char_dic(s):
        digist = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return digist[s]
    return reduce(fn,map(char_dic,s))
print(str_to_int('12345'))


def up_first(s):#将首字母大写
    st = ''
    b = list(s)
    c = b[0]
    d = c.upper()
    b.remove(c)
    b.insert(0,d)
    for n in b:
        st = st + n
    return st
L1 = ['daf','fsdf','dggd','Fsfsdf']
L2 = list(map(up_first,L1))
print(L2)

#利用reduce求积
from functools import reduce
def prod(* a):
    def sumD(x,y):
        return x * y
    return reduce(sumD,a)
print(prod(*[1,2,3,4,5]))

#Python内建的filter()函数用于过滤序列。
#filter()也接收一个函数和一个序列
#filter()把传入的函数依次作用于每个元素，然后根据返回值
#是Ture还是False决定是保留还是丢弃该元素
def is_odd(n):#过滤出奇数
    return n % 2 == 1
a = list(filter(is_odd,[1,2,3,4,5,6,7,8,9,0]))
print(a)


#计算素数、
def  next_iter():#无限数列生成器
    n = 1
    while True:
        n = n + 1
        yield n
def not_divisible(n):#筛选器
    return lambda x : x % n > 0
def primes():
    yield 2
    it = next_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n),it)

for n in primes():
    if n < 10:
        print(n)
    else:
        break


def is_palindrome(n):
     s = list(str(n))
     c = list(reversed(s))
     if  s is c:
        return s
     else:
         return 0


def test():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
    b = list(filter(is_palindrome,list(range(200))))
    print(b)
    if a is b:
        print('测试成功！')
    else:
        print('测试失败！')
test()

#sorted()函数也是一个高阶函数，它还
# 可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
a = ['bob', 'About', 'Zoo', 'Credit']
c = sorted(a,key= str.lower)
print(c)
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    print(t[0])
    return t[0]
d = sorted(L,key= by_name)
print(d)


#返回函数
#不需要立刻求和，而是在后面的代码中，
# 根据需要再计算，可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        x = 0
        for n in args:
            x = x + n
        return x
    return sum()
#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1,2,3,4,5)#返回的是一个值
print(f)
#我们在函数lazy_sum中又定义了函数sum，并且，
# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。

#匿名函数
#关键字lambda表示匿名函数，冒号前的x表示函数参数
a = [1,2,3,4,5,6]
b = list(map(lambda x:x * x,a))
print(b)

L  = list(filter(lambda x: x % 2 == 1,range(1,20)))
print(L)


#装饰器，在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log # 装饰器
def now():
    print('dasfsadfsa')
f = now()
#print(now.__name__)

# 如果装饰器decorator本身需要传入参数，就需要一个返回一个decorator的高阶函数
import functools
def log(text):
    def decorator(func):
       # @functools.wraps(func) #把原始的__name__等属性复制到wrapper中，返回的时候
        #一起返回，这样调用now（）函数的属性就不变
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('excute')
def now():
    print('1233124')

f = now()
f
print(now.__name__)

def log(text):
    def decorator(func):
        def wrapp(*args, **kw):
            print('%s excute in %s' %(text,func.__name__))
            return func(*args,**kw)
        return wrapp
    return decorator

@log('tim()')
def tim():
    print("fsdgadsg")

tim()

#偏函数
#通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点
a = int('12345',base= 8)
print(a)
#int()函数可以把字符串转换为十进制整数,base指定字符串是几进制
def int2(x):
    return int(x,base = 2)
c = int2('1000')
print(c)

#利用偏函数定义
import functools
int2 = functools.partial(int,base = 2)
print(int2('1000'))
'''
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），
# 不应该被直接引用，比如_abc，__abc等；
#类似__xxx__这样的变量是特殊变量，
#可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量
#模块定义的文档注释也可以用特殊变量__doc__访问，
import  function
print(function.__doc__)
print(function.fact(4))