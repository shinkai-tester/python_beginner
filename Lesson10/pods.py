lst = [int(i) for i in input().split()]
a = [0] * 10
for i in lst:
    a[i] += 1

for i in range(len(a)):
    for k in range(a[i]):
        print(i, end = ' ')