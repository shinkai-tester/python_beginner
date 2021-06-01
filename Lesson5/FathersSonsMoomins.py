SurnamesMoomins = input().split()
for i in range(len(SurnamesMoomins)):
    if i - 1 < 0:
        past = 'Нет'
    else:
        past = SurnamesMoomins[i - 1]
    present = SurnamesMoomins[i]
    if i == len(SurnamesMoomins) - 1:
        future = 'Нет'
        print('Предшественник: ' + past, 'Текущая мумь: ' + present, 'Следующая мумь: ' + future, sep='\n')
    else:
        future = SurnamesMoomins[i + 1]
        print('Предшественник: ' + past, 'Текущая мумь: ' + present, 'Следующая мумь: ' + future, '-----', sep='\n')
