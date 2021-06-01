number = int(input())
max1 = 0
max2 = 0
max3 = 0
kind1 = 'a'
kind2 = 'b'
kind3 = 'c'
while number <= 3:
    print('Количество цветов должно быть больше трёх!')
    number = int(input('Введите количество цветов еще раз: '))
for k in range(number):
    kind = input()
    NumberKind = int(input())
    if NumberKind > max1:
        max3 = max2
        max2 = max1
        max1 = NumberKind
        kind3 = kind2
        kind2 = kind1
        kind1 = kind
    else:
        if NumberKind > max2:
            max3 = max2
            max2 = NumberKind
            kind3 = kind2
            kind2 = kind
        else:
            if NumberKind > max3:
                max3 = NumberKind
                kind3 = kind
print(kind1, kind2, kind3, sep = '\n')