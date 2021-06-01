def prep(lst, num, sh):
    for i in range(sh):
        a = input('Игрок %s, введите координату корабля ' % num).split()
        x = int(a[0]) - 1
        y = int(a[1]) - 1
        lst[x][y] = 1

razm = 3
first = [[0 for i in range(razm)] for k in range(razm)]
second = [[0 for i in range(razm)] for k in range(razm)]
ships = 2
f_frags = 0
s_frags= 0

prep(first, '1', ships)
prep(second, '2', ships)

while f_frags < ships and s_frags < ships:
    a = input('Игрок 1, введите координату выстрела ').split()
    x = int(a[0]) - 1
    y = int(a[1]) - 1
    if second[x][y] == 1:
        f_frags += 1
        second[x][y] = 2
        print('Убил')
    else:
        second[x][y] ='*'
        print('Промазал')

    a = input('Игрок 2, введите координату выстрела ').split()
    x = int(a[0]) - 1
    y = int(a[1]) - 1
    if first[x][y] == 1:
        s_frags += 1
        first[x][y] = 2
        print('Убил')
    else:
        first[x][y] ='*'
        print('Промазал')

if s_frags == ships and f_frags == ships:
    print('Ничья')
elif s_frags == ships:
    print('Победа 2 игрока')
elif f_frags == ships:
    print('Победа 1 игрока')
else:
    print('Ошибка')

for i in first:
    for k in i:
        print(k, end= ' ')
    print()

print()

for i in second:
    for k in i:
        print(k, end= ' ')
    print()