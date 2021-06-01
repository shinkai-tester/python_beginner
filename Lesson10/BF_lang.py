def create_dict(bfcode):
    slovar = {}
    save_key = []
    for i in range(len(bfcode)):
        if bfcode[i] == '[':
            save_key.append(i)
        if bfcode[i] == ']':
            key = save_key.pop()
            slovar[key] = i
    slovar_reverse = {value: key for key, value in slovar.items()}
    slovar.update(slovar_reverse)
    return slovar


def run_bfcode(bfcode, slovar):
    index_command = 0
    lst = [0 for i in range(30000)]
    index = 15000
    while index_command < len(bfcode):
        if bfcode[index_command] == '+':
            lst[index] += 1
        elif bfcode[index_command] == '-':
            lst[index] -= 1
        elif bfcode[index_command] == '>':
            index += 1
        elif bfcode[index_command] == '<':
            index -= 1
        elif bfcode[index_command] == ',':
            lst[index] = ord(input())
        elif bfcode[index_command] == '.':
            print(chr(lst[index]), end='')
        elif bfcode[index_command] == '[':
            if lst[index] == 0:
                index_command = slovar[index_command]
        elif bfcode[index_command] == ']':
            index_command = slovar[index_command] - 1
        index_command += 1


cleaned_code = ''.join([i for i in input() if i in '+-<>[].,'])
slovarik = create_dict(cleaned_code)
run_bfcode(cleaned_code, slovarik)
