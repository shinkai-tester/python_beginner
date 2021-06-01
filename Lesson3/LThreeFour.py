ThreeFirst = input()
ThreeSecond = input()
sumFirst = int(ThreeFirst[0])+int(ThreeFirst[1])+int(ThreeFirst[2])
sumSecond = int(ThreeSecond[0])+int(ThreeSecond[1])+int(ThreeSecond[2])
if int(ThreeFirst[0]) == 0:
    print('Номер билета не может начинаться с нуля!')
elif sumFirst == sumSecond and int(ThreeSecond) < 999:
    changeNumber = int(ThreeSecond)  + 1
    print(ThreeFirst + str(changeNumber).zfill(3))
elif int(ThreeSecond)  + 1 == 1000 and sumFirst == sumSecond:
    print(ThreeFirst + '000')
else:
    print(ThreeFirst + ThreeSecond)