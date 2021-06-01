def heal_animals(num_crystals):
    if num_crystals == 8:
        return [3, 5]

    spisok = sorted(heal_animals(num_crystals - 1))

    if 5 in spisok:
        spisok[-1:] = [3, 3]
    else:
        spisok[-3:] = [5, 5]

    return spisok


print(sorted(heal_animals(int(input()))))
