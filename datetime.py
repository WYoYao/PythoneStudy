

# datetime是Python处理日期和时间的标准库。
'''
# 获取当前日期和时间
# 我们先看如何获取当前日期和时间

from datetime import datetime
now =datetime.now()
print(datetime.now())
print(type(now))

# 获取指定日期和时间
# 要指定某个日期和时间，我们直接用参数构造一个datetime
dt=datetime(2016,9,12,21,12)
print(dt)
'''

# datetime转换为timestamp
'''
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。

# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法

from datetime import datetime
# 转换成为时间戳   注意python的时间戳是以秒为单位，分数的后面代表的是对应的毫秒
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
print(datetime.now().timestamp())

'''

# timestamp转换为datetime

# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
# from datetime import datetime
# print(datetime.fromtimestamp(1473686195.727677))
# 注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
# 本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间

# timestamp也可以直接被转换到UTC标准时区的时间
# from datetime import datetime
# print(datetime.fromtimestamp(1473686195.727677))
# print(datetime.utcfromtimestamp(1473686195.727677))


#str转换为datetime
# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
# from datetime import datetime
# print(datetime.strptime('2016-9-12 21:27:00','%Y-%m-%d %H:%M:%S'))
# print(datetime.strptime('2016-9-12 21:27:00','%Y-%m-%d %H:%M:%S').timestamp())

# datetime 转换成为 str
# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串
# from datetime import datetime
# print(datetime.now().strftime('%Y-%m-%d'))

# datetime加减
# from datetime import datetime,timedelta
# now=datetime.now()
# print(now)
# now=now-timedelta(hours=10)
# print(now)
# now=now + timedelta(hours=10)
# print(now)
# now=now - timedelta(days=1)
# print(now)
# now=now + timedelta(days=2, hours=12)
# print(now)
