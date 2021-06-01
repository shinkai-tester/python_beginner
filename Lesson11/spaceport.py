class Rocket:

    def __init__(self, y, m):
        self.year = y
        self.mileage = m

    def print_fields(self):
        print("Год создания: %d" % self.year)
        print("Пробег: %d" % self.mileage)

    def avg_mileage(self):
        avg_mil = self.mileage / (2019 - self.year)
        return avg_mil


class UFO(Rocket):
    def __init__(self, y, m, b, c):
        Rocket.__init__(self, y, m)
        self.brand = b
        self.company = c

    def print_fields(self):
        Rocket.print_fields(self)
        print("Марка: %s" % self.brand)
        print("Владелец: %s" % self.company)

year, mileage = [int(i) for i in input().split()]
r = Rocket(year, mileage)
year, mileage, brand, company = input().split()
u = UFO(int(year), int(mileage), brand, company)
r.print_fields()
print(r.avg_mileage())
u.print_fields()
print(u.avg_mileage())
