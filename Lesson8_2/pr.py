def f():
    x = int(input())
    if x == 0:
        return
    f()
    print(x)


f()
