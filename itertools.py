

# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数


# 我们看看itertools提供的几个“无限”迭代器：


# from itertools import count,cycle,repeat

'''
# 每次递增加1
natuals =count(1)

for k in natuals:
    print(k)
'''

'''
# 每次循环打印一个字符
cs=cycle('abc')
for k in cs:
    print(k)
'''

'''
# 可以通过repeat来进行循环的次数限定
re=repeat('A',3)
for k in re:
    print(k)
'''

#无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
'''
import itertools
natuals=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,natuals)
print(list(ns))
'''

'''
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
from itertools import chain
for k in chain('abc','def'):
    print(k)
'''

'''
# groupby()把迭代器中相邻的重复元素挑出来放在一起
from itertools import groupby
for key,group in groupby('AAABBBCCAAA'):
    print(key,list(group))
'''

#实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
from itertools import groupby
for k,obj in groupby('AaaBBbcCAAa',lambda x:x.upper()):
    print(k,list(obj))


