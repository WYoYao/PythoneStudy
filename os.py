
import os
# 打印对应的系统
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# print(os.name)

# 环境变量
# 打印所有的环境变量
# print(os.environ)

# 如果要获取其中某一个环境变量，可以这样使用
# print(os.environ.get('path'))

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径
# print(os.path.abspath('.'))

# 如果要在某一个目录下创建一个新的目录，首先把目录的完整路径表示出来
# print(os.path.join(os.path.abspath('.'),'testdir'))

# 然后使用mkdir 创建对应的文件目录
# os.mkdir(os.path.join(os.path.abspath('.'),'testdir'))

# 然后我们可以删除需要删除这个创建的文件夹
# os.rmdir(os.path.join(os.path.abspath('.'),'testdir'))

# 使用路径拼接的时候不要使用字符串直接拼接，因为操作系统不同的时候拼接的内容不一样
# print(os.path.join('g:\pythonDemo','os.py'))

# 拆分的时候也需要注意，也不能直接通过字符串进行截取
# ('g:\\pythonDemo', 'os.py') 可以得到两部分一部分是对应的最后一级目录，第二部分内容是文件的名称及后缀
# print(os.path.split('g:\pythonDemo\os.py'))
# ('g:\\pythonDemo\\os', '.py') 可以直接获取文件的后缀名
# print(os.path.splitext('g:\pythonDemo\os.py'))

#  创建一个文件的时候使用open 就好了
# with open(os.path.join(os.path.abspath('.'),'testtest.txt'),'w') as f:
#     pass

# 修改一个文件
# os.rename('testtest.txt','testindex.txt')

# 删除一个文件
# os.remove('testindex.txt')

# 获取当前文件的所有文件
#print(os.listdir('.'))

# 获取所有的文件夹
# print([x for x in os.listdir('.') if os.path.isdir(x)])


# 获取所有的 .py 文件
# print([ x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py' ])
