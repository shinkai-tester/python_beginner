n = int(input())
a = input().split()
if n > len(a):
    n %= len(a)
a = a[n:] + a[:n]
print(a)