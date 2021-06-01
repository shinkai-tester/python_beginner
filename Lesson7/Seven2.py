text = input()
text = ''.join([text[i] for i in range(len(text)) if i % 2 == 0 or ord(text[i]) in range(1040, 1072)])
print(text)
