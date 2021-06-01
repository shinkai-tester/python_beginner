command = 'Start'
SurnamesList = []
ValidSurnames = []
SnListForDelete =[]
while command[0] != 'Stop':
    command = input().split()
    if command[0] == 'Добавить':
        surname = command[3]
        if surname not in SurnamesList:
            SurnamesList.append(surname)
            SnListForDelete.append(1)
    if command[0] == 'Удалить' and command[2] == 'индексу':
        k = int(command[3])
        if len(SnListForDelete) - 1 >= k:
            SnListForDelete[k] = 0
        else:
            print('В списке нет такого индекса')
    if command[0] == 'Удалить' and command[2] == 'фамилии':
        SurnameRemove = command[3]
        if SurnameRemove in SurnamesList:
            SnIndex = SurnamesList.index(SurnameRemove)
            SnListForDelete[SnIndex] = 0
        else:
            print('В списке нет такой фамилии')
for i in range(len(SurnamesList)):
    if SnListForDelete[i] == 1:
        ValidSurnames.append(SurnamesList[i])
print(SurnamesList)
print(SnListForDelete)
print(ValidSurnames)