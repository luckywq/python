# map(fn, Iterable)

def f(x):
    return x * x

r = map(f, range(1,10))

print(list(r)) #[1, 4, 9, 16, 25, 36, 49, 64, 81]


# reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(fn, [a,b,c,d]) = f(f(f(a,b),c),d)

from functools import reduce

def add(x,y):
    return x + y

print(reduce(add, range(1,5)))




