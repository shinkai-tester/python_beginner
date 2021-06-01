try:
    f = open('f.txt', 'r')
except FileNotFoundError:
    f = open('f.txt', 'w')
else:
    text = f.read()
    print(text)
finally:
    f.close()
