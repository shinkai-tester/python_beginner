Name = input()
BirthDate = int(input())
sum = 0

while not(1800 <= BirthDate <= 2017):
    print('Год рождения не входит в диапазон от 1800 до 2017!')
    BirthDate = int(input('Введите год еще раз: '))

multi = BirthDate * 4 % 1000

for i in str(multi):
    sum += int(i)

print('Раз, два... Меркурий в четвертом доме... луна ушла... шесть – несчастье... вечер – семь...')
if sum % 2 == 0:
    print('Вас ждет уважение.')
if sum % 8 == 0:
    print('Вы будете богат.')
if 10 <= abs(sum) < 100:
    print('Вы проживете долгую жизнь.')
if sum == 7:
    print('Сегодня вечером вам отрежут голову. Аннушка уже купила подсолнечное масло, и не только купила, но даже разлила.')
if sum == 8:
    print('Вы попадете в сумасшедший дом.')
if  sum % 4 == 0:
    print('В Вашей жизни будет великая любовь.')
if sum == 24:
    print('Вы запишете курс “Python для начинающих”!')
else:
    if sum % 2 != 0 and sum % 8 != 0 and sum % 4 != 0 and not(10 <= abs(sum) < 100) and sum not in (7, 8, 24):
        print('Я не могу предсказать вашу судьбу!')