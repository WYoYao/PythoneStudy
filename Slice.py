L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 和ES5 一样 python 的list 和 Tuple 也支持Slice 的操作并且有更高级的用法

# 取前三个参数    同时也是包前不包后
print(L[0:3])

# 如果Slice 的第一个参数为 0 的时候可以省略
print(L[:3])

# 同时也支持通过负数取值 如果只制定一个参数的时候只会获取一个单个的值 但是返回的不会是一个list
print(L[0])
print(L[-1])
T=('one','two','three')
print(T[0])
print(T[-1])

# 既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[-2:-1])

# 像开始的 0 一样 倒数的-1 同时也是可以省略的
ran=list(range(100))
print(ran[:10])
print(ran[-10:])

# 同时也可以每5个取一个
print(ran[::5])

# Tuple 也支持切片操作 如果只传入一个参数的时候会返回当前下标的值，但是如果传入两个以上值进行切片的时候会返回一个Tuple
# String 也可以看成一个list,每个元素就是其的一个