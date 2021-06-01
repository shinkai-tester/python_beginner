a = [1, 2, 3, 4, 5, 1, 2, 3, 6]
#for i in range(len(a)):
#    if a[i] in a[:i]:
#        print('Yes')
#    else:
#        print('NO')
b = set()
for i in a:
    if i in b:
        print('Yes')
    else:
        print('No')
    b.add(i)