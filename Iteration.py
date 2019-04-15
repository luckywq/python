from collections.abc import Iterable

# 对象迭代
d = {'a': 1, 'b': 2, 'c': 3}

for key,value in d.items():        #迭代key  for key in d, 迭代value ：for v in d.values()
    print(key + '-->' + str(value))


# 判断对象是否可以迭代


print(isinstance('1111', Iterable)) # True
print(isinstance(1111, Iterable))  # False
print(isinstance((1,2,3,4), Iterable)) # True

# 迭代list索引以及本身
l1 = ['a','c','e']

for index, value in enumerate(l1):
    print(index, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


#通过迭代查找list中的最大值和最小值，返回tuple

llll = [1,2,3,4,5,6,7,8,9]

def getMaxMin(l):
    if len(l) == 0:
        return None,None
    max = l[0]
    min = l[0]
    for v in l:
        if v <= min:
            min = v
        if v >= max:
            max = v
    return (min,max)


print(getMaxMin(llll))