current_position = 0
my_li = [1, 2, 3, 4, 5]
for i in range(0, 8):
    value = my_li[current_position % (len(my_li))]
    current_position += 1
    print(value)
for i in range(0, 5):
    value = my_li[current_position % (len(my_li))]
    current_position += 1
    print(value)