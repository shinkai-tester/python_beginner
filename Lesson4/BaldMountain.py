TotalLength = int(input())
PreviousHeight = 0
CurrClimb = 0
MaxClimb = 0
for i in range(TotalLength // 100):
    Height = int(input())
    if Height > PreviousHeight:
        PreviousHeight = Height
        CurrClimb += 1
    else:
        PreviousHeight = Height
        MaxClimb = max(MaxClimb, CurrClimb)
        CurrClimb = 0
MaxClimb = max(MaxClimb, CurrClimb)
print(MaxClimb * 100)


