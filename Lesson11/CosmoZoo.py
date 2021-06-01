class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *lst):
        lst = list(lst)
        lst_copy = self.lst.copy()
        lst_copy.extend(lst)
        self.lst = lst_copy.copy()
        total = 0
        portion = 0
        for i in range(0, len(lst_copy)):
            total = total + lst_copy[i]
            portion += 1
            if total >= 100:
                print('На обработку отправлено %d порций. Их пищевая ценность: %d калорий.' % (portion, total))
                del self.lst[:portion]
                total = 0
                portion = 0

    def get_current_part(self):
        return self.lst


buf = Buffer()
print(buf.get_current_part())
buf.add(10, 10, 10)
print(buf.get_current_part())
buf.add(69, 1)
buf.add(101)
print(buf.get_current_part())
buf.add(101, 101, 1, 10, 100, 11, 10)
print(buf.get_current_part())
