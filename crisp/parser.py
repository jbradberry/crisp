from rpython.rlib import rstring


def tokenize(s):
    s = rstring.replace(s, '(', ' ( ')
    s = rstring.replace(s, ')', ' ) ')
    return rstring.split(s)


class Node(object):
    pass


class Atom(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Atom('%s')" % self.value


class List(Node):
    def __init__(self, children):
        self.children = children

    def __repr__(self):
        return "List(%s)" % (','.join(self.children))


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
        return Atom(token)


def parse(program):
    return build_ast(tokenize(program))
