def expp(a, n):
    if n == 0:
        return 1
    return expp(a, n - 1) * a


def eff_e(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return eff_e(a, n - 1) * a
    else:
        return eff_e(a, n//2) * eff_e(a, n//2)

print(eff_e(3, 3))
