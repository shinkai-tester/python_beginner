class Rational:

    def __init__(self, c, z=1):
        self.c = c
        self.z = z
        print('Создана новая дробь:', self)
        self.sokr()

    def __repr__(self):
        self.sokr()
        return '%s/%s = %s' % (str(self.c), str(self.z), str(self.to_float()))

    def to_float(self):
        return self.c / self.z

    def rev(self):
        self.c, self.z = self.z, self.c
        self.sokr()

    def __add__(self, other):
        c = self.c * Rational.nok(self.z, other.z) // self.z + other.c * Rational.nok(other.z, self.z) // other.z
        z = Rational.nok(self.z, other.z)
        return Rational(c, z)

    def __sub__(self, other):
        c = self.c * Rational.nok(self.z, other.z) // self.z - other.c * Rational.nok(other.z, self.z) // other.z
        z = Rational.nok(self.z, other.z)
        return Rational(c, z)

    def __mul__(self, other):
        c = self.c * other.c
        z = self.z * other.z
        return Rational(c, z)

    def __truediv__(self, other):
        c = self.c * other.z
        z = self.z * other.c
        return Rational(c, z)

    def __str__(self):
        return '%s/%s' % (str(self.c), str(self.z))

    def __eq__(self, other):
        if self.c == other.c and self.z == other.z:
            return True
        return False

    def __lt__(self, other):
        if (self - other).c < 0:
            return True
        return False

    @staticmethod
    def nod(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def nok(a, b):
        return a * b // Rational.nod(a, b)

    def sokr(self):
        n = Rational.nod(self.c, self.z)
        self.c //= n
        self.z //= n
        if self.z < 0:
            self.c *= -1
            self.z *= -1

a = [Rational(1, 1),
    Rational(1, 3),
    Rational(2),
    Rational(-3),
    Rational(-5, 1),
    Rational(-5, 100)]

print(sorted(a))
