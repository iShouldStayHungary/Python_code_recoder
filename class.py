#-*- coding : utf-8 -*-
' class'
'''
#面向对象最重要的概念就是类（Class）和实例（Instance）
#如果要让内部属性不被外部访问，可以把属性的名称前加上两
# 个下划线__，在Python中，实例的变量名如果以__开头，就变
# 成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):#继承自object类
    count = 0
    def __init__(self,name,score,gender,hight):
        self.hight = hight
        self.__name = name #__表示私有变量
        self.__score = score
        self.__gender = gender
        Student.count += 1
#在Python中，变量名类似__xxx__的，也就是以双下划线开头，
    # 并且以双下划线结尾的，是特殊变量，特殊变量是可以
    # 直接访问的，不是private变量
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    def get_gender(self):
        return self.__gender

    def set_name(self,name):
        self.__name = name

    def set_score(self,score):
        self.__score = score

    def set_gender(self,gender):
        self.__gender =  gender


    def print_obj(self):
        print("%s的成绩是：%s,性别是：%s"%(self.__name,self.__score,self.__gender))
#__init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到self，
# 因为self就指向创建的实例本身有了__init__方法，
# 在创建实例的时候，就不能传入空的参数了，必须传入
# 与__init__方法匹配的参数，但self不需要传，
# Python解释器自己会把实例变量传进去
bart = Student('lixu',56,'male',123)
bart.set_name('sfssdgf')
bart.print_obj()
print(type(bart))
#当我们拿到一个对象的时候，可以用type()函数判断他的类型
print(isinstance([1,2,3],(list, tuple)))
#优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”
print(dir(bart)) #利用dir()函数可以返回该对象的所有属性和方法
#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
#函数只能判断对象的公有属性，私有属性不能访问
#hasattr()函数判断对象是否有该属性
#getattr()函数返回对象的属性
#setattr（）函数设置对象的属性
print(hasattr(bart,'hight'))
print(getattr(bart,'hight'))
setattr(bart,'hight',10000)
print(getattr(bart,'hight'))
print(bart.hight)
s =  Student()
c = Student()
print(Student.count)

from types import  MethodType
def set_hight(self,hight):
    self.hight = hight
s.set_hight = MethodType(set_hight,s)#给对象绑定一个方法
s.set_hight(29)
print(s.hight)

#使用__slots__
#如果我们想要限制实例的属性怎么办？比如，
# 只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object): #该类的实例只允许定义name和age属性
    #但是在该类的子类中，该限制不起作用
    #__slots__ = ('name','age')
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property  #property把age（）变成实例的属性
    def age(self):
        return self.age

    @age.setter  #@property本身又创建了另一个装饰器@age.setter
    def age(self,value):
        if not isinstance(value,int):
            raise ValueError('age must be an integger')
        if value < 0 or value > 150:
            raise  ValueError('age must between 0 - 150')

s = Student()
s.name = 'sdgdsfg'
print(s.name)
try:
    s.score = 2042
except AttributeError as e:
    print('AttributrError:',e)

class CStudent(Student):
    pass
d = CStudent()
d.score = 23302
print(d.score)
bart = Student()
bart.__int__('lixu',156)

class Screen(object):

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self,value):
        self.width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('value must be an intagger')
        if value < 0 or value > 1000:
            raise  ValueError('value must between 0 - 1000')
        self.height = value

    @property
    def resolution(self):
        return self.resolution




#特殊函数

class Student(object):
    def __init__(self,name,age,gender,score):
        self.name = name;
        self.age = age
        self.gender = gender
        self.score = score
    def __str__(self):
        print('%s的年龄：%s,性别：%s,成绩：%s .'%(self.name,self.age,self.gender ,self.score))

s = Student('lixu',21,'male',10)

#如果一个类想要用for  in 循环，就必须实现一个__iter__()方法，
# 该方法返回一个可以迭代的对象,使用__next()__就可以得到下一个值
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self): #返回一个可以迭代的对象
        return self

    def __next__(self):
        self.a ,self.b = self.b ,self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        else:
            return self.a
for n in Fib():
    print(n)

#在类中实现__getitem()__方法就可以像list那样访问类了
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n ,int):#n是索引
            a,b = 0,1
            for x in range(n):
               a,b = b, a +  b
            return a
        if isinstance(n ,slice): #n是切片
            start = n.start
            stop  = n.stop
            if start is None:
                start = 0
            a,b = 0,1
            L = []
            for x in range(stop):
                if x> start:
                    L.append(a)
                a,b = b, a + b
            return L
f = Fib()
print(f[10])
print(f[0:4])

#枚举类型定义一个class类型，然后，每个常量都是class的
# 一个唯一实例。Python提供了Enum类来实现这个功能：
from enum import Enum

Month = Enum('item',('Jan','feb','Mar','Apr','may','jul','jue'))
for name in Month.__members__.items():
    print(name)

from enum import  Enum ,unique

@unique #unique装饰器可以检查保证没有重复的值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
for name ,member in Weekday.__members__.items():
    print(name,':',member.value)

#使用type()动态的创建类
#type()函数既可以返回一个对象的类型，又可以创建出新的类型，
#要创建一个class对象，type()函数依次传入3个参数：

#class的名称；
#继承的父类集合，注意Python支持多重继承，如果只有一个父类，
# 别忘了tuple的单元素写法；
#class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
h = type('hello',(object,),dict())

#元类（类的模板）
#metaclass是类的模板，必须从type类型派生
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
#有了ListMetaclass，我们在定义类的时候还要指示
# 使用ListMetaclass来定制类，传入关键字参数metaclass
class MyList(list,metaclass = ListMetaclass):
    pass
#当我们传入关键字参数metaclass时，魔术就生效了
# ，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()
# 来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，
# 返回修改后的定义
#__new__()方法接收到的参数依次是
#当前准备创建的类的对象；

#类的名字；

#类继承的父类集合；

#类的方法集合。
L = MyList()
L.add(2)
print(L)
'''
#ORM框架
#全称“Object Relational Mapping”，即对象-关系映射，就是把
# 关系数据库的一行映射为一个对象，也就是一个类对应一个表

class Filed(object):
    def __init__(self,name,colum_type):
        self.name = name
        self.colum_type = colum_type
    def __str__(self):
        return ('<%s:%s>'%(self.name,self.colum_type))


class StringFiled(Filed):
    def __init__(self,name):
        super(StringFiled,self).__init__(name,'varchar'(100))

class IntegarFiled(Filed):
    def __init__(self,name):
        super(IntegarFiled,self).__init__(name,'bigint')

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found Model : %s'% name)
        mapping = dict()
        for k ,v in attrs.item():
            if isinstance(v,Filed):
                print('Found mapping:%s==>%s' % (k,v))
                mapping[k] = v
        for k in mapping.keys():
            attrs.pop(k)
        attrs['__mapping__' ] = mapping #保存属性和映射关系
        attrs['name'] = name
        return type.__new__(cls,name,bases,attrs)
#基类Model
class Model(dict,metaclass = ModelMetaclass):

    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribution '%s" % key)

    def __set__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mapping__.item():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values(%s)' %(self.__table__,','.join(fields),','.join(params))
        print('sql:%s'% sql)
       # print('ARGS:%s' % self.__str__(args))

class User(Model):
    id = IntegarFiled('id')
    name = StringFiled('username')
    email = StringFiled('email')
    password = StringFiled('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()