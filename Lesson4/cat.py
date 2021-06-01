NumSpaces = 1
print('*' + '    ' + '*')
while NumSpaces < 7:
    print('*', end='')
    NumSpaces += 1
print(end='\n')
NumSpaces =1
print('*' + ' ' + '**' + ' ' + '*')
print('*' + '    ' + '*')
while NumSpaces < 7:
    print('*', end='')
    NumSpaces += 1
print(end='\n')
print('  **  ')
NumSpaces = 6
InnerSpaces = NumSpaces - 3
print ('*' * NumSpaces)
for i in range(InnerSpaces):
    print ('*' + '    '  + '*')
print ('*' * NumSpaces)
NumSpaces =1
Nothing = '  '
while NumSpaces < 11:
    Nothing += ' ' 
    print(Nothing + '**')
    print(Nothing + '**')
    NumSpaces += 1
    