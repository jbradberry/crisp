from rply.token import BaseBox
from rply import ParserGenerator

from .lexer import lexer


class Atom(BaseBox):
    pass


class Int(Atom):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return "Int<%d>" % self.value


class Float(Atom):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return "Float<%f>" % self.value


class String(Atom):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return "String<'%s'>" % self.value


class Symbol(Atom):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return "Symbol<%s>" % self.value


class List(BaseBox):
    def __init__(self, children):
        self.children = children

    def eval(self):
        return "[%s]" % " ".join([item.eval() for item in self.contents()])

    def contents(self):
        return self.children


pg = ParserGenerator(
    ['LPAREN', 'RPAREN', 'FLOAT', 'INTEGER', 'STRING', 'SYMBOL'],
)


@pg.production('expression : FLOAT')
def expression_float(p):
    return Float(float(p[0].getstr()))


@pg.production('expression : INTEGER')
def expression_integer(p):
    return Int(int(p[0].getstr()))


@pg.production('expression : STRING')
def expression_string(p):
    return String(str(p[0].getstr()))


@pg.production('expression : SYMBOL')
def expression_symbol(p):
    return Symbol(str(p[0].getstr()))


@pg.production('sequence :')
@pg.production('sequence : sequence expression')
def sequence(p):
    if not p:
        return List([])

    return List(p[0].contents() + [p[1]])


@pg.production('expression : LPAREN sequence RPAREN')
def expression_list(p):
    return List(p[1].contents())


parser = pg.build()
