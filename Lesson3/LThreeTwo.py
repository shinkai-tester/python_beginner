chair1 = int(input())
chair2 = int(input())
chair3 = int(input())
chair4 = int(input())
if chair1 > chair2 and chair1 > chair3 and chair1 > chair4:
    print('1')
elif chair2 > chair1 and chair2 > chair3 and chair2 > chair4:
    print('2')
elif chair3 > chair1 and chair3 > chair2 and chair3 > chair4:
    print('3')
elif chair4 > chair1 and chair4 > chair2 and chair4 > chair3:
    print('4')
else:
    print('Не могу определить: одинаковый вес')