import tkinter as tk


class Calc:

    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title('Hi')
        self.tk.configure(background="LightSkyBlue1")
        self.tk.geometry("200x130")
        self.label = tk.Label(self.tk, text="I'm happy to see you ٩(◕‿◕｡)۶")
        self.label.pack(side="top", fill="both")
        self.ent1 = tk.Entry(bg='mint cream')
        self.ent1.pack()
        self.b = tk.Button(text='Result', width=15, height=3, bg='lavender', command=self.calc)
        self.b.pack()
        self.ent2 = tk.Entry(bg='mint cream')
        self.ent2.pack()
        self.tk.mainloop()

    def calc(self):
        vir = self.ent1.get().split()
        res = 'Unknown'
        if vir[1] == '-':
            res = int(vir[0]) - int(vir[2])
        elif vir[1] == '+':
            res = int(vir[0]) + int(vir[2])
        self.ent2.delete(0, tk.END)
        self.ent2.insert(0, (str(res)))

a = Calc()
