

'''
    # 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板
    # 而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
'''


# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

'''
class Student(object):
    pass
bart = Student()
print(bart)
#          类名     继承的父类   内存地址
#<__main__.Student object at 0x0000000002CD4550>
'''



# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去

'''

class Student(object):
    # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
    #注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    def __init__(self,name,like):
        self.name=name
        self.like=like

person=Student('leo','play')
print(person,person.name,person.like)

'''


# 既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法

'''
class Student(object):
    def __init__(self,name,like):
        self.name=name
        self.like=like
    #要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递
    def print_like(self):
        print('个人的爱好是%s' % self.like)

person=Student('leo','play')

person.print_like()
'''



'''

class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_level(self):
        if self.score>= 90:
            print('A')
        elif self.score>=60:
            print('B')
        elif self.score>=30:
            print('C')
        else:
            print('D')


leo=Student('leo',85)
leo.print_level()

'''