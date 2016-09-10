# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

# 除此之外，Python的class中还有许多这样有特殊用途的函数


# __str__
'''
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'name values is %s ' % self.name
    # 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    __repr__ = __str__


# __str__    转换成 str 类型的时候，返回的参数

leo=Student('leo')
print(leo)
# <__main__.Student object at 0x0000000002CD0518>

# 这个时候如果想打印出更加好理解的内容可以设置其的 __str__
print(str(leo))
'''


'''
# __iter__
class Demo(object):
    def __init__(self):
        self.MaxNumber=10
    # 定义完 __iter__ 之后其的 Iterable 为True,但是不能代表就能使用 for in 循环了，还需呀实现__next__
    def __iter__(self):
        return self
    # 真正的实现额 __next__ 之后循环才能在这里开始
    def __next__(self):
        self.MaxNumber-=1
        if self.MaxNumber<0:
            raise StopIteration();
        return 'next' + str(self.MaxNumber)

leo=Demo()

from Iterator import Iterable
print('检查',isinstance(leo,Iterable))

for k in leo:
    print(k)

'''


'''
# __getitem__
# __iter__ 和 __next__ 实现了 fon in 的循环，但是如果其通过下标取值的时候还是出出问题，可以使用__getitem__ 来取对应的值

class Demo(object):
    def __init__(self):
        self.arr=[1,2,3,4,5]
        self.index=-1
    def __getitem__(self,n):
        return [x for x in self.arr][n]

    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index+1>len(self.arr):
            raise StopIteration();
        return self.arr[self.index]

leo=Demo()

print([x for x in leo])
print(leo[0],leo[1],leo[2],leo[3],leo[4])
'''


'''
# __getattr__
# 正常的情况如果访问一个不存的属性会报错，但是如果设置了__getattr__ 属性就可以避免这个问题
# 如果有包含的属性有优先调用其属性，如果没有其属性会通过__getattr__ 来调用其属性
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

class Demo(object):
    def __getattr__(self,value):
        if value=='age' or value=='name':
            return '现在还没有录入这些个信息'

leo=Demo()
# 返回了默认的参数
print(leo.age)
print(leo.name)
# 返回了None
print(leo.like)
print(leo.haha)


for k in range(10):
    print(k)
'''


'''
# __call__ 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
# 同时也可以把实例当作方法一直执行，设置其 __call__ 属性就可以实现这个效果

class Student(object):
    def __init__(self,name):
        self.name=name
    def __call__(self,value):
        print('%s is %s' % (self.name,value))

leo=Student('leo')
leo('study')

# 如何判断一个对象是否可以当作方法一样被调用呢可以是用 callable

print(callable(abs))
print(callable(leo))

print(callable(123))

'''