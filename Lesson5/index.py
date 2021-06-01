a = [int(i) for i in input().split()]
m = -1
index = -1
if len(a) == 6:
    for i in range(6):
        if a[i] > m:
            m = a[i]
            index = i
    print(index + 1)
else:
    print('Вы ввели некорректные данные')
