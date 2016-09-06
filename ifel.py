age=23
if age<16:
    print('00后')
# elif 是if else 的缩写
elif age<26:
    print('90后')
# 但是不else if 是不可以使用的
# else if age<36:
    # print('80后')
else:
    print('你好老')

# 同时还可自动的转换使用 只要 Number 不为0 String 不为"" Boolean 不为False List 不为[] Tuple 不为() if判断中都可以转换为True
if -1 and 'str' and True and (1,) and [0]:
    print('以上值都为真')
else :
    print('以上有一个值为假')


