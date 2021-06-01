NumberOfElements = int(input())
UniqueSn = []
count = 0
for i in range(NumberOfElements):
    Surname = input()
    if Surname not in UniqueSn:
        UniqueSn.append(Surname)
for j in range(len(UniqueSn) - 1):
    for k in range(len(UniqueSn) - 1):
        if UniqueSn[k] > UniqueSn[k + 1]:
            UniqueSn[k], UniqueSn[k+1] = UniqueSn[k+1], UniqueSn[k]
            count += 1
print(UniqueSn, count, sep='\n')