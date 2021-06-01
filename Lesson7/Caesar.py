string = input()
string = string.lower()
sdv = int(input())
s = ''
for c in string:
    if 'а' <= c <= 'я':
        ot_sm = ord(c) - ord('а')
        new_ot_sm = (ot_sm + sdv) % 32
        abs_sm = ord('а') + new_ot_sm
        c = chr(abs_sm)
    s += c
print(s)
