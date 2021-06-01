def mx(*a):
    m = a[0]
    for i in a:
        if i > m:
            m = i
    return m


print(mx(1, 3, 4))
