max_v = 0
curr_vl = int(input())
while curr_vl != 0:
    if curr_vl > max_v:
        max_v = curr_vl
    if curr_vl == 100:
        break
    curr_vl = int(input())
print('Макс. влажность: ', max_v, '%', sep='')