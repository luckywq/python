# filter

def isOdd(n):
    return n % 2 == 1

print(list(filter(isOdd,range(10)))) #[1, 3, 5, 7, 9]