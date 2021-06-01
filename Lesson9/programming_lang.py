N = int(input())
lang = set(input().split())
one = set(lang)
alll = set(lang)
for i in range(N - 1):
    lang = set(input().split())
    one |= lang
    alll &= lang

print(alll)
print(one)