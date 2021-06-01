d = dict()
text = input().lower()
for i in text:
    if 'a' <= i <= 'z':
        d[i] = d.get(i, 0) + 1

d = sorted(list(d.items()), key=lambda x: x[1], reverse=True)
for i in d:
    print(i[0], ': ', i[1], sep='')
