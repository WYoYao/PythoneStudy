# 很多时候，数据读写不一定是文件，也可以在内存中读写。

# StringIO顾名思义就是在内存中读写str。

from io import StringIO

'''
f=StringIO()
# 通过write 写入文件
for i in range(1,11):
    f.write('hello World%s\n' % i)
# 通过getvalue 获取写入的所有数据
# print(f.getvalue())

# 这个后面写入的数据调用readline 获取不到数据
print(f.readline())
'''

# 只有在创建的时候就存在的数据才能被读取
f=StringIO('helloWolrd1\nhelloWolrd2\nhelloWolrd3\nhelloWolrd4\nhelloWolrd5\n')
# 后面写入的数据是不能通过readline  和 readlines read 读取出来的
# 后面的写入的内容会前面写入的内容替换掉
f.write('helloWolrd6\nhelloWolrd7\n')
# print(f.readline())
# print([x for x in f.readlines()])
print(f.read())




