L = list(range(10))

# 取下标n-m个
'''
当n为0时可以省略
'''

n = 1
m = 3
l1= L[n:m]

print (l1) #[1,2]

print(L[-3:-1]) #[7,8]

print(L[1:]) #[1, 2, 3, 4, 5, 6, 7, 8, 9]取第1个开始以后的所有

print(L[:7:2]) #[0, 2, 4, 6] 前7个数每隔2取1个

print(L[:]) #复制一个list


# 通过切片删除字符串前后空格
def trim(s):
    while s[0] == ' ':
        s = s[1:]
    while s[-1] == ' ':
        s = s[:-1]
    return s

print(trim('  www  '))

'''
'''

