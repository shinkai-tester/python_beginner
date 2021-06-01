Statuses = ['Тяжело болен', 'Болен', 'Слегка болен', 'Близок к выздоровлению', 'Выписать через пару дней', 'Выписан']
dictionary = {}
Requests = int(input())
for i in range(Requests):
    Command = input()
    id = int(input())
    while not(1 <= id <= 100):
        print('Введён несуществующий id пациента!')
        id = int(input('Введите id ещё раз: '))
    if Command == 'Изменить статус':
        number = int(input())
        if id in dictionary and dictionary[id] != 'Выписан':
            CurrState = dictionary.get(id, ' ')
            CurrStateIndex = Statuses.index(CurrState)
            NewStateIndex = CurrStateIndex  + number
            NewState = Statuses[NewStateIndex]
            dictionary[id] = NewState
        else:
            State = Statuses[1 + number]
            dictionary.update({id: State})
        if id in dictionary and dictionary[id] == 'Выписан' and number < 0:
            EndState = Statuses[0]
            dictionary[id] = EndState
            print('Изменение для ', id, ' может быть только положительным!')
            print('Введите id пациента и команду ещё раз. Если Вы хотите улучшить состояние данного пациента, введите 1.')
            continue
    if Command == 'Узнать статус':
        if id in dictionary:
            Result = dictionary[id]
        else:
            Result = Statuses[1]
        print(Result)