
try:
    a = int(input())
    b = int(input())
    print(a/b)
except ZeroDivisionError:
    print('b = 0')
except ValueError:
    print('.')
finally:
    print('Работа программы закончена')
