import sys

def str_from_terminal():
    string_argv = ''
    for i in sys.argv:
        if i!=sys.argv[0]:
            string_argv += i + ' '
    return string_argv