NumberOfElements = int(input())
a = []
b = []
for i in range(NumberOfElements):
    Surname = input()
    a.append(Surname)
print(list(set(a)))