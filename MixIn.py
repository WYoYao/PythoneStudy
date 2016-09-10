# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
# 在设计类的继承关系时，通常，主线都是单一继承下来的.但是，如果需要“混入”额外的功能，通过多重继承就可以实现.种设计通常称之为MixIn。
class Animal(object):
    def say(self):
        print('我是Animal')
    def play(self):
        print('我啥都不会玩')

class Runnable(object):
    def run(self):
        print('Running...')
    def play(self):
        print('你来追我啊')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Person(Animal,Runnable):
    pass
# 同时继承了Animal 的say 和Runnable run
leo=Person()
leo.say()
leo.run()
# 如果多个继承类的属性中有冲突，这样会优先选择前面的类的方法和属性
leo.play()