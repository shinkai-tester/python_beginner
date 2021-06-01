begin_poloz = list([i.split() for i in input().split(', ')])
final_poloz = begin_poloz.copy()
i = 0
length = len(final_poloz)

while i < (length - 1):
    for k in range(i + 1, length):
        i_set = set(final_poloz[i])
        k_set = set(final_poloz[k])
        if i_set & k_set:
            final_poloz.pop(k)
            final_poloz.pop(i)
            union_ik = i_set | k_set
            final_poloz.append(list(union_ik))
            length -= 1
            i -= 1
            break
    i += 1

result = list(map(lambda a: sorted(a), sorted(final_poloz, key=len)))

for s in result:
    print(*s)
