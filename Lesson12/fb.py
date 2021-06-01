import pickle


class ToWrite:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


#    def __repr__(self):
#        return str(self.p1) + ' ' + str(self.p2)

# a = ToWrite(1, 2)

with open('f.pickle', 'rb') as f:
    b = pickle.load(f)
print(b)
