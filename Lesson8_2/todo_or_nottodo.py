def decor(func):
    def repl(text):
        text = text.replace(' делай ', ' не делай ')
        text = text.replace('Делай ', 'Не делай ')
        text = text.replace(' не не делай ', ' не делай ')
        text = text.replace('Не не делай ', 'Не делай ')
        changed_magic = func(text)
        return changed_magic
    return repl

@decor
def magic(text):
    todo = text.count(' делай ') + text.count('Делай ') - (text.count('Не делай ') + text.count(' не делай '))
    return text + '!' + ' (Tasks to do = %s)' % todo

print(magic(input()))