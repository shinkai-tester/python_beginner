lines_coms = ''
with open('code.stack', 'r') as com:
    for command in com:
        lines_coms += command
commands = lines_coms.splitlines()

i = 0
while i < len(commands):
    if i == 6:
        i = 8
        continue
    else:
        print(commands[i])
    i+=1

print(chr(300))