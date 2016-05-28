def if_(cond, iftrue, iffalse):
    if interpret(cond):
        return interpret(iftrue)
    else:
        return interpret(iffalse)


def interpret(val):
    if isinstance(val, tuple):
        return interpret_s(val)
    else:
        return val


def interpret_s(s_expression):
    command, tail = s_expression[0], s_expression[1:]
    return command(*map(interpret, tail))

