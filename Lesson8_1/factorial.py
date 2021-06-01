def factor(n):
    s = 1
    for a in range(2, n + 1):
        s *= a
    return s


for i in range(2, 10):
    print(factor(i))
