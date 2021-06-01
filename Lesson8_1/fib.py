def fib(a):
    d0 = 0
    if a == 0:
        return d0
    d1 = 1
    for i in range(a - 1):
        d0, d1 = d1, d0 + d1
    return d1


for k in range(0, 100):
    print(fib(k))
