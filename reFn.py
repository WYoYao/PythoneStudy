# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lady_sum(*arugments):
    def fn():
        sum=0
        for n in arugments:
            sum =sum+n
        return sum
    return fn
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f=lady_sum(1,2,3,4,5)
print(f())

# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

f1=lady_sum(1,2,3,4,5)
f2=lady_sum(1,2,3,4,5)

# 通过比较两个变量的引用地址 可以知道两个函数的引用地址是不一样的
print(f1==f2)

# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 因为循环的每个i 没有自己的独立作用域，和JS 一样如果需要这样的执行的时候可以创建一个方法将 i 传入
f1, f2, f3 = count()
print(f1(),f2(),f3())

def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            def g():
                return i*i
            return g
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())