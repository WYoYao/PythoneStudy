# 调试程序用到的调试方法


'''
    # 1、 通过print 进行调试,如果在10/ 0 的时候出现错误，我们可以在之前的地方捕获到这个值然后查看

    def foo(s):
        n=int(s)
        print('>>> n=%d' % n)
        return 10/n

    def main():
        foo('0')
    # 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。
    main()
'''


'''
# 断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代


def foo(s):
    n=int(s)
    # 如果不满足断言（断言失败）的时候就会抛出错误
    # 如果满足则不会做任何的处理
    assert n!=0,'n is zero'
    return 10/n

print(foo('1'))
foo('0')

# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert
# 关闭后，你可以把所有的assert语句当成pass来看。
'''


# logging
'''
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
import logging
# 使用的时候需要配置 logging.basicConfig 有debug，info，warning，error等几个级别
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
'''



import pdb
s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)