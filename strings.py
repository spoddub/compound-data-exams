def cons(a, b):
    return a + '\0' + b


def car(pair):
    return pair[:pair.index('\0')]


def cdr(pair):
    return pair[pair.index('\0')+1:]
