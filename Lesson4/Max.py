s = 0
x = int(input())
while x != 0:
    if x > s:
        s = x
    x = int(input())
print(s)