from . import parser


def interpret(program):
    print parser.tokenize(program)
