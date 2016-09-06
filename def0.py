#求绝对值的函数abs，只有一个参数。
print(abs(100))

print(abs(-20))

print(abs(12.34))
#max函数max()可以接收任意多个参数，并返回最大的那个
print(max(1, 2))

print(max(2, 3, 1, -5))

# 常用类型转换函数
# int 小数转的时候只能向下取整，包含字符的时候会转换失败
print(int(12.99))
# float 将int 转换为一位小数的float  将字符串转换成为对应的 float值
print(float('12.34'))
# str 将一个参数转换成为对应的字符串
print(str(12.32))
print(str(True))

# 同时函数也是一个引用对象，也可以通过函数名引用赋值
a=abs
print(a(-123))
