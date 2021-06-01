FieldSize = 3
field = [['*' for i in range(FieldSize)] for k in range(FieldSize)]

for i in field:
    for k in i:
        print(k, end= ' ')
    print()