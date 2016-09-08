# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 例如，在一个int中，删掉偶数，只保留奇数，可以这么写
l= list(filter(lambda x:x%2==1,map(lambda s:{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s],str(123456789))))
print(l)

# 把一个序列中的空字符串删掉
l=list(filter(lambda str:str and str.strip(),['A', '', 'B', None, 'C', '  ']))
print(l)

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。