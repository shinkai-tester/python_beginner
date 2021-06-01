def f(x):
    if x == 0:
        return
    print('A')
    f(x - 1)


f(10)
