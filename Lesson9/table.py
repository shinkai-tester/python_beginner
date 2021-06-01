locs = sorted(set(input().split()))
roads = set(map(frozenset, map(lambda x: x.replace(' ', ''), input().split(','))))
directions = [i for i in roads if len(i) > 1]
coordinates_x = []
coordinates_y = []
data = [['0' for i in range(len(locs))] for k in range(len(locs))]


def Red(skk): return "\033[91m {}\033[00m".format(skk)


def Yellow(skk): return "\033[93m {}\033[00m".format(skk)


def LightPurple(skk): return "\033[94m {}\033[00m".format(skk)


for x in range(len(locs)):
    for y in range(len(locs)):
        if {locs[x], locs[y]} in directions:
            data[x][y] = '1'
        if locs[x] == locs[y]:
            data[x][y] = '2'

format_row = "{:>2}" * (len(locs) + 1)
print(format_row.format("", *locs))
for loc, row in zip(locs, data):
    for x in range(len(locs)):
        for y in range(len(locs)):
            if data[x][y] == '1':
                data[x][y] = LightPurple(data[x][y])
            if data[x][y] == '0':
                data[x][y] = Red(data[x][y])
            if data[x][y] == '2':
                data[x][y] = Yellow(data[x][y])
    print(format_row.format(loc, *row))
