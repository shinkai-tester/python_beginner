text = input()
new_text = []
for word in text.split():
    if word.lower() != word.lower()[::-1] or len(word) == 1:
        new_text.append(word)
print(' '.join(new_text))