class FileHelper:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None
        self.text = None
        print('Вы инициализировались с файлом %s' % self.file_name)

    def read(self):
        print('Начато чтение файла %s' % self.file_name)
        try:
            self.file = open(self.file_name, 'r')
        except FileNotFoundError:
            print('Файл %s не найден' % self.file_name)
        else:
            self.text = self.file.read()
            print('Был считан следующий текст:')
            print(self.text)
            print('Чтение файла успешно закончено')
            self._close()

    def write(self, text):
        print('Начата запись в файл %s' % self.file_name)
        self.file = open(self.file_name, 'w')
        self.file.write(text)
        self.text = text
        print('Был записан следующий текст:')
        print(self.text)
        print('Запись в файл успешно закончена')
        self._close()

    def _close(self):
        print('Закрываем файл %s' % self.file_name)
        self.file.close()
        self.file = None
        print('Файл %s успешно закрыт' % self.file_name)

    def change_name(self, name):
        self.file_name = name
        self.file = None
        self.text = None
        print('Теперь вы работаете с файлом %s' % self.file_name)

    def print_current_text(self):
        if self.text is None:
            print('Попробуйте что-то записать в файл или считать из него что-то')
        else:
            print('Текущий текст это:', end=' ')
            print(self.text)


f = FileHelper('new.txt')
f.write('Some text')
f.change_name('some_file.txt')
f.write('Other text')
f.change_name('new.txt')
f.print_current_text()
f.read()
f.print_current_text()
f.change_name('h.txt')
f.read()
