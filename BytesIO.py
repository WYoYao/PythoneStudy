

# BytesIO StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

from io import BytesIO

'''
f=BytesIO()
# 这个时候写入的不是str 是经过utf-8 编码的 bytes
f.write('中文'.encode('utf-8'))
print(f.getvalue())
#print(f.read())
'''

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')\
# 读取了内容后使用utf-8 进行编码
print(str(f.read(),'utf-8'))

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431925324119bac1bc7979664b4fa9843c0e5fcdcf1e000