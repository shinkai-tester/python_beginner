x = input()
a= []
while x != '0':
    a.append(x)
    x = input()
length = len(a)
for i in range(length):
    print(-i - 1, end = ' ')
    print(a[- i - 1])