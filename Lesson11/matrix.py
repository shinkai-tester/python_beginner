class Matrix:

    def __init__(self, mat):
        self.mat = mat

    def __add__(self, second_matrix):
        mat = [[a + b for a, b in zip(row, other_row)] for row, other_row in zip(self.mat, second_matrix.mat)]
        return Matrix(mat)

    def __repr__(self):
        self.mat = '\n'.join(' '.join(map(str, k)) for k in self.mat)
        return self.mat


n = int(input())
A = Matrix([[int(i) for i in input().split()] for k in range(n)])
B = Matrix([[int(i) for i in input().split()] for k in range(n)])
print(A + B + B)
