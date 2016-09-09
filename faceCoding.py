# 如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是把数据类型应该被视为一个对象

class Student(object):
    # 默认执行 __init__ 方法 每个方法中传入的第一个参数是当前实例
    def __init__(own,name,score):
        own.name=name
        own.score=score
    def print_score(own):
        print('这个学生的分数是%d' % own.score)
    def print_own(own):
        print(own)
    
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()

bart.print_own()


# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student

# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。