from rpython.rlib import rstring


def tokenize(s):
    s = rstring.replace(s, '(', ' ( ')
    s = rstring.replace(s, ')', ' ) ')
    return rstring.split(s)


class Node(object):
    pass


class Int(Node):
    def __init__(self, value):
        self.value = value

    def render(self):
        return "Int(%d)" % self.value


class Float(Node):
    def __init__(self, value):
        self.value = value

    def render(self):
        return "Float(%f)" % self.value


class Symbol(Node):
    def __init__(self, value):
        self.value = value

    def render(self):
        return "Symbol(%s)" % self.value


def dispatch_atom(value):
    try:
        int_value = int(value)
        return Int(int_value)
    except:
        pass

    try:
        float_value = float(value)
        return Float(float_value)
    except:
        pass

    return Symbol(value)


class List(Node):
    def __init__(self, children):
        self.children = children

    def render(self):
        values = [node.render() for node in self.children]
        return "List(%s)" % (', '.join(values))


def build_ast(tokens):
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(build_ast(tokens))
        tokens.pop(0)  # pop off ')'
        return List(L)
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return dispatch_atom(token)


def parse(program):
    return build_ast(tokenize(program))
