text = input()
new_text = []
for word in text.split():
    upper = 0
    lower = 0
    for i in word:
        if 1040 <= ord(i) <= 1071:
            upper += 1
        if 1072 <= ord(i) <= 1103:
            lower += 1
    if lower >= upper:
        new_text.append(word)
print(' '.join(new_text))
