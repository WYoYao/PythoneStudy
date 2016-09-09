# pip install Pillow

from PIL import Image
im=Image.open('test.png')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

#当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：
# import mymodule
'''
No module named 'mymodule'
'''


# Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
import sys
# for k in sys.path:
#     print(k)


'''
    如果我们要添加自己的搜索目录，有两种方法：
        1.是直接修改sys.path，添加要搜索的目录：
        这种方法是在运行时修改，运行结束后失效。
'''
# 可用通过相对地址添加路径
# sys.path.append('../scope')
# 可以通过当前目录的物理路径来获取对应的模块
# sys.path.append('h:\PythoneStudy\scope')
# 可以通过绝对路径获取对应的模块


# sys.path.append('/PythoneStudy/scope')
# for k in sys.path:
#     print(k)
# import config
# print(config)


'''
    2. 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。
'''


