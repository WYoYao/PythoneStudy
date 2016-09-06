# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def _myAbs(num):
    if num>0:
        return num
    else:
        return -num

print(_myAbs(100))
print(_myAbs(-100))

# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。

# return None可以简写为return。 空函数如果想定义一个什么事也不做的空函数，可以用pass语句：
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

def void():
    pass

print(void())

# 同时书写方法的时候也需要对其参数进行检测 可以使用 isinstance 来检验参数的类型
def _myAbs(num):
    # 每个方法定义的时候需要 检查其参数的类型
    if not isinstance(num,(int,float)):
         raise TypeError('bad operand type')
    if num>0:
        return num
    else:
        return -num

print(_myAbs(100))
print(_myAbs(-100))
# print(_myAbs('strtest'))


# 表面可以返回多个值，但是实际情况下 只能返回一个值tuple 返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple
# 1返回一个tuple 2 按位置赋值() 后面进行的相当于解构赋值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 解构返回的tuple
x, y = move(100, 100, 60, math.pi / 6)
# 一个数解构的时候直接得到的tuple
a = move(100, 100, 60, math.pi / 6)

print(x,y)

print(a)

(c,d)=a
print(c,d)

print(isinstance(move(100, 100, 60, math.pi / 6),(tuple)))
print(isinstance(a,(tuple)))