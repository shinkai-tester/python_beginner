class Spaceport:

    def __init__(self):
        self.spaceships = []
        self.rockets = []
        self.ufos = []

    def ret_spaceships(self):
        return self.spaceships

    def print_spaceships(self):
        print(self.spaceships)

    def append_spaceship(self, spaceship):
        self.spaceships.append(spaceship)
        for spaceship in self.spaceships:
            if type(spaceship) == Rocket and spaceship not in self.rockets:
                self.rockets.append(spaceship)
            elif type(spaceship) == UFO and spaceship not in self.ufos:
                self.ufos.append(spaceship)

    def del_spaceship(self, index):
        if self.spaceships[index] in self.rockets:
            self.rockets.remove(self.spaceships[index])
        elif self.spaceships[index] in self.ufos:
            self.ufos.remove(self.spaceships[index])
        del self.spaceships[index]

    def ret_num(self):
        return len(self.spaceships)

    def print_num(self):
        print(len(self.spaceships))

    def ret_rocket(self):
        return self.rockets

    def print_rocket(self):
        print(self.rockets)

    def ret_ufo(self):
        return self.ufos

    def print_ufo(self):
        print(self.ufos)

    def ret_num_rocket(self):
        return len(self.rockets)

    def print_num_rocket(self):
        print(len(self.rockets))

    def ret_num_ufo(self):
        return len(self.ufos)

    def print_num_ufo(self):
        print(len(self.ufos))

    def ret_spaceships_after_date(self, date):
        ships_afer_date = []
        for ship in self.spaceships:
            if ship.year > date:
                ships_afer_date.append(ship)
        return ships_afer_date

    def print_spaceships_after_date(self, date):
        print(self.ret_spaceships_after_date(date))

    def ret_ufo_brand(self, brand):
        ufos_brand = []
        for u in self.ufos:
            if u.brand == brand:
                ufos_brand.append(u)
        return ufos_brand

    def print_ufo_brand(self, brand):
        print(self.ret_ufo_brand(brand))


class Rocket(Spaceport):

    def __init__(self, y, m):
        Spaceport.__init__(self)
        self.year = y
        self.mileage = m

    def __repr__(self):
        return 'Корабль(%s)' % self.year


class UFO(Rocket, Spaceport):
    def __init__(self, y, m, b, c):
        Spaceport.__init__(self)
        Rocket.__init__(self, y, m)
        self.brand = b
        self.company = c

    def __repr__(self):
        return 'Нло(%s, Владелец: %s, Марка: %s)' % (self.year, self.company, self.brand)


domodedovo = Spaceport()
domodedovo.print_num_rocket()
domodedovo.append_spaceship(UFO(2018, 1500, 'UFOLOG', 'Yand'))
domodedovo.print_rocket()
domodedovo.append_spaceship(Rocket(2007, 1500))
domodedovo.print_spaceships()
domodedovo.del_spaceship(1)
domodedovo.print_ufo()
domodedovo.print_rocket()
domodedovo.print_spaceships()
domodedovo.append_spaceship(UFO(2015, 1500, 'UFOLOG', 'Yamb'))
domodedovo.append_spaceship(UFO(2015, 1500, 'RocKETStAR', 'Yanb'))
domodedovo.append_spaceship(Rocket(2007, 15000))
print(domodedovo.ret_spaceships_after_date(2006))
domodedovo.print_spaceships_after_date(2008)
domodedovo.print_ufo_brand('UFOLOG')
domodedovo.del_spaceship(0)
domodedovo.print_ufo_brand('UFOLOG')
domodedovo.print_ufo_brand('RocKETStAR')
domodedovo.print_num_ufo()
