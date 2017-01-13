from rply import LexerGenerator


lg = LexerGenerator()

lg.add('LPAREN', '\(')
lg.add('RPAREN', '\)')
lg.add('FLOAT', '-?\d+\.\d+')
lg.add('INTEGER', '-?\d+')
lg.add('STRING', '".*?"')
lg.add('SYMBOL', '[^\s]+')

lg.ignore('\s+')

lexer = lg.build()
