Tourist1 = input()
Tourist2 = input()
Tourist3 = input()
if Tourist1 == 'Член профсоюза':
    Price1 = 10
elif Tourist1 == 'Ребенок':
    Price1 = 5
elif Tourist1 == 'Не член профсоюза':
    Price1 = 30
elif Tourist1 == 'Милиционер':
    Price1 = 5
if Tourist2 == 'Член профсоюза':
    Price2 = 10
elif Tourist2 == 'Ребенок':
    Price2 = 5
elif Tourist2 == 'Не член профсоюза':
    Price1 = 30
elif Tourist2 == 'Милиционер':
    Price2 = 5
if Tourist3 == 'Член профсоюза':
    Price3 = 10
elif Tourist3 == 'Ребенок':
    Price3 = 5
elif Tourist3 == 'Не член профсоюза':
    Price3 = 30
elif Tourist3 == 'Милиционер':
    Price3 = 5
total = Price1 + Price2 + Price3
print(total)