razm = 5
pole = [[0 for i in range(razm + 2)] for k in range(razm + 2)]
pole1 = [[0 for i in range(razm + 2)] for k in range(razm + 2)]
mines = 5
for i in range(mines):
    x, y = [int(i) for i in input('Введите координату мины ').split()]
    pole[x][y] = 1
    pole1[x][y] = '*'

for x in range(1, razm + 1):
    for y in range(1, razm + 1):
        if pole1[x][y] != '*':
            pole1[x][y] = (pole[x + 1][y] + pole[x - 1][y] + pole[x][y + 1] + pole[x][y - 1] +
                           pole[x + 1][y + 1] + pole[x + 1][y - 1] + pole[x - 1][y + 1] + pole[x - 1][y - 1])

for x in range(1, razm + 1):
    for y in range(1, razm + 1):
        print(pole1[x][y], end=' ')
    print()