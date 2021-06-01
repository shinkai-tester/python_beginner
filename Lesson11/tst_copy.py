class Student:

    def __init__(self, n, a, u):
        self.name = n #поле класса
        self.age = a
        self.uni = u
        print('Здесь был вызван конструктор')

    def hello(self):
        print("Hello, I'm %s" % self.name)

class Worker(Student):
    def __init__(self, n, a, u, p, z):
        Student.__init__(self, n, a, u)
        self.prof = p
        self.zp = z
        print('Здесь был вызван конструктор воркера')

    def hello(self):
        print("Hello, I'm %s, my profession is %s and I earn %d per month" % (self.name, self.prof, self.zp))

A = Worker('Ivan', 16, 'Fefe', 'Teacher', 44545)
A.hello()
S = Student('Ivan', 16, 'Fefe')
S.hello()

