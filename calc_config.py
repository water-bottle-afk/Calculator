__author__ = "Nadav"


from sys import stdin, stdout, stderr

""" A module configuration. """


HIGHEST_PRIORITY = 8
LOWEST_PRIORITY = 1

ADD_SYMBOL = '+'
SUBTRACT_SYMBOL = '-'
MULTIPLY_SYMBOL = '*'
DIVIDE_SYMBOL = '/'
RIGHT_PARENTHESIS_SYMBOL = '('
LEFT_PARENTHESIS_SYMBOL = ')'

priorities = {
         HIGHEST_PRIORITY : [RIGHT_PARENTHESIS_SYMBOL, LEFT_PARENTHESIS_SYMBOL],
        LOWEST_PRIORITY+1: [MULTIPLY_SYMBOL, DIVIDE_SYMBOL],
         LOWEST_PRIORITY : [ADD_SYMBOL, SUBTRACT_SYMBOL],
     }

calc_stdin = stdin
calc_stdout = stdout
calc_stderr = stderr
