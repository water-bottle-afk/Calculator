__author__ = "Nadav"

""" A module for the calculator. """

from calc_config import calc_stdin, calc_stdout, calc_stderr
from parser import ExpressionParser
from exceptions import *


class Calculator:
    """ A class for the calculator.
        gets the expression (str),
        stdin, stdout, stderr.
        evaluates the expression and returns the result.
        """

    def __init__(self, exercise: str,
                 stdin=calc_stdin,
                 stdout=calc_stdout,
                 stderr=calc_stderr):

        self.exercise = exercise
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.parser = ExpressionParser(self.exercise)
        self.expression = self.parser.parse_to_expression()


    def calculate(self):
        return self.expression.evaluate()

