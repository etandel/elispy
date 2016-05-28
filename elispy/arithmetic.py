from functools import reduce
import operator


def build_arithmetic_op(name, func):
    def op(*args):
        return reduce(func, args)
    op.__name__ = name
    return op


add = build_arithmetic_op('add', operator.add)
sub = build_arithmetic_op('sub', operator.sub)
mul = build_arithmetic_op('mul', operator.mul)
div = build_arithmetic_op('div', operator.truediv)
mod = operator.mod
