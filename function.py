#-*- coding: utf-8 -*-


' function '


'''
a = abs # 变量指向函数abs(求绝对值)
sum = a(-11)# 所以也可以通过a调用abs函数
print(sum)

#定义函数 python函数可以同时返回多个值，但其实就是一个tuple。
def my_abs(x):
    if not isinstance(x,(int, float)):  #加入异常判断，增强程序的健壮性
        raise TypeError("bad opreator Type")
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-44))

def move(x, y):
    if not isinstance(x,(int, float)):
        raise TypeError("bad operator Type!")
    if not isinstance(y, (int, float)):
        raise TypeError("bad operator Type!")
    x = x * 2
    y = y * 2
    return x,y

a,b = move(1,2)
print(a,b)

#计算 ax^2 +bx +c的值
import  math
def quadratic(a,b,c):
    if not isinstance(a,(int ,float)):
        raise TypeError("bad Type")
    if not isinstance(a,(int ,float)):
        raise TypeError("bad Type")
    if not isinstance(a,(int ,float)):
        raise TypeError("bad Type")
    sum = b * b - 4 * a * c
    if sum < 0:
        print("无解，测试失败")
    elif sum == 0:
         x =  (-b + math.sqrt(sum)) / 2
         print(x)
    else:
        x = (-b + math.sqrt(sum)) / 2
        y = (-b - math.sqrt(sum)) / 2
        print(x,y)
quadratic(1,6,9)

#传入的参数个数是变化的（把list或者把tuple当做一个参数传去函数）
def cycle1(numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum
#b = cycle1([1,2,3]) #
c = [1,2,3,4]
b =cycle1(c)
print(b)
def cycle2(*numbers):#这样函数调用就可以更简单
    sum = 0
    for n in numbers:
        sum += n*n
    return sum
d= cycle2(1,2,3)
a = [1,2,3,4]
b = cycle2(*a)
print(b)
#**extra表示把extra这个dict的所有key-value用关
# 键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
def person(name,age,*args,**kw):# *args可变参数，args接收的是一个tuple
    #** kw是关键字参数，kw接收的是一个dict。
    print('name:',name,'age:',age,'fs:',args,kw)

person('liux',23,'sfs','fsf',job = '医生')
'''
#递归函数
def fact(x):
    if x == 1:
        return x
    else:
        return x*fact(x - 1)
#print(fact(30))