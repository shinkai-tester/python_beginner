pass_chars, *orcs_chars = input().split(',')
height, strength, speed = map(int, pass_chars.split())
pass_orcs = list(filter(lambda x: int(x[1]) >= height and int(x[2]) >= strength and int(x[3]) >= speed, list(map(lambda x: x.split(), orcs_chars))))
names_pass_orcs = ' '.join(list(list(zip(*pass_orcs))[0]))
the_best_orc = (max(pass_orcs, key=lambda x: int(x[1]) + int(x[2]) + int(x[3])))
print(names_pass_orcs, the_best_orc[0], sep='\n')