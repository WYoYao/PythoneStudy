# collections是Python内建的一个集合模块，提供了许多有用的集合类。

'''
# 看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
# 定义一个class又小题大做了，这时，namedtuple就派上了用场：

from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p,p.x,p.y)

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
# 可以验证创建的Point对象是tuple的一种子类

print(isinstance(p,Point))
print(isinstance(p,tuple))
'''

# deque
'''
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
from collections import deque
q=deque(['a','b','c'])
q.appendleft('d')
q.append('f')
print(q)
q.pop()
q.popleft()
print(q)
'''



#defaultdict
'''
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd=defaultdict(lambda:'undefind')
dd['k1']='k1'
print(dd['k1'],dd['k2'])

#注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
#除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''

# OrderedDict
'''
#　使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
# 如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
d['z']=4
d['y']=5
d['z']=6

for k,v in d.items():
    print(k,v)
'''

# Counter
'''
# Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c=Counter()
for char in 'uwhfuhefhauwe':
    c[char]=c[char]+1
print(c)
'''

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431954588961d6b6f51000ca4279a3415ce14ed9d709000