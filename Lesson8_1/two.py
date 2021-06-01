def ret_st(a):
    s = 0
    for i in a:
        if type(i) == str:
            s += 1
    return s


def print_st(a):
    print(ret_st(a))


print_st([1, 2, 3, 'efefef', 'fefere', []])
