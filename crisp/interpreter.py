

def hailstone(number):
    if number & 1:
        return 3 * number + 1
    else:
        return number / 2


def interpret(program):
    value = int(program.split('\n')[0])
    print value
    while value != 1:
        value = hailstone(value)
        print value
