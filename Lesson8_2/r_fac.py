def r_f(n):
    if n == 0:
        return 1
    return n * r_f(n - 1)


print(r_f(10))
