def puzir(lst):
    for i in range(len(lst) - 1):
        for k in range(len(lst) - 1):
            if lst[k] > lst[k + 1]:
                lst[k], lst[k + 1] = lst[k + 1], lst[k]
    print('Сортировка пузырьком выполнена успешно')
    return lst


def vibor(spisok):
    for i in range(len(spisok) - 1):
        for k in range(i + 1, len(spisok)):
            if spisok[k] < spisok[i]:
                spisok[k], spisok[i] = spisok[i], spisok[k]
    print('Сортировка выбором выполнена успешно')
    return spisok


a = [int(i) for i in input().split()]
puzir(a)
print(a)
a = [int(i) for i in input().split()]
vibor(a)
print(a)
