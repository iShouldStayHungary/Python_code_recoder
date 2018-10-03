#-*- coding: utf-8 -*-
# datetime的学习
#注意到datetime是模块，datetime模块还包含一个datetime类，
# 通过from datetime import datetime导入的才是datetime这个类。

#如果仅导入import datetime，则必须引用全名datetime.datetime。

#datetime.now()返回当前日期和时间，其类型是datetime。
from datetime import datetime,timezone ,timedelta
'''
print(datetime.now())
#datetime和timestamp的转换
dt = datetime(2018,8,1,10,28)
print(dt)
print(dt.timestamp())
#timestamp是一个浮点数，小数位表示毫秒

#timestamp转化为datetime
t = 1533093380.0
print(datetime.fromtimestamp(t))
#转化为本地时间
print(datetime.utcfromtimestamp(t))
#转化为UTC标准时间（也就是UTC+0:00时区的时间）（零时区）

#用户输入的str转化为datetime,使用datetime.strptime()实现
a = datetime.strptime('2018-8-1 10:41:50','%Y-%m-%d %H:%M:%S')
#字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式
print(a)

#datetime转化为str使用strftime()实现
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))

#datetiem 的加减
#使用timedelta你可以很容易地算出前几天和后几天的时刻
now = datetime.now()
print(now)
#datetime.datetime(2018-08-04 09:30:12.791923)
now = now + timedelta(days = 2,hours = 1,minutes = 5)
print(now)

#时区转换
#可以通过utcnow()拿到当前的UTC时间，然后在转化为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)#每个datetime类型有一个时区属性tzinfo，
# 但是默认为None，拿到UTC时间，并强制设置时区为UTC+0:00:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
#使用astimezone()转化为北京区时
print(bj_dt)
'''
#练习
def to_timestamp(t,utc):
    dt = datetime.strptime(t,'%Y-%m-%d %H:%M:%S')
    print(dt)
    if utc[4] != '0':
        s = utc[4]
    else:
        s = utc[5]
    user_time = dt.astimezone(timezone(timedelta(hours = int(s))))
    print(s)
    user = user_time.timestamp()
    print(user)
    return user

if __name__ == '__main__':
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433117430.0, t1

    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433059830.0, t2

