FieldSize = 3
field = []
WinnerPositions = (
    [[(x, y) for y in range(3)] for x in range(3)] +
    [[(x, y) for x in range(3)] for y in range(3)] +
    [[(d, d) for d in range(3)]] +
    [[(2-d, d) for d in range(3)]]
)
symbol = '*'

for i in range(FieldSize):
    field.append(input().split())

for positions in WinnerPositions:
    values = [field[x][y] for (x, y) in positions]
    if len(set(values)) == 1 and values[0] != '*':
        symbol = values[0]
if symbol == 'X':
    print('Крестики')
elif symbol == '0':
    print('Нолики')
else:
    print('Никто не победил')