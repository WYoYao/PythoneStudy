# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

# 在Python中，迭代是通过for ... in来完成的

# 只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
for key in [1,2,3]:
    print(key)

for key in {'name':'leo','age':23,}:
    print(key)

# dict 对象会迭代对象的key 如果想直接迭代出dict 的value 的时候可以使用的 dect.values() 取出其值的集合
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# String 也可以迭代 因为其类似每一个字符的组成的list
person={
    'name':'leo',
    'age':23,
    'like':'play',
}

print(person.keys(),person.values(),person.items())
print(isinstance(person.keys(),(list,tuple)))

# for in 只要作用于一个可迭代的对象，for 循环就可以正常的使用，而不用关系这个数据究竟是list，还是其他类型的数据
# 判断一个对象是可迭代对象，方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print(isinstance([1,2,3,4],(Iterable)))
print(isinstance({
    'name':'leo',
},(Iterable)))
print(isinstance('String',(Iterable)))

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
l=[1,2,3,4,5]
for i,value in enumerate(l):
    print(i,value)

# for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：相当于循环遍历出来的 对象然后再解构赋值
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)

