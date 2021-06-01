students = input().split()
marks = input().split()
for i in range(len(marks)):
    if marks[i] == '2':
        students[i] = 'Двоечник'
for i in range(len(students)):
    print(students[i], ': ', marks[i], sep='')