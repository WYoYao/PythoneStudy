import config


# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
'''
    1.正常的函数和变量名是公开的（public）
    2.类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等
    3.类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量

    ### private函数和变量“不应该”被直接引用，而不是“不能”被直接引用

'''

# 通过导入的模块还是可以引用的，私有变量只是相当于开发人员之间，默认的协议
print(config.publckName)
print(config._privateName)
print(config.__privateWord)