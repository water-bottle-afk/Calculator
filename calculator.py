__author__ = "Nadav"

""" A module for the calculator. """

from calc_config import calc_stdin, calc_stdout, calc_stderr
from parser import ParserToBinaryExpression
from exceptions import *


class Calculator:
    """ A class for the calculator.
        gets the expression (str),
        stdin, stdout, stderr.
        evalues the expression and returns the result.
        """


    def __init__(self, expression: str,
                 stdin=calc_stdin,
                 stdout=calc_stdout,
                 stderr=calc_stderr):

        self.expression = expression
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr

    def calculate(self):
        try:
            expression = ParserToBinaryExpression(self.expression).parse_to_expression()
            return expression.evaluate()

        except InvalidBinaryExpression as e:
            ...

        except Exception as e:
            print(f"generic error {e}")
