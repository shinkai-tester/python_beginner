Statuses = ['Тяжело болен', 'Болен', 'Слегка болен', 'Близок к выздоровлению', 'Выписать через пару дней', 'Выписан']
a = dict(
                    [(id, Statuses)
                        for id in range(1, 101)])
BeginState = a[1][1]
print(BeginState)