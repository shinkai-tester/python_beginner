# a = [1, 2, 3, 22, 33]
# print(list(filter(lambda x: len(str(x)) == 2, a)))
# words = input()
# words = words.split()
# words = list(filter(lambda x: len(x) % 2 == 0, words))
# words = ' '.join(list(map(lambda word: ''.join(list(map(lambda char: chr(ord(char) + 1), word))), words)))
# print(words)

print(
    ' '.join(
        map(lambda word: ''.join(
            map(lambda char: chr(ord(char) + 1), word)),
            filter(lambda x: len(x) % 2 == 0, input().split())
            )
    )
)
