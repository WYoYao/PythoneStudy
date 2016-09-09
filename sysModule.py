
#使用sys模块的第一步，就是导入该模块：
import sys

def test():
    #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    args=sys.argv
    print(args[0])
    lenth=len(args)
    if lenth==1:
        print('Hello World')
    elif lenth==2:
        print('hello %s' % args[1])
    elif lenth>2:
         print('Too many arguments!')

# 通过__name__ 判断出执行的文件的入口模块是否是本模块，可以使用比较 __来添测试当前模块的代码__
if __name__=='__main__':
    test()
    