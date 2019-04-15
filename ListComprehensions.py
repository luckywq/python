####列表生成器

# 生成[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x * x for x in range(1,11)])

# 加上条件，仅仅需要偶数的平方

print([x * x for x in range(1,11) if x % 2 == 0]) #[4, 16, 36, 64, 100]

# 循环嵌套可以生成全排列

print([m + n for m in 'ABC' for n in 'XYZ']) #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 类似map 对原list进行重新计算
print([x*x for x in [1,2,3]]) #[1, 4, 9]