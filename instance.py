def cons(a, b):
    return 2 ** a * 3 ** b


def car(pair):
    a = 0
    while pair % 2 == 0:
        pair //= 2
        a += 1
    return a


def cdr(pair):
    b = 0
    while pair % 3 == 0:
        pair //= 3
        b += 1
    return b
