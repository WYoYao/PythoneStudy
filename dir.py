
'''
# 判断基本类型的时候使用type 就可以直接判断出其类型
print(type(123))
print(type('name'))
print(type(None))
'''

'''
# 如果一个变量指向函数或者类，也可以用type()判断：
class Animal(object):
    def __init__(self,name):
        self.__name=name

person=Animal('leo')

print(type(person))
print(type(abs))
'''

'''
# 判断基本类型可以写成这个样子
print(type(123)==int)
print(type('str')==str)
print(type(True)==bool)
'''

#判断方法和类的时候比较了对象可以这样实现比较 需要引用types 这个模块

def fn():
    return 'HelloWorld'
class Animal(object):
    def __init__(self,name):
        self.__name=name
person=Animal('leo')
'''
# 这个时候abs 和 自己创建的fn  和匿名函数是不一样的类型，如何区分这几种函数，就需要types了
print(type(person))
print(type(abs))
print(type(fn))
print(type(lambda:'helloWorld'))
'''

'''
import types
# 各自对应自己的类 返回的都是True
print(type(person)==Animal)
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda:'helloWolrd')==types.LambdaType)
print(type((x*x for x in [1,2,3]))==types.GeneratorType)
# 对应不同于自己的类返回的都是False
print(type(fn)==types.BuiltinFunctionType)
print(type(abs)==types.FunctionType)
print(type(lambda:'helloWolrd')==types.MethodType)
# 但是自己的定义的方法的和匿名函数是都属于Function的
print(type(fn)==types.FunctionType)
print(type(abs)==types.FunctionType)
print(type(lambda:'helloWolrd')==types.FunctionType)
'''

# 创建了继承Animal的Dog 类 和 Husky 类
class Dog(Animal):
    pass
class Husky(Dog):
    pass

anii=Animal('aa')
dogg=Dog('aa')
huss=Husky('aa')

'''
# 使用Type 判断的时候只判断出了属于Husky 这个类，但是跟父类做对比的时候显示的不是
print(type(huss)==Husky)
print(type(huss)==Dog)
print(type(huss)==Animal)
'''

# 使用 isinstance 来判断类型
'''
    #首先判断自己的类型都是对的
print(isinstance(anii,(Animal)))
print(isinstance(dogg,(Dog)))
print(isinstance(huss,(Husky)))
'''

'''
    #使用isinstance 可以判断是否是其类的基类
print(isinstance(anii,(Animal)))
print(isinstance(dogg,(Animal)))
print(isinstance(huss,(Animal)))
'''

'''
    #同时也可以通过判断其是否是多个类的其中一个
print(isinstance(huss,(str,int,Husky)))
print(isinstance(123,(str,int,Husky)))
print(isinstance('123',(str,int,Husky)))
'''

'''
# 一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
# 是一个包含 字符串 的 list  （list 里面并不是方法的只是字符串）
print(dir('asd'))
'''


'''
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法

class Demo(object):
    def __len__(self):
        return 998
aa=Demo()
print(len(aa))
print(aa.__len__())
'''

#仅仅把属性和方法列出来是不够的，我们可以直接操作一个对象的状态
class Demo(object):
    def __init__(self):
        self.x=9
    def power(self):
        self.x=pow(self.x,2)
'''
    1.getattr() 获取对应的属性
    2.setattr() 设置对应的属性
    3.hasattr() 验证是否包含该属性
'''

de=Demo()
# 验证是否拥有该属性
print(hasattr(de,'x'))
print(hasattr(de,'y'))
# 设置其对应的属性
setattr(de,'y',19)
de.z=18
print(de.y)
print(de.z)
# 获取其对应的属性
print(getattr(de,'x'))
print(de.x)
# 在获取不包含的的属性的时候两种的方式都会报错 object has no attribute
# print(de.g)
# print(getattr(de,'g'))
# 可以传入一个默认值，如果属性不存在就返回默认的值   这个比直接点要强大
print(getattr(de,'g',404))



# 总结只有在不知道对象信息的时候我们才去使用上面的方法去检测使用 对象的构造和属性，如果知道的情况还是是用 ... 来执行的对应的属性
