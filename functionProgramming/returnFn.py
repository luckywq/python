# 返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

f = lazy_sum(1,2,3,4)
print(f())

# 闭包

def createCounter():
    li = [0]
    def counter():
        li[0] += 1
        return li[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())