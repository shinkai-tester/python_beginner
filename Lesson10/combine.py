locations = int(input())
loc_zerno = {}
combine_loc = {}

for i in range(locations):
    zerno = input()
    loc_zerno[i] = zerno

combine_number = int(input())

for i in range(combine_number):
    combine_name = input()
    combine_loc[combine_name] = 0

signal = input().split()
curr_combine = list(combine_loc.keys())[0]
while 'Стоп' not in signal:
    if 'Локация' in signal:
        curr_loc = combine_loc.get(curr_combine)
        curr_zerno = loc_zerno.get(curr_loc)
        print('На данный момент комбайн %s собирает %s' % (curr_combine, curr_zerno))

    if signal[0] == 'Перемещение':
        if int(signal[1]) in loc_zerno:
            combine_loc[curr_combine] = int(signal[1])
        else:
            print('Локации №', signal[1], 'не существует')

    if signal[0] == 'Переключение':
        if signal[1] in combine_loc:
            curr_combine = signal[1]
        else:
            print('Комбайна', signal[1], 'не существует')
    signal = input().split()
