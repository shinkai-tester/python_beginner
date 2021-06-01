NumberOfElements = int(input())
UniqueSn = []
for i in range(NumberOfElements):
    Surname = input()
    if Surname not in UniqueSn:
        UniqueSn.append(Surname)
print(UniqueSn)