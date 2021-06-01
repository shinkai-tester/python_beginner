PriceGoose = int(input())
AmountGoose = int(input())
PurePrice = PriceGoose * AmountGoose
if PriceGoose < 0 or AmountGoose < 0:
    print('Введено отрицательное число, невозможно посчитать цену')
elif AmountGoose <= 5:
    print(int(PurePrice))
elif 5 < AmountGoose <= 10:
    FinalPrice1 = PurePrice - PurePrice * 0.25
    print(int(FinalPrice1))
elif AmountGoose > 10:
    FinalPrice2 = PurePrice - PurePrice * 0.5
    print(int(FinalPrice2))