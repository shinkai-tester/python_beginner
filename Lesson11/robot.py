class Robot:

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.next = None
        self.messages = []


class RobotList:

    def __init__(self, name, identifier):
        self.first = Robot(name, identifier)
        self.current = self.first
        self.last = self.first

    def next(self):
        self.current = self.current.next

    def reset(self):
        self.current = self.first

    def new(self, name, identifier):
        tmp = Robot(name, identifier)
        self.last.next = tmp
        self.last = tmp

    def send_message(self, identifier, message):
        self.reset()
        while self.current is not None:
            if self.current.identifier == identifier:
                self.current.messages.append(message)
                break
            self.next()

    def read_messages(self, identifier):
        self.reset()
        while self.current is not None:
            if self.current.identifier == identifier:
                print(self.current.messages)
                break
            self.next()

    def printLL(self):
        self.current = self.first
        while self.current:
            print(self.current.name)
            self.current = self.current.next


rl = RobotList('Main', 1)
rl.new('Степан', 71771)
rl.new('Африкан', 7383727829237)
rl.send_message(7383727829237, 'Африкан, вернись')
rl.send_message(7383727829237, 'Я все прощу!')
rl.read_messages(7383727829237)
rl.new('Кукумбер', 11)
rl.send_message(11, 'Соленый огурец!')
rl.read_messages(71771)
rl.read_messages(11)
rl.read_messages(7383727829237)
rl.printLL()
