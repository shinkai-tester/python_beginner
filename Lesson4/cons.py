import os
x = 100
while x != 0:
    print('Введите 0, чтобы ничего не было')
    print('Введите 1, чтобы с Вами поздоровались')
    print('Введите 2, чтобы узнать сумму двух чисел')
    print('Введите 3, чтобы мы напечатали Ваше имя десять раз')
    x = int(input('Введите команду: '))
    if x == 1:
        print('Hello!')
    elif x == 2:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(a + b)
    elif x == 3:
        name = input('Введите Ваше имя: ')
        for i in range(10):
            print(name)
    input()
    os.system('cls')