# 创建一个类
class Student(object):
    pass

# 创建一个实例
person=Student()

# 我可以给实例添加需要的属性和方法
person.name='leo'
person.age=23
print(dir(person))

from types import MethodType
def say(self):
    print(self.name)
person.sayName=MethodType(say,person)

person.sayName()

#以上内容只能修改单个的实例，如果需要给所有的实例添加方法，需要在对象上添加对应的方法
son=Student()
Student.tell=lambda self:print('哈哈哈哈哈哈')
son.tell()
person.tell()


# 如果需要限制属性的实例的时候可以使用 __slots__
class test(object):
    __slots__=('name','age')    # 创建一个Tuple 来保存可以创建的属性名称

t=test()
t.name='leo'
t.age=23
print(t.name,t.age)
# 在对__slots__ 设置其他的属性的时候 系统会抛出错误
# t.like='play'       # object has no attribute
