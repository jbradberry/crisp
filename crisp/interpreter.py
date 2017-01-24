from . import lexer, parser


def interpret(program):
    ast = parser.parser.parse(lexer.lexer.lex(program))
    print ast.eval()
