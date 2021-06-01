NumberOfElements = int(input())
Surnames = []
Lights = []
EndResult = []
for i in range(NumberOfElements):
    Surname = input()
    NumberLights = int(input())
    if Surname not in Surnames:
        Surnames.append(Surname)
        Lights.append(NumberLights)
for j in range(len(Surnames)):
    Result = [Surnames[j], Lights[j]]
    EndResult.append(Result)
for j in range(len(EndResult) - 1):
    for k in range(len(EndResult) - 1):
        if EndResult[k][1] > EndResult[k + 1][1]:
            EndResult[k], EndResult[k+1] = EndResult[k+1], EndResult[k]
print(EndResult)