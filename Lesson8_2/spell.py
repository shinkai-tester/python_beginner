print('\n'.join(map(lambda spell: ''.join(map(lambda numb: chr(int(numb)), spell.split(' '))), filter(lambda x: len(x.split()) == 6, input().split(';')))))
