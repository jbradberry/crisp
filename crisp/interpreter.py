from . import parser


def interpret(program):
    print parser.parse(program)
