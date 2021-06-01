FieldSize = 3
field = [['*' for i in range(FieldSize + 1)] for k in range(FieldSize + 1)]
winner_positions = (
        [[(x, y) for y in range(1, 4)] for x in range(1, 4)] +
        [[(x, y) for x in range(1, 4)] for y in range(1, 4)] +
        [[(d, d) for d in range(1, 4)]] +
        [[(d, 4 - d) for d in range(1, 4)]]
)
count = 0

def who_is_winner(field):
    for positions in winner_positions:
        values = [field[x][y] for (x, y) in positions]
        if len(set(values)) == 1 and values[0] != '*':
            return values[0]


while True:
    count += 1
    a, b = [int(i) for i in input().split()]
    if count % 2 != 0:
        field[a][b] = 'X'
    if count % 2 == 0:
        field[a][b] = '0'

    for a in range(1, FieldSize + 1):
        for b in range(1, FieldSize + 1):
            print(field[a][b], end=' ')
        print()
    print()

    if who_is_winner(field) != '0' and who_is_winner(field) != 'X' and count == 9:
        print('Ничья')
        break
    elif who_is_winner(field) == '0':
        print('Победа ноликов')
        break
    elif who_is_winner(field) == 'X':
        print('Победа крестиков')
        break
