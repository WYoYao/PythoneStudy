# Python内置的sorted()函数就可以对list进行排序
print(sorted([36, 5, -12, 9, -21]))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
'''
    注意sorted 和 map filter 的不用
        第一个参数是一个Iterable
        第二个参数是一个命名关键子参数 key= 加一个方法
            key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list：
        返回值是一个list (感觉也是加ed 的原因)
'''
print(sorted([36, 5, -12, 9, -21],key=abs))

# 对于字符串的排序是根据ASCII的大小比较的
print(sorted('qweQWE'))

'''
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
'''
print(sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)],key=lambda t:t[1]))