EMPTY = []


def cons(head, tail):
    return [head] + tail


def head(xs):
    if xs is EMPTY:
        raise ValueError('Cannot get head of EMPTY')
    else:
        return xs[0]


def tail(xs):
    if xs is EMPTY:
        raise ValueError('Cannot get tail of EMPTY')
    else:
        return xs[1:]

