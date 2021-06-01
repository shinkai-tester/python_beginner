list1 = [101, 101, 1, 10, 100, 11, 10]
unwanted = []
total = 0
number = -1

for ele in range(0, len(list1)):
    total = total + list1[ele]
    number += 1
    if total >= 100:
        print(total)
        total = 0
        number = 0
    else:
        print('No')
