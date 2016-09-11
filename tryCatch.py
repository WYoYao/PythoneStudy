
'''
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
try:
    print('try...')
    r=10/0
    print('r value is %s' % r)
# 如果没有错误发生，except语句块不会被执行
# 这个地方用的是 ZeroDivisionError 类型的错误会被这里捕捉，错误类型有很多，应该由不同的错误类型来捕捉
except ZeroDivisionError as e:
    print('except:',e)
except ValueError as e:
    print('ValueError:', e)
# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
else:
    print('no error!')
finally:
    print('finally')
print('end')
'''


'''
# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。
def fn(value):
    return int(value)

try:
    print(fn('asd'))
    # 因为所有的错误类都继承 BaseException 所以在使用BaseException 会捕获所有的错误类型，后面的都捕获不到
except BaseException as e:
    print('BaseException')
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
finally:
    print('执行完毕')
'''


# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用

def fn(value):
    return int(value)

def main():
    return fn('leo')

'''
# 可以在最外层的地方调用 try catch，或者可以处理错误的地方调用对应的错误逻辑的处理
# 也就是说可以用任何的地方都使用try catch 只需要在能处理的错误路基的地方调用就好了
try:
    main()
except BaseException as e:
    print('BaseException')
finally:
    print('finally')
'''

# 如果可能发生错误的地方不做任何的try catch 的处理的情况，可以打印出错误，但是程序并不能继续执行
# main()
# print('haha')

'''
# Python内置的logging模块可以非常容易地记录错误信息
import logging

try:
    main()
except BaseException as e:
    # 打印出了错误，同事也继续执行的后面的操作
    logging.exception(e)

print('End')
'''

'''
# 抛出错误
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
class LeoError(ValueError):
    pass

try:
    raise LeoError('这个是现在抛出的错误')
# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。
except LeoError as e:
    print(e)
finally:
    print('finally')
print('end')
'''


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？

# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型

# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。