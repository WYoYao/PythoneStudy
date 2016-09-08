def fn(x):
    return x * x

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

'''
    传入的fn 是一个函数，
    传入的[] 是一个Iterable 对象
    返回的是Iterator
'''

i = map(fn,[1,2,3,4])

# print(next(i))

# 如果想直接返回的遍历的数组可以使用list
i=list(map(fn,[1,2,3,4]))
print(i)

'''
    redux 接受两个参数：
        1. 一个必须接受两个参数的函数 第一次执行会把Iterable 的第一个值和第二个值传入函数进行运算，以后每次执行会把上一次执行的函数结果与后面一个数一起执行该函数的运算
        2.一个Iterable 对象

    运行效果：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''

from functools import reduce
def fn(x,y):
    return x+y
print(reduce(fn,[1,2,3,4,5]))

# 如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x,y):
    return x * 10 + y
print(reduce(fn,[1,2,3,4,5]))

# 将一个字符串转换成对应的数字对象
def strInt(str):
    def chatInt(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    def fn(x,y):
        return x * 10 + y
    return reduce(fn,map(chatInt,str))

print(strInt('987654321'))

# 用lambda函数进一步简化成
def lam(str):
    return reduce(lambda x,y:x * 10 + y,map(lambda s: {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s],str))

print(lam('987654321'))
