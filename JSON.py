'''
如果我们要在不同的编程语言之间传递对象，
就必须把对象序列化为标准格式，
比如XML，但更好的方法是序列化为JSON，
因为JSON表示出来就是一个字符串，
可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。J
SON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

'''
'''
JSON类型	    Python类型
{}	            dict
[]	            list
"string"	    str
1234.56	        int或float
true/false	    True/False
null	        None
'''

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON
import json
# 可以通过dumps 转换将 python 类型转换成为JSON类型
# print(json.dumps({'name':'leo'}))

# 同时也可以通过json.dump 直接将一个python 对象转换成为一个JSON类型，并且将其写入一个file-like Object
# with open('jsonDemo.txt','w') as f:
#     json.dump({'name':'leo'},f)

# 当我们需要将JSON 类型转换成为python 对象的时候可以使用loads
# print(json.loads('{"name": "leo"}')['name'])

# 同时也可以使用json.load 从一个file-like Object中读取字符串并反序列化
# with open('jsonDemo.txt','r') as f:
#     print(json.load(f)['name'])

# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。
# 所有读取文件的标识符应该是 r 而不是 rb


# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
import json
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
s=Student('leo','23')
print(s)
#print(json.dumps(s))
# <__main__.Student object at 0x0000000002CD06A0> is not JSON serializable 这样执行的得到一个错误
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象 把一个实例对象转换成为一个JSON对象的时候需要将其先转换的成为对应的dict对象，然后再进行转换、
# 可以使用因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s,default=lambda obj:obj.__dict__))