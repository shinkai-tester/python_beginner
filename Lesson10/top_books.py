import operator
interviewees = int(input())
number_books = int(input())
top_listik = {}
top_bukovka = {}
final_listik = {}
final_bukovka = {}

for i in range(interviewees * number_books):
    book_name, uvlek, smysl, kach, orig = input().split()
    value_list = int(kach) * 10 + int(orig) * 10 + int(smysl) + int(uvlek)
    value_buk = int(uvlek) * 3 + int(smysl) * 3 + int(kach) + int(orig)
    top_listik[book_name] = top_listik.get(book_name, 0) + value_list
    top_bukovka[book_name] = top_bukovka.get(book_name, 0) + value_buk

sorted_top_listik = sorted(top_listik, key=lambda x: (-top_listik[x], x))
sorted_top_bukovka = sorted(top_bukovka, key=lambda x: (-top_bukovka[x], x))

for a in sorted_top_listik:
    final_listik[a] = sorted_top_listik.index(a) + 1

for b in sorted_top_bukovka:
    final_bukovka[b] = sorted_top_bukovka.index(b) + 1

result = dict(final_listik.items() & final_bukovka.items())
sorted_result = dict(sorted(result.items(), key=operator.itemgetter(1)))

for key, value in sorted_result.items():
    print(key, value)
