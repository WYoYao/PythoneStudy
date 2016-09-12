
'''
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
'''

# Python提供了pickle模块来实现序列化。

import pickle
d=dict(name='leo',age='23')
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
print(pickle.dumps(d))
# 同时也可以使用 pickle.dump直接把对象序列化后写入一个文件，
with open('pickDemo.text','wb') as f:
    pickle.dump(d,f)

# 同时可以使用
print(pickle. loads(b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01X\x02\x00\x00\x0023q\x02X\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00leoq\x04u.'))

# 同时也可以通过pickle.load 从一个文件中直接读取出来二进制的文件流，然后放到内存中
with open('pickDemo.text','rb') as f:
    o=pickle.load(f)
    print(o['name'])