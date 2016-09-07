#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x * x for x in range(1,11)])
# 相当于
l=[]
for x in range(1,11):
    l.append(x * x)
print(l)


#[4, 16, 36, 64, 100]
print([x * x for x in range(1, 11) if x % 2 == 0])
# 相当于
l=[]
for x in range(1,11):
    if x % 2 ==0:
        l.append(x * x)
print(l)

# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print([m + n for m in 'ABC' for n in 'XYZ'])
# 相当于
l=[]
for m in 'ABC':
    for n in 'XYZ':
        l.append(m+n)
print(l)

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
print([d for d in os.listdir('.')])

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([key+"="+value for key,value in d.items()])

# 相当于
l=[]
for item in d.items():
    key,value=item
    l.append(key+"="+value)
print(l)


# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
L = ['Hello', 'World', 18, 'Apple', None]

print([ s for s in L isinstance(s,str)?s.lower():s])