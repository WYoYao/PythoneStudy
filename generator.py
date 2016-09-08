# 创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

print([y for y in (x * x for x in range(1,11))])

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

# o=fib(6)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3

# o=odd()

# next(o)
# next(o)
# next(o)

g=odd()
while True:
    try:
        x=next(g)
        print('g',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break