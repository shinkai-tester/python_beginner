import os


def start():
    while True:
        print('Главное меню')
        print('Введите X если хотите играть за крестиков')
        print('Введите 0 если хотите играть за ноликов')
        command = input('Введите команду: ')
        if command == 'X':
            game('X')
            input()
        elif command == '0':
            game('0')
            input()
        elif command == 'exit':
            break
        else:
            print('Команда некорректна!')
            input()
        os.system('cls')


def game(symbol):
    os.system('cls')
    print('Старт игры за %s' % symbol)
    turn = 1
    field = [['*' for i in range(3)] for k in range(3)]
    while turn < 10:
        bot_turn_boolean = False
        if turn % 2 == 1:
            print('Сейчас ход крестиков')
            if symbol == 'X':
                human_turn(field, 'X')
            else:
                bot_turn(field, 'X')
                bot_turn_boolean = True
                print_field(field)
        else:
            print('Сейчас ход ноликов')
            if symbol == 'X':
                bot_turn(field, '0')
                bot_turn_boolean = True
                print_field(field)
            else:
                human_turn(field, '0')

        win = analyse(field)
        if win == 'X':
            if not bot_turn_boolean:
                print_field(field)
            print('ПОБЕДА КРЕСТИКОВ')
            break
        if win == '0':
            if not bot_turn_boolean:
                print_field(field)
            print('ПОБЕДА НОЛИКОВ')
            break
        turn += 1
        if turn == 10:
            if not bot_turn_boolean:
                print_field(field)
            print('НИЧЬЯ')
            break


def human_turn(field, symbol):
    x, y = [int(i) - 1 for i in input('Введите координаты: ').split()]
    field[x][y] = symbol


def bot_turn(field, symbol):
    values = [[0 for i in range(3)] for i in range(3)]

    values[1][1] = 1

    for i in range(3):
        for k in range(3):
            if field[i][k] == '*':
                values[i][k] += count_priority(field, symbol, i, k)
            else:
                values[i][k] = -1

    m = 0
    m_index_i = 0
    m_index_k = 0
    for i in range(3):
        for k in range(3):
            if values[i][k] > m:
                m = values[i][k]
                m_index_i = i
                m_index_k = k

    field[m_index_i][m_index_k] = symbol


def count_priority(field, symbol, i, k):
    proirity = 0
    tmp = [0, 0, -1]

    for z in range(3):
        if field[i][z] == 'X':
            tmp[0] += 1
        if field[i][z] == '0':
            tmp[1] += 1
        else:
            tmp[2] += 1

    proirity += return_priority(symbol, tmp)
    tmp = [0, 0, -1]

    for z in range(3):
        if field[z][k] == 'X':
            tmp[0] += 1
        if field[z][k] == '0':
            tmp[1] += 1
        else:
            tmp[2] += 1

    proirity += return_priority(symbol, tmp)
    tmp = [0, 0, -1]

    if i == k:
        for z in range(3):
            if field[z][z] == 'X':
                tmp[0] += 1
            if field[z][z] == '0':
                tmp[1] += 1
            else:
                tmp[2] += 1

    proirity += return_priority(symbol, tmp)
    tmp = [0, 0, -1]

    if i + k == 2:
        for z in range(3):
            if field[z][2 - z] == 'X':
                tmp[0] += 1
            if field[z][2 - z] == '0':
                tmp[1] += 1
            else:
                tmp[2] += 1

    proirity += return_priority(symbol, tmp)

    return proirity


def return_priority(symbol, tmp):
    if symbol == '0':
        tmp[0], tmp[1] = tmp[1], tmp[0]
    if tmp[0] == 2:
        return 100
    if tmp[0] == 1 and tmp[2] == 1:
        return 2
    if tmp[0] == 1 and tmp[1] == 1:
        return 1
    if tmp[1] == 2:
        return 15
    return 0


def print_field(field):
    for i in field:
        for k in i:
            print(k, end=' ')
        print()


def analyse(field):

    winner = ([field[0][0], field[0][1], field[0][2]],
              [field[1][0], field[1][1], field[1][2]],
              [field[2][0], field[2][1], field[2][2]],
              [field[0][0], field[1][0], field[2][0]],
              [field[0][1], field[1][1], field[2][1]],
              [field[0][2], field[1][2], field[2][2]],
              [field[0][0], field[1][1], field[2][2]],
              [field[0][2], field[1][1], field[2][0]])

    for i in winner:
        if i[0] == i[1] == i[2]:
            if i[0] == 'X':
                return 'X'
            if i[0] == '0':
                return '0'

start()