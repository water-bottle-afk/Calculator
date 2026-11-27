__author__ = "Nadav"

from abstract_classes import BinaryOperator, ExpressionElement
from numbers import Number
from calc_config import *

class Operand(ExpressionElement):
    """
    A class for representing an Operand (Number).
    A number is an ExpressionElement.
    """

    def __init__(self, number:str):
        # A number could be int, float, etc.
        self.number = Operand.parse_from_str_to_number(number)

    @staticmethod
    def parse_from_str_to_number(buffer: str) -> int | float | None:
        try:
            return int(buffer)
        except ValueError:
            pass

        try:
            return float(buffer)
        except ValueError:
            print("Value error! The Exercise must contain numbers and symbols! ", file=calc_stderr)
            exit(1) #TODO: add error/Exception/exit values


    def evaluate(self) -> int | float:
        """ :returns the value of the number. """
        return self.number

    def __str__(self) -> str:
        """ A string representation. """
        return str(self.number)

    def __repr__(self) -> str:
        """ A string representation. """
        return str(self.number)

class Add(BinaryOperator):
    """ An Add operator (+).
        It's a binary operator with two operands.
        For Example: Add(3,5) represents 3+5."""

    symbol = "+"
    priority = 1
    relative_expression_indexes = (-1, 1)

    def __init__(self, expression_1: ExpressionElement, expression_2: ExpressionElement):
        super().__init__(Add.symbol, Add.priority, expression_1, expression_2)

    def evaluate(self) -> Number:
        """ Returns the evaluation of this operator """
        return self.expression_1.evaluate() + self.expression_2.evaluate()


class Subtract(BinaryOperator):
    """ A Subtract operator (-).
        It's a binary operator with two operands.
        For Example: Subtract(3,5) represents 3-5."""

    symbol = "-"
    priority = 1
    relative_expression_indexes = (-1, 1)

    def __init__(self, expression_1: ExpressionElement, expression_2: ExpressionElement):
        super().__init__(Subtract.symbol, Subtract.priority,
                         expression_1, expression_2)

    def evaluate(self) -> Number:
        """ Returns the evaluation of this operator """
        return self.expression_1.evaluate() - self.expression_2.evaluate()


class Multiply(BinaryOperator):
    """ A Multiply operator (*).
        It's a binary operator with two operands.
        For Example: Multiply(3,5) represents 3*5."""

    symbol = "*"
    priority = 2
    relative_expression_indexes = (-1, 1)

    def __init__(self, expression_1: ExpressionElement, expression_2: ExpressionElement):
        super().__init__(Multiply.symbol, Multiply.priority, expression_1, expression_2)

    def evaluate(self) -> Number:
        """ Returns the evaluation of this operator """
        return self.expression_1.evaluate() * self.expression_2.evaluate()


class Divide(BinaryOperator):
    """ A Divide operator (/).
        It's a binary operator with two operands.
        For Example: Divide(3,5) represents 3/5."""

    symbol = "/"
    priority = 2
    relative_expression_indexes = (-1, 1)

    def __init__(self, expression_1: ExpressionElement, expression_2: ExpressionElement):
        super().__init__(Divide.symbol, Divide.priority, expression_1, expression_2)

    def evaluate(self) -> Number:
        """ Returns the evaluation of this operator """
        return self.expression_1.evaluate() / self.expression_2.evaluate()
