

# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符
'''
f=open('./index.txt','r')
print(f)
# 使用read 方法可以一次性读取全部的内容，Python把内容读到内存，用一个str对象表示
print(f.read())
# 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
f.close()
'''

# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
'''
try:
    f=open('./index.txt','r')
    print(f.read())
finally:
    if f:
        f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

with open('./index.txt','r') as f:
    print(f.read())
# I/O operation on closed file. 已经关闭了
print(f.read())
'''


# read()
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
# with open('./index.txt','r') as f:
    # print('5',f.read(5))            # 读取5个bytes的内容

    # print('readline',f.readline().strip()) # 读取一行的内容
    # print('readline',f.readline().strip()) # 读取一行的内容
    # print('readline',f.readline().strip()) # 读取一行的内容

    # print('readline',f.readline(1)) # 读取一段的内容
    # print('readline',f.readline(2)) # 读取一段的内容
    # print('readline',f.readline(3)) # 读取一段的内容

    # for line in f.readlines():          # 返回一个List
    #     print(line.strip())

    # print('read',f.read())          # 读取全部所有的内容


# 如果需要打开一个二进制文件的内容，可以使用rb 提示符
'''
with open('./img.png','rb') as f:
    print(f.read())
'''

'''
# 指定编码格式        需要制定encoding 关键字参数，需要通过制定不同的编码方式来指定不同的编码的文件
with open('./index.txt','r',encoding='gbk') as f:
    print(f.read().strip())
'''

'''
# 在遇到一个编码不规范的文件，可能会遇到UnicodeDecodeError，因为文件中可能夹杂了一些非法编码的字符，遇到这种情况
# open 函数还接受了errors参数，表示获取文件的时候出现的错误，最简单的方式是忽略
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
'''


# 写入文件 读和写是一样的唯一的区别是调用 open 函数的时候，标识符的传入的值是不同的,
# 传入标识符的 'w' 和 'wb' 的时候表示的写入文本 或 写入二进制文件
# 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
with open('./rindex.txt','w') as f:
    f.write('hello1\n')
    f.write('hello2\n')
    f.write('hello3\n')
    f.write('hello4\n')