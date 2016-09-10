
class Student(object):
    def __init__(self):
        self._score=80
        self._birthday=1993
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if value<60:
            print('我怎么可能考怎么低，强行修改一波')
            self._score=60
        elif value>95:
            print('考太高对大家都不公平，谦虚的修改一波')
            self._score=100
        else:
            self._score=value
    # 添加一个只读属性只是不用设置setter 修饰器就好了
    @property
    def age(self):
        return 2016-self._birthday

leo=Student()
print(leo.score)

leo.score=50
print(leo.score)

leo.score=97
print(leo.score)

print(leo.age)

# can't set attribute 设置只读属性会报错
# leo.age=22
# 其实我们还是可以对其进行设置 可 __xx 私有属性一样 声明的时候的 _xx 只是行为上面的规范，
leo._birthday=1996
print(leo.age)