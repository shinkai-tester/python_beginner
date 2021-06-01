def f(x):
    return x ** 2


def g(x):
    return x ** 3


def Print(func, x=0):
    print(func(x))


def m(func, lst):
    for i in range(len(lst)):
        lst[i] = func(lst[i])
    return lst


#n = list(map(int, input().split()))
#print(n)