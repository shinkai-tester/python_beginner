def injection(func):
    def dec(params):
        params[4:4] = [['vulnerability', False]]
        func(params)
        params[4], params[5] = params[5], params[4]
        func(params)

    return dec


def mydecor(func):
    def mydec(params):
        func(params)
        params[5][1] = not (params[5][1])

    return mydec


@mydecor
@injection
def invisibility(params):
    params[4][1] = not (params[4][1])


frodo = [['name', 'Frodo'], ['strength', 2], ['height', 1], ['speed', 4], ['invisibility', False]]
invisibility(frodo)
print(frodo)
