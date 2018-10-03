#-*- coding:utf-8 -*-
#日期：2018.7.31
#正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符
# 串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。
import re
#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
print(re.match(r'^\d{3}\s+\d{3,8}$','010 123456'))
print('a b   c'.split(' '))
#无法识别连续的空格，用正则表达式试试
#用正则表达式切分字符串
print(re.split(r'[\s\,\;\.]+','a ,b   .  cd ;e'))
#除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。
# 用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$','101-12344')
print(m)
print(m.group())
print(m.group(0))
#记住group（）和group（0）永远提取原始的字符串
#groups()提取所有的字符串分组
print(m.group(1))
#\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
print(re.match(r'^(\d+)(0*)$','1230323000').groups())
print(re.match(r'^(\d+?)(0*)$','1230323000').groups())

#如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式
re_zhengzebiaodashi = re.compile(r'(\d{3})-(\d{3,8})$') #预编译
print(re_zhengzebiaodashi.match('101-214344').groups())
#编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，
# 所以调用对应的方法时不用给出正则字符串。

#验证一个Email邮箱地址的正则表达式
def valid_email(st):
    m = re.match(r'([0-9a-zA-Z\s+\<\>]+)\s+|([0-9a-zA-Z\.]+)\@([0-9a-z\.]+)',st)
    if m:
        print(m.groups())
        if m.group(1) :
            print('名称：%s' % m.group(1))
        else:
            print('名称：%s' % m.group(2))
        print('域名：%s'% m.group(3))
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    valid_email('bill.gates@microsoft.com ')