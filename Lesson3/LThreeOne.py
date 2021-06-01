A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
LetCoordW = input()
NumCoordW = int(input())
LetCoordB = input()
NumCoordB = int(input())

if NumCoordW > 8 or NumCoordB > 8:
    print('Введена неверная цифра координаты')
elif not(LetCoordW in A) or not(LetCoordB in A):
    print('Введена неверная буква координаты')
elif  LetCoordW == LetCoordB and NumCoordW == NumCoordB:
    print('Введены две одинаковые координаты')
else:
    print('Координаты введены верно, генерируем ответ')
    if LetCoordW == LetCoordB  or NumCoordW == NumCoordB:
        print('YES')
    else:
        print('NO')


