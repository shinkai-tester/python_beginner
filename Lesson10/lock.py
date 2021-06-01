state_trans = [{'А': 0, 'Б': 1, 'В': 0, 'Г': 0, 'Д': 0},
               {'А': 2, 'Б': 0, 'В': 0, 'Г': 0, 'Д': 0},
               {'А': 0, 'Б': 0, 'В': 0, 'Г': 0, 'Д': 0}]
N = int(input())
state = 0

for i in range(N):
    letter = input()
    if state == 2 and letter == 'В':
        print('Открыт')
    else:
        print('Закрыт')
    state = state_trans[state][letter]
