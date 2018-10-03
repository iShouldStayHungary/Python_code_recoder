#Sclice 切片
'''
student = ['sf','fss','sgdr','gd','dg','gds']
#print(student[0:3]) #切片输出，不用循环，很便利
print(student[:-2])
L = list(range(100))
#print(L[:20:2])#每两个取一个
def trim(*stri): # 删除字符串中的空格
    cha = ''
    n = 0
    for item in stri:
        if(stri[n] != ' '):
            cha += stri[n]
            n += 1
        else:
            n += 1
    return cha


    if(stri[0] == ' ' and  stri[-1] == ' '):
        return stri[1:-2]
    elif(stri[0] == ' ' and  stri[-1] != ' '):
        return stri[1:]
    elif(stri[0] != ' ' and stri[-1] == ' '):
        return stri[:-2]
    else:
        return stri

s = "    hello   "
b = trim(*s)
print(b)

#列表生成式
#第一种:使用list()函数实现
a  = list(range(1,11))
print(a)

#第二种使用for循环实现
L = []
for x in range(1,11):
    L.append(x * x)
print(L)

#第三种：使用列表生成式实现
print([x * x for x in range(1,11)])
print([x * x for x in range(1,11) if x % 2 == 0]) # 用if进行筛选
# 还可以使用两层循环实现全排列
print([m + n for m in "ABC" for n in "abc"])

import os
print([d for d in os.listdir('.')])
# os.listdir()函数可以列出当前路径下的文件目录

#for循环可以同时使用多个变量，例如字典中的items（）可以同时迭代key和value
d = {'x':'a','y':'b','z':'c'}
for key ,value in d.items():
    print(key,'=',value)

L = ['AAFF','FSTEV','ESHEA']
print([s.lower() for s in L])#lower()把字符串转换成小写uper()转换成大写

#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，
# 列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
# 不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了。
#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环
# 的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
# 从而节省大量的空间。在Python中，这种一边循环一边计算的机制，
# 称为生成器：generator。
g = (x * x for x in range(10))#生成器g只存储算法
#如果要打印出生成器g中的每一个元素，用next()函数,
# 每次代用next()函数计算出后续的元素
for n in g:
    print(n)

def fib(max): #菲波那切数列
    n,a,b = 0 ,0,1
    while n < max:
        print( b, end=',')
        a, b =  b, a + b
        n += 1
fib(6)
g = fib(6)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as a:
        print(a.value) #想要获取generator的返回值就必须捕获fib()的StopInteration中的value
#要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def fib (max):
    n, a, b = 0, 0, 1
    while n < max :
        a,b = b,a + b
        n += 1
        yield a
    return "Done"
for n in fib(6):
    print(n)
#当一个函数是generator的时候，通常不用next（）函数一个一个的输出，
#二十利用for循环输出
#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator：
#最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，
# 遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step1')
    yield 1 #遇到yield就中断，下次再执行的时候就从上次中断的地方开始执行
    print('step2')
    yield 2
#调用generator的时候先生成一个generator对象，然后用next()函数不不断获取下一个返回的值
a = odd()
next(a)
next(a)

def yang(max):#杨辉三角
    a =[1]
    n = 0
    while n <= max:
        yield a
        a = [a[n] + a[n+1] for n in range(len(a) - 1)]
        a.insert(0,1)
        a.append(1)
        n  = n + 1
g = yang(6)
for n in g:
    print(n)

'''
