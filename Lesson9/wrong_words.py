import re

right_words = list('двулика например и том все скрипку мир покоя ошибку на обыкновенный '
                   'поэта текст обособлены насчет с качается сто обреченный верную поздно '
                   'любовь нам во-первых а не ноту препинания его цены счастье пробелами крах еще '
                   'двух слово юного мы ты знаем дружба сторон платить числе сотни точками запятыми в взять '
                   'улика должны заключенный за тире вновь что горем знаки я во-вторых вторых исправить '
                   'настроить быть ваш спасала образ будет могут убита но скобками забыть '
                   'знаками со веков оков петров телефон'.split())

gudwin_text = input().split()
text_no_signs = gudwin_text.copy()
bad_words = []

for word in gudwin_text:
    good_word = re.sub('^[^а-яА-Я]*|[^а-яА-я]*$', '', word).lower()
    text_no_signs = list(filter(lambda x: x != '', [w.replace(word, good_word) for w in text_no_signs]))

for i in text_no_signs:
    if i not in right_words:
        bad_words.append(i)

print(' '.join(bad_words))
