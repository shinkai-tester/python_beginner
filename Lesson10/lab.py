lab =[{'Влево': None, 'Вверх': 1, 'Вправо': 2},
      {'Влево': None, 'Вниз': 0, 'Вправо': 3},
      {'Влево': 0, 'Вверх': 3},
      {'Влево': 1, 'Вверх': None, 'Вправо': 4, 'Вниз': 2},
      {'Вверх': None, 'Вниз': 3, 'Вправо': 'WIN'}]
zona = 0
while True:
    save_zona = zona
    print('Вы можете пойти: ')
    for i in lab[zona]:
        print(i)
    storona = input('Введите сторону, в которую Вы хотите пойти: ')
    if storona in lab[zona]:
        zona = lab[zona][storona]
    else:
        print('Вы ошиблись, Вы остаетесь в той же зоне')
    if zona is None:
        print('Это тупик')
        zona = save_zona
    if zona == 'WIN':
        print('Вы победили')
        tmp = input('Введите start, если хотите ещё поиграть, либо что угодно, чтобы выйти: ')
        if tmp == 'start':
            zona = 0
        else:
            break


