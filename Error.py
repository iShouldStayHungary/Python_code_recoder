#-*- coding: utf-8 -*-
#logging 模块可以非常容易的记录错误信息
import logging
logging.basicConfig(level= logging.INFO)
#它允许你指定记录信息的级别，有debug，info，warning，error
# 等几个级别，当我们指定level=INFO时，logging.debug就不起作用了
# 。同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息
def foo(s):
    n = int(s)
    #assert n != 0, 'n is zero!'
    logging.info('n = %d' % n)
#断言（assert）类似于print打印出错误信息
    return 10 /int(s)

def bar(s):
    return foo(s)* 3

def exceute():
    if __name__ == '__main__':
        try:
            bar('0')
        except Exception as e:
            logging.exception(e)

exceute()

