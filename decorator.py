# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
# 函数对象有一个__name__属性，可以拿到函数的名字：
def now():
    print('2016/9/8')
fn=now
print(fn.__name__)

#现在，我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#log wrapper
def log(fn):
    def wrapper(*args, **kw):
        print('functionName %s()' % fn.__name__)
        fn(*args, **kw)
    return wrapper

# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处
'''
把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
'''
@log
def now():
    print('2015-3-25')
# now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
now()

print('现在函数的名称是',now.__name__)


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
# decorator

def log(text):
    def decorator(fn):
        def wrapper(*args, **kw):
            print('%s %s()' % (text,fn.__name__))
            return fn(*args, **kw)
        return wrapper
    return decorator

@log('这个是新加的参数')
def now():
    print('2015-3-25')

now()

# 剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

print('现在函数的名称是',now.__name__)

# 现在返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下
import functools

def log(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('functionName %s()' % fn.__name__)
        fn(*args, **kw)
    return wrapper

@log
def now():
    print('2016/9/8')

print('使用了functools.wraps，现在函数的名称是',now.__name__)

def log(text):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print('%s %s()' % (text,fn.__name__))
            return fn(*args, **kw)
        return wrapper
    return decorator

@log('新添加的日志')
def now():
    print('2016/9/8')
print('使用了functools.wraps，现在函数的名称是',now.__name__)

# decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。