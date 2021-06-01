A = {'A': 1, 'B': 2, 'C': 3}
B = {}

for i in A:
    B[A[i]] = i

print(B)