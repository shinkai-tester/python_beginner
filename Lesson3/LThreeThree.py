type = int(input())
RubToGold = int(input())
DolToGold = int(input())
CurToConv = int(input())

if type == 1:
    conv1 = (RubToGold/DolToGold) * CurToConv
    print(CurToConv,'Руб это', conv1,'$')
elif type == 2:
    conv2 = (DolToGold / RubToGold) * CurToConv
    print(CurToConv, '$ это', conv2, 'Руб')
else:
    if type != 1 and type != 2:
        print('Неверный тип перевода!')
    if RubToGold < 1 or DolToGold < 1:
        print('Курс должен быть натуральным числом!')
    if CurToConv < 0:
        print('Число валюты должно быть целым неотрицательным числом!')
