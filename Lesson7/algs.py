# a = input()
# b = ''
# for i in range(len(a) - 1, -1, -1):
#     b += a[i]
# print(b)
a = input().split()
for i in range(1, len(a), 2):
    print(a[i])
#print('\n'.join(str(len(i)) for i in input().split()))
