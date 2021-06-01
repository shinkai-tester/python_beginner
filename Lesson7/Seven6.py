text = input()
new_text = []
for word in text.split():
    new_text.insert(0, word)
print(' '.join(new_text))
