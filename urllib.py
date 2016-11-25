

#urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：

# import urllib
# print(urllib.)

from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))


'''
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data=f.read()
    print('Status',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k, v))
    print('data',data.decode('utf-8'))
'''