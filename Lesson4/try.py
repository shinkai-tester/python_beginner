id = 1
number = int(input())
sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures[id + number])

print('-----------------------------------------------------------------------------')

Statuses = ['Тяжело болен', 'Болен', 'Слегка болен', 'Близок к выздоровлению', 'Выписать через пару дней', 'Выписан']
Requests = int(input())
id = 0
a = 1
d = {}
Command = 0
for i in range(Requests):
    Command = input()
    id = int(input())
    number = int(input())
    EndStatus = Statuses[a + number]
    d[id] = EndStatus
print(d[id])


Statuses = ['Тяжело болен', 'Болен', 'Слегка болен', 'Близок к выздоровлению', 'Выписать через пару дней', 'Выписан']
Requests = int(input())
id = 0
a = 1
d = {}
Command = 0
sum = 0
for i in range(Requests):
    Command = input()
    id = int(input())
    while not(1 <= id <= 100):
        print('Введён несуществующий id пациента!')
        id = int(input('Введите id ещё раз: '))
    if Command == 'Изменить статус':
        number = int(input())
        sum += number
        d[id] = Statuses[a + sum]
print(d)

