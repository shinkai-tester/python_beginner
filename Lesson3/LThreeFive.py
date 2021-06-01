chargeOne = int(input())
chargeTwo = int(input())
if chargeOne == 0 or chargeTwo == 0:
    print('Ноль на входных данных!')
if (chargeOne < 0 and chargeTwo < 0) or (chargeOne > 0 and chargeTwo > 0):
    print('Одноименные')
else:
    print('Разноименные')
