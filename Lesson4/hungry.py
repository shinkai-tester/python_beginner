OrderNumber = int(input())
SumFinalLost = 0
SumLostFire = 20000
for k in range(OrderNumber):
    dish1, price1 = input().split()
    dish2, price2 = input().split()
    if int(price1) < int(price2):
        SumFinalLost += int(price1)
    else:
        SumFinalLost += int(price2)
if OrderNumber < 10:
    SumFinalLost += SumLostFire
print(SumFinalLost)