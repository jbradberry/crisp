import sys
from rpython.rlib.streamio import open_file_as_stream
from rpython.jit.codewriter.policy import JitPolicy


def main(argv):
    print "Hello, world!"
    return 0


def target(driver, args):
    return main, None


def jitpolity(driver):
    return JitPolicy()


if __name__ == '__main__':
    main(sys.argv)
