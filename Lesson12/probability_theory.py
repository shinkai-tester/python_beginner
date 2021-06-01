import random
n = int(input())
fav_digits = list(map(int, input().split()))

for d in fav_digits:
    if d not in range(0, n):
        raise Exception('Given digit %d is not in range  from 0 to n' % d)

theory = round(len(fav_digits) / n * 1000000)
print(theory)

fact = 0
for i in range(1000000):
    if random.randint(0, n-1) in fav_digits:
        fact += 1

print(fact)
