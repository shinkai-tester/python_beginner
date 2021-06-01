def Caesar(text, sdv):
    text = text.lower()
    s = ''
    for c in text:
        if 'а' <= c <= 'я':
            ot_sm = ord(c) - ord('а')
            new_ot_sm = (ot_sm + sdv) % 32
            abs_sm = ord('а') + new_ot_sm
            c = chr(abs_sm)
        s += c
    return s


s = Caesar(input(), int(input()))
print(s)
