_list = list([i.split() for i in input().split(', ')])
l = _list[:]

len_l = len(l)
i = 0
while i < (len_l - 1):
    for j in range(i + 1, len_l):
        i_set = set(l[i])
        j_set = set(l[j])
        if i_set.intersection(j_set):
            l.pop(j)
            l.pop(i)
            ij_union = list(i_set.union(j_set))
            l.append(ij_union)
            len_l -= 1
            i -= 1
            break

    i += 1

print(sorted(l))