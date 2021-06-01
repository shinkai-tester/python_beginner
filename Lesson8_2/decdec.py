def dec(func):
    def f_for_decorate():
        print('Привет, я выполнюсь до кода')
        func()
        print('Привет, я выполнюсь после кода')
    return f_for_decorate


@dec
def pr():
    print('Я выполню какой-то код')


pr()
