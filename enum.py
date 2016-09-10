from enum import Enum,unique

'''
Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# value属性则是自动赋给成员的int常量，默认从1开始计数。
for name,member, in Month.__members__.items():
    print(name,member.value)
'''

# 需要更精确地控制枚举类型，可以从Enum派生出自定义类：
# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Sat.value)

# 访问这些枚举的方式
print(Weekday.Sun)
print(Weekday['Sun'])
print(Weekday(0))

print(Weekday.Sun.value)
print(Weekday['Sun'].value)
print(Weekday(0).value)