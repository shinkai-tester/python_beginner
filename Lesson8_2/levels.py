def labyrinth(levels, orcs_first, L):
    if levels == 1:
        return orcs_first
    return min(labyrinth(levels - 1, orcs_first, L) ** 2, labyrinth(levels - 1, orcs_first, L) + L)


print(labyrinth(int(input()), int(input()), int(input())))
