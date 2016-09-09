# int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换

'''
偏函数： 返回一个新的参数，为其参数函数，默认制定对应的值
简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
'''
import functools
int2=functools.partial(int,base=2)
print(int2('111'))

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
int2 = functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base
kw = { 'base': 2 }
int('10010', **kw)

max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是
print(max2(5, 6, 7))
# 相当于：
args = (10, 5, 6, 7)
print(max(*args))
