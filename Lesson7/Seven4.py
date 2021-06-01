text = input()
print(' '.join([word for word in text.split() if word.lower() != word.lower()[::-1] or len(word) == 1]))
