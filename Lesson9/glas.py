ch = set()
nech = set()
text = input().split()
flag = 1
glasn = 'eioua'
for word in text:
    for char in word:
        if char in glasn:
            if flag == 1:
                nech.add(char)
            else:
                ch.add(char)
    flag *= -1

print(ch - nech)