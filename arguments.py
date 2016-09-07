def typeOf(arguments):
    if isinstance(arguments,(list)):
        print('当前类型为','list')
    elif isinstance(arguments,(tuple)):
        print('当前类型为','tuple')
    elif isinstance(arguments,(map)):
        print('当前类型为','map')
    elif isinstance(arguments,(set)):
        print('当前类型为','set')
    else:
        print(None)

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
        return 'list'
    elif isinstance(arguments,(tuple)):
        print('tuple')
        return 'tuple'
    elif isinstance(arguments,(map)):
        print('map')
        return 'map'
    elif isinstance(arguments,(set)):
        print('set')
        return 'set'
    else:
        print(None)
        return None


calc(['1','2','3'])
calc(('1','2','3'))
calc(set(['1','2','3']))
calc({
    '1':'leo',
    '2':'leo',
    '3':'leo'
})

# 上面只是使用的引用类型的参数，并不是使用可变参数实现的功能，想要使用的可变参数，我们只需要修改一个参数里面的内容
# 如果使用可变参数我们传参的时候可以不使用的上面这些方式调用,可以采用传多个参数的方式
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*arguments):
    if isinstance(arguments,(list)):
        print('*arguments这里','list')
    elif isinstance(arguments,(tuple)):
        print('*arguments这里','tuple')
    elif isinstance(arguments,(map)):
        print('*arguments这里','map')
    elif isinstance(arguments,(set)):
        print('*arguments这里','set')
    else:
        print(None)
    sum = 0
    print(arguments[0])
    for n in arguments:
        for k in n:
            print(k)


print(calc(['1','2','3']))
print(calc(('1','2','3')))
print(calc(set(['1','2','3'])))
print(calc({
    '1':'leo',
    '2':'leo',
    '3':'leo'
}))

# 如果已经有一个list或者tuple，要调用一个可变参数，可以使用如下的方法不用的一个一个去赋值写
def calc(*arguments):
    sum=0
    for n in arguments:
        sum=sum+n*n
    return sum

# 如果需要把一个list 的参数全部传入到一个可变参数的方法中可以是用 *转换list tuple 使其直接可以使用
print(calc(*[1,2,3,4,5]))
print(calc(*(1,2,3,4,5)))
# 使用* 转换后就相当于三个参数不是什么类型

# 关键参数可以允许你传入0个或任意个数的含参数名的参数，这些含参数名的参数会在函数的内部中转换成为一个dict(map)
def person(name,age,**other):
    print('name',name,'age',age,'other',other)
person('leo','23',like='girl',happy='play')

# 当本身就有一个dict 对象的时候，如果需要传给函数的关键字参数，需要怎么处理，可以使用** 进行转意
person('leo','23',**{
    'like':'girl',
    'happy':'play',
    'height':182,
    'color':'black',
})

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
# 和关键字参数不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)
person('leo','23',**{
    'city':'beijing',
    'job':'pg',
})

# 不能使用 多余的参数这样会报错 比如like
#**{
#    'city':'beijing',
#    'job':'pg',
#    'like':'play',
#}
#

# 如果定义一个函数中 已经用到了一个可变的参数，那么后面定义命名关键字参数的时候可以省略掉中间的*
def person(name,age,*lt,city,job):
    print(name,age,lt,city,job)
person('leo','23',*[1,2,3],**{
    'city':'beijin',
    'job':'pg',
})


# 同时命名关键字参数可可以使用默认值来表示
def person(name,age,*,city='beijing',job):
    print(name,age,city,job)

person('leo','23',**{
    'job':'pg',
})

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数

#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#但是请注意，参数定义的顺序必须是：
#1.必选参数、
#2.默认参数、
#3.可变参数、
#4.命名关键字参数和
#5.关键字参数。


# 任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数
def test(name,age):
    print(name,age)
test('leo','23')
test(*['leo','23'])
test(**{
    'name':'leo',
    'age':'23',
})