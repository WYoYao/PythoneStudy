# type()

# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

'''
class Hello(object):
    def hello(self,name='world'):
        print('Hello %s' % name)

h = Hello()
h.hello()
print(type(Hello))

#　type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type
#　h 是 Hello 的实例，Hello 是h 的类
#  Hello 是type 的实例， type 是Hello 的类，那么应该也能通过type来创建 一个新的类

def demoFn(self,name='world'):
    print('demohello %s' % name)

DemoHello=type('DemoHello',(object,),{
    'hello':lambda self,name='world':print('demohello %s' % name)
})

d = DemoHello()
d.hello()
print(type(DemoHello))

# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''

# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类

'''
metaclass

除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

metaclass，直译为元类，简单的解释就是：

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
'''

# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
class ListMetaclass(type):
    '''
        1.__new__()方法接收到的参数依次是：

        2.当前准备创建的类的对象；

        3.类的名字；

        4.类继承的父类集合；

        5.类的方法集合
    '''
    def __new__(cla,name,base,attrs):
        attrs['add']=lambda self,x:self.append(x)
        return type.__new__(cla,name,base,attrs)
# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass):
    pass

l=MyList()
l.add(1)
l.add(2)
l.add(3)
print(l)

当我们传入关键字参数metaclass时它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建.

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000