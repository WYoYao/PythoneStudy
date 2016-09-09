
'''
# 我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印
class Animal(object):
    def run(self):
        print('I am running')

t=Animal()
t.run()
# 继承最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog作为它的子类，什么事也没干，就自动拥有了run()方法：
class Dog(Animal):
    pass
    
l=Dog()
l.run()
'''

'''
# 当然，也可以对子类增加一些方法
class Animal(object):
    def run(self):
        print('I am running')

class Dog(Animal):
    def eat(self):
        print('I am eating')

t=Dog()
t.eat()
'''


'''
# 继承的第二个好处:当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
# 我们就获得了继承的另一个好处：多态。

class Animal(object):
    def run(self):
        print('I am running')
class Dog(Animal):
    def run(self):
        print('Dog is running')

d=Dog()
d.run()
'''


'''
# 什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
class Animal(object):
    def run(self):
        print('I am running')
class Dog(Animal):
    pass

a = list() # a是list类型的实例
b = Animal() # b是Animal类型的实例
c = Dog() # c是Dog类型的实例

print(isinstance(a,(list)))
print(isinstance(b,(Animal)))
print(isinstance(c,(Dog)))
# 因为Dog是从Animal继承下来的，当我们创建了一个Dog的实例c时，我们认为c的数据类型是Dog没错，但c同时也是Animal也没错，Dog本来就是Animal的一种！
print(isinstance(c,(Animal))) 
'''


