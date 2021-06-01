import re

words_number = int(input())
translator = {}

for i in range(words_number):
    new_lang, old_lang = input().split()
    translator[new_lang] = old_lang
text = input()
for k, v in translator.items():
    text = re.sub(r'\b' + k + r'\b', v, text, flags=re.IGNORECASE)
print(text)
