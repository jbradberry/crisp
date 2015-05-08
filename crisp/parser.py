from rpython.rlib import rstring


def tokenize(program):
    program = rstring.replace(program, '(', ' ( ')
    program = rstring.replace(program, ')', ' ) ')
    return rstring.split(program)
