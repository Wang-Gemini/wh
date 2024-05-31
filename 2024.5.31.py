#     30号
#dete类
from datetime import date

a = date.today()
print(a)
print(a.year)
print(a.month)
print(a.day)
a = date(2017,3,1)
b = date(2017,3,15)
print(a.__eq__(b))
print(a.__ge__(b))
print(a.__gt__(b))
print(a.__le__(b))
print(a.__lt__(b))
print(a.__ne__(b))
print(a.__sub__(b))
print(a.__rsub__(b))

print(a.__format__('%Y-%m-%d'))
print(a.__format__('%Y/%m/%d'))
print(a.__format__('%y/%m/%d'))
print(a.__format__('%D'))
print(a.__format__('%d'))

from datetime import  time
a = time(12, 20, 30,899)
print(a.__format__('%H:%M:%S'))

from  datetime import *
d = datetime(2012,12,12, 23, 59, 59)
print(d)
#昨天
d1 = d + timedelta(days=-1)
print(d1)
#明天
d2 = d + timedelta(days=1)
print(d2)
#上一个小时
d3 = d + timedelta(hours=-1)
print(d3)
#下一个小时
d4 = d + timedelta(hours=1)
print(d4)
#上一秒
d5 = d + timedelta(seconds=-1)
print(d5)
#下一秒
d6 = d + timedelta(seconds=1)
print(d6)

#time模块

a = time.time()
#计算当前时间点与a之间的时间间隔，以秒为单位
for x in range(100000):
    pass
b = time.time() -a
print(b)
#第一次调用时，返回的是程序运行的实际时间
print(time.perf_counter())
#第二次调用时，返回的是自第一次调用后，到这次调用的时间间隔
print(time.perf_counter())
#返回的是距离上一次调用的时间间隔
print(time.perf_counter())
#5
print("start:s"%time.ctime())
time.sleep(5)
print("End:%s"%time.ctime())

#6
print(time.time)
print(time.ctime(time.time()))

#将时间元素组转化为format,年月日格式
a = time.strftime("%Y-%m-%d",time.gmtime())
print(a)

b = time.strftime("%Y-%m-%d %x")
print(b)

#返回当地的日期和时间
c = time.strftime("%x %X")
print(c)

#calendar模块
import calendar
thismonth=calendar.month(2021,11,0)
print(thismonth)

#isleap()方法是判断年份为润年还是平年
#2018是平年，所以为false
print(calendar.isleap(2018))
#2008是润年，所以为True
print(calendar.isleap(2008))