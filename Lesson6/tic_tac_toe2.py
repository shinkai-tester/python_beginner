FieldSize = 3
field = [['*' for i in range(FieldSize + 1)] for k in range(FieldSize + 1)]
command = input()

while command != 'Stop':
        x, y = [int(i) for i in input().split()]
        if x > len(field) - 1 or y > len(field) - 1:
            print('Такой координаты не существует!')
        else:
            if field[x][y] == '*':
                if command == 'Крестик':
                    field[x][y] = 'X'
                if command == 'Нолик':
                    field[x][y] = '0'
            else:
                print('На этом поле уже стоит символ!')
        command = input()

for x in range(1, FieldSize + 1):
    for y in range(1, FieldSize + 1):
        print(field[x][y], end=' ')
    print()