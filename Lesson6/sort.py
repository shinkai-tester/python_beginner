N = int(input())
a = []
for i in range(N):
    a.append([int(i) for i in input().split()])

for i in range(N):
    for k in range(N - 1):
        if sum(a[k]) > sum(a[k + 1]):
            a[k], a[k + 1] = a[k + 1], a[k]

for i in range(N):
    for k in range(len(a[i])):
        print(a[i][k], end=' ')
    print()