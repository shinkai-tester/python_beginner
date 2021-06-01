N = int(input())
d = dict()

for i in range(N):
    info = input().split()
    parent = info[0]
    childs = info[1:]
    for child in childs:
        d[child] = parent
    if parent not in d:
        d[parent] = None

N = int(input())
for i in range(N):
    zapros = input().split()
    parent = zapros[0]
    child = zapros[1]
    while child != parent and child is not None:
        child = d[child]
    if child is None:
        print('NO')
    else:
        print('YES')



'''
8
A B C D
B F G
F O I
F P
Alexei Stepan Misha
Vladimir Alexei
Stepan Ilya
Misha Egor Dima
'''