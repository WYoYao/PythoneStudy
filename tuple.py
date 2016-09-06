#tuple 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改.
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来.
t=(1,2)
print('%d %d %s' % (t[0],t[-1],t) )

# 定义一个空的tuple 可以写成
full=()
print(full)

#但是定义只有一个数的时候 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
one=(1)

print(one)

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
onet = (1,)
print(onet)

#虽然这个tuple 的第一位的空间是不可变的，但是如果其某一个元素如果是引用类型的时候，只要不修改其引用地址是可以的改变的
demo=(1,2,3,[])
# 'tuple' object does not support item assignment
# demo[0]=123

# 在不改变其引用的地址的情况下是可以改变的
demo[3].append(1)
print(demo)

# 'tuple' object does not support item assignment  改变其引用的地址的时候会报错
#demo[3]=[1,2,3]
