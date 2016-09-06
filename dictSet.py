#dict Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

#假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
#第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

maps={
    'leo':91,
    'john':89,
    'list':[1,2,3,4],
    'tuple':(1,2,3,4),
    'map':{
        'one':1,
        'two':2,
    }
}
print(maps)
print(maps['leo'])

#可以通过 for in 循环 map 对象的 key
for key in maps:
    print(maps[key])

# 如果一个key 不存在的时候调用会报错，调用之前可以使用 in 判断是否属于
print('leo' in maps)
print('other' in maps)

#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(maps.get('leo','我是默认的值'))
print(maps.get('other'))
print(maps.get('other','我是默认的值'))

#如果要删除一个对应的key 也是可以使用pop   需要传入对应的key值
maps.pop('john')
print(maps)
#pop expected at least 1 arguments, got 0 如果不传值会报错
# maps.pop()
# 如果传入的值不存在也会报错
# maps.pop('other')

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#要创建一个set，需要提供一个list作为输入集合：
s=set(['yello','green','red','yello'])
print(s)

#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素
#key 值是不能够是引用类型的值 但是可以使用tuple (list map 都不可以使用) 只有不可变对象才可以使用
# s.add({'name':'leo'})
# s.add(['leo'])
s.add(('name','leo'))
print(s)

