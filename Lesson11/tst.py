class Student:

    number = 0

    def __init__(self, n, a, u):
        self.name = n #поле класса
        self.age = a
        self.uni = u
        Student.number += 1 #поле класса, а не конкретного студента
        print('Здесь был вызван конструктор')

    def __del__(self): #сборщик мусора
        print('Объект класса уничтожен')

    def hello(self):
        print("Hello, I'm %s" % self.name)
#метод класса - функции, которые работают с полями класса

    @staticmethod
    def print_num():
        print(Student.number)

class Worker(Student):
    pass

Students = []

for i in range(10):
    Students.append(Student('A', 20 + i, 'B'))

S = Student('Ilya', 16, 'MGU') #объект класса
A = Student('Misha', 20, 'VSU')
S.hello()
Student.print_num()
print('Это конец программы')

A = Worker('Name', 16, 'Fefe')
print(A.name)
A.hello()

# a = input()
# a = a.split() #метод класса str
# init - конструктор
