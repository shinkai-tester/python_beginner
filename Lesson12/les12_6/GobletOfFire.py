import json
import pickle
from operator import attrgetter
import os
from itertools import groupby


class ToWrite:

    def __init__(self, n, s, ma):
        self.name = n
        self.school = s
        self.magic_age = ma

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.school, self.magic_age)


def Triwizard():
    best_students = {}
    with open('registered.pickle', 'rb') as register:
        unpickled = []
        while True:
            try:
                i = pickle.load(register)
            except EOFError:
                break
            unpickled.append(i)

    for g, data in groupby(unpickled, key=attrgetter('school')):
        o = max(data, key=attrgetter('magic_age'))
        best_students.update({o.school: o.name})
        for i in unpickled:
            if i.magic_age == o.magic_age and i.school == o.school and i.name != o.name:
                best_students.update({o.school: [o.name, i.name]})
    os.remove('registered.pickle')
    WriteToBest(best_students)


def WriteToBest(best):
    with open('final.txt', 'w', encoding='UTF-8') as f:
        for value in best.values():
            if type(value) == list:
                f.write('{}\n'.format(', '.join(value)))
            else:
                f.write('{}\n'.format(value))


def WriteToPickle(stud):
    with open('registered.pickle', 'ab') as register:
        pickle.dump(stud, register)


def check_student(comm):
    name = comm[0]
    school = comm[1]
    with open('data.json', 'r', encoding='UTF-8') as f_json:
        data = json.load(f_json)
        if name in data and data[name]['Школа'] == school and data[name]['Возраст'] >= 17:
            student = ToWrite(name, school, data[name]['Возраст'] + data[name]['Магическая сила'])
            WriteToPickle(student)
        else:
            print('You shall not pass!')


command = input().split(', ')
while command[0] != 'Конец регистрации 192819':
    check_student(command)
    command = input().split(', ')
Triwizard()
