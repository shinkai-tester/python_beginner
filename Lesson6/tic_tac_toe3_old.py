FieldSize = 3
field = []
value = 'S'

for i in range(FieldSize):
    field.append(input().split())

for x in range(FieldSize):
    for y in range(FieldSize):
        if field[x][y] != '*':
            if (field[0][y] == field[1][y] ==  field[2][y] or
            field[x][0] == field[x][1] == field[x][2] or
            field[0][0] == field[1][1] == field[2][2] or
            field[0][2] == field[1][1] == field[2][0]):
                value = field[x][y]
if value == 'X':
    print('Крестики')
elif value == '0':
    print('Нолики')
else:
    print('Никто не победил')