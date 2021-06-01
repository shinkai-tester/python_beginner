import mimesis

new_content = ''

with open('spisok.txt', 'r+', encoding='UTF-8') as f:
    person = mimesis.Person('ru')
    for line in f:
        new_content += person.full_name() + '\n'
    f.seek(0)
    f.truncate()
    f.write(new_content)
