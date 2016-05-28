import operator
from functools import reduce
from operator import (mod,
                      lt, le, gt, ge, eq, ne,
                      not_, and_, or_)


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


def build_arithmetic_op(name, func):
    def op(*args):
        return reduce(func, args)
    op.__name__ = name
    return op


add = build_arithmetic_op('add', operator.add)
sub = build_arithmetic_op('sub', operator.sub)
mul = build_arithmetic_op('mul', operator.mul)
div = build_arithmetic_op('div', operator.truediv)


def if_(cond, iftrue, iffalse):
    if interpret(cond):
        return interpret(iftrue)
    else:
        return interpret(iffalse)


LEXICON = {}


def interpret(val):
    if isinstance(val, tuple):
        return interpret_s(val)
    else:
        return val


def interpret_s(s_expression):
    command, tail = s_expression[0], s_expression[1:]
    return command(*map(interpret, tail))

