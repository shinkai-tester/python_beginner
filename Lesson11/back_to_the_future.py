class Stack:

    def __init__(self):
        self.stack = []
        self.less_than = []
        self.before_return = []

    def can_i_return(self, index):
        if self.stack[index] == self.stack[-1]:
            self.stack.remove(self.stack[index])
            return True
        else:
            self.before_return = self.stack[index+1:]
            return False

    def ret_from_past(self, index):
        if self.can_i_return(index):
            print('Отправка успешно совершена.')
        else:
            print('Полет запрещен – после Вас есть еще следующие путешественники:', self.before_return)

    def can_i_go_to_past(self, num):
        if len(self.stack) == 0:
            self.stack.append(num)
            return True
        stack_no_neg = self.stack.copy()
        stack_no_neg = [x for x in stack_no_neg if x >= 0]
        if all(i > num for i in stack_no_neg):
            self.stack.append(num)
            return True
        else:
            self.less_than = list(filter(lambda x: x >= 0, [i for i in self.stack if i <= num]))
            return False

    def go_to_past(self, num):
        if self.can_i_go_to_past(num):
            print('Отправка успешно совершена.')
        else:
            print(
                f'Полет запрещен – перед Вами есть люди, которые должны прилететь через {self.less_than}. Полет '
                f'рекомендуется выполнить на %d дней.' % ((self.less_than[-1]) - 1))

    def new_day(self):
        self.stack = [x - 1 for x in self.stack]


command = input()
s = Stack()
while command != 'Stop':
    command = command.split()
    if command[0] == 'Прошлое':
        s.go_to_past(int(command[1]))
    elif command[0] == 'Настоящее':
        s.ret_from_past(int(command[1]))
    elif command[0] == 'Новый':
        s.new_day()
    command = input()
