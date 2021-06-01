Info = dict()
N = int(input())

for i in range(N):
    name, thing, num = input().split()
    num = int(num)
    if name in Info:
        Info[name][thing] = Info[name].get(thing, 0) + num
    else:
        Info[name] = dict()
        Info[name][thing] = num

for name in Info:
    print(name)
    for thing in Info[name]:
        print(thing, ': ', Info[name][thing], sep='')
    print('----------------------------------')