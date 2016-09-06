# 定义参数的时候可以是用默认参数 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
def enroll(name, gender, age=23, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

# 这样就可以在不需要修改后后面两个参数的时候只传前面两个参数
enroll('len','pg')

# 如果只需要传入第四个默认参数 而不使用第三个默认参数的时候可以使用 指明参数的形式使用
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。
enroll('leo','pg',city='wuhan')

# Python函数在定义的时候，默认参数的值就被计算出来了，如果使用引用类型的时候可能会出现一些BUG

def _appEnd(l=[]):
    l.append('end')
    return l

print(_appEnd())
print(_appEnd())
print(_appEnd())
print(_appEnd())
# 出现上面的bug 的原因就是因为在函数声明的时候l=[] 中的[] 是引用类型已经在堆内存中声明了，后面调用的这个引用的类型的时候，其实引用的都是这个堆内存的地址，可以使用的 None 在每个函数内部声明的对应的引用类型来解决这个问题

def _appEnd(l=None):
    if not l:
        #这个是后每次l没有传任何值的时候 都会重新在堆内存中声明一的对应空间来存放对应的[] 这样每次调用的时候就不会相互的影响
        l=[]
    l.append('end')
    return l

print(_appEnd())
print(_appEnd())
print(_appEnd())
print(_appEnd())
# 因此在给对应的函数设置默认值的时候 需要将其设置为值类型的量，如果需要设置引用类型的变量可以通过默认赋值为None 在函数内部中声明的方法


# 可变参数：还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 传入引用类型的参数，实现参数的可变 比如传入list tuple map set 这种类型的参数，然后在方法中进行调用
def calc(arguments):
    if isinstance(arguments,(list)):
        print('list')
    elif isinstance(arguments,(tuple)):
        print('tuple')
    elif isinstance(arguments,(map)):
        print('map')
    elif isinstance(arguments,(set)):
        print('set')
    else:
        print(None)
        sum = 0
    print(arguments[0])
    for n in arguments:
        print(n)
        sum = sum + int(n) * int(n)
    return sum

print(calc(['1','2','3']))
# print(calc(('1','2','3')))
print(calc(set(['1','2','3'])))
print(calc({
    '1':'leo',
    '2':'leo',
    '3':'leo'
}))

# 上面只是使用的引用类型的参数，并不是使用可变参数实现的功能，想要使用的可变参数，我们只需要修改一个参数里面的内容
# 如果使用可变参数我们传参的时候可以不使用的上面这些方式调用,可以采用传多个参数的方式
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*arguments):
    if isinstance(arguments,(list)):
        print('这里','list')
    elif isinstance(arguments,(tuple)):
        print('这里','tuple')
    elif isinstance(arguments,(map)):
        print('这里','map')
    elif isinstance(arguments,(set)):
        print('这里','set')
    else:
        print(None)
    sum = 0
    print(arguments[0])
    for n in arguments:
        print('这里',n)
        sum = sum + int(n) * int(n)
    return sum


print(calc(['1','2','3']))
print(calc(('1','2','3')))
print(calc(set(['1','2','3'])))
print(calc({
    '1':'leo',
    '2':'leo',
    '3':'leo'
}))

# 如果已经有一个list或者tuple，要调用一个可变参数，可以使用如下的方法不用的一个一个去赋值写
