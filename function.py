'''
    list和tuple的区别：
        list是一种有序的集合，可是随时添加删除其中的元素
            取List最后一个元素 可以用list[-1]
            尾部添加元素，append(contend);
            insert(index, content)  指定位置插入元素
            pop()尾部删除元素，pop(index)删除指定索引元素
        tuple是一种有序列表，初始化后不能被修改（）

    函数：
    .必选参数在前，默认参数在后
'''
# 可变参数
def my_add(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(my_add(1,2,3))

# list 和 truple可以通过在前面加一个*变为可变参数
nums1 = [1,2,3,4]
nums2 = (2,2,3,4)
print(my_add(*nums1))
print(my_add(*nums2))

# 关键字参数
# 可变参数允许传入0或多个参数，这些参数在函数调用的时候被封装成一个tuple，而关键字参数允许传入0个或多个含函数名的参数，这些参数在函数内部组装成一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:',kw)

person('wangqi', 18)

# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
# 汉诺塔经典算法
def move(n,a,b,c):
    if(n == 1):
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1,b, a, c)

move(3, 'a', 'b' ,'c')

