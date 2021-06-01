N = int(input())
b = []
for i in range(N):
    a = input()
    a = a.split()
    for k in range(len(a)):
        a[k] = int(a[k])
    b.append(a)

for l in b:
    for m in l:
        print(m, end=' ')
    print()