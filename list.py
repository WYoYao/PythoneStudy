#创建一个List
test=['red','green','yellow'];

#通过下标访问         同时也不能访问过界
print('第一个元素是%s' % test[0])
print('最后一个元素是%s' % test[-1])

#获取其对应的长度
print('这个list的长度是%d' % len(test))

#通过append 添加一个元素到整个list 的最后面
test.append('blue')
print(test)

# 通过insert 指定一个位置，并且向制定的位置插入一个元素，其位置后面的元素依次往后排。
test.insert(0,'block')
print(test)
# 必须要指定两个参数，如果只指定一个参数的时候或报错
# test.insert('block')

#pop 删除一个list 后面的内容
test.pop()
print(test)
#如果要删除一个制定的位置的元素可以给pop 传对应的下标  同时pop 也能够传入-1 从list 后面进行删除
test.pop(0)
test.pop(-1)
print(test)

# 同时一个list 的类型也可以不是相同类型的  同事list的一个索引也可以是list
oList=[123,'hello',True,[1,2,3,4]]
print(oList)

