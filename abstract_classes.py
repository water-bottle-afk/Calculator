__author__ = "Nadav"

from abc import ABC, abstractmethod
from numbers import Number

class ExpressionElement(ABC):
    """
    Interface for representing an expression element.
    For example,
    1 is an ExpressionElement, (2+3) is too.
    """

    @abstractmethod
    def evaluate(self) -> Number:
        """ An Abstract method for evaluating the expression. """
        ...

    @abstractmethod
    def __str__(self) -> str:
        """ A string representation of the expression. """
        ...

class Operand(ExpressionElement):
    """
    A class for representing an Operand (Number).
    A number is an ExpressionElement.
    """

    def __init__(self, number):
        # A number could be int, float, etc.

        self.number = number

    def evaluate(self) -> Number:
        """ :returns the value of the number. """
        return self.number

    def __str__(self) -> str:
        """ A string representation. """
        return str(self.number)


class Operator(ABC, ExpressionElement):
    """ An Abstract class for representing an operator. """
    def __init__(self, operator_symbol):
        self.operator_symbol = operator_symbol


class BinaryOperator(ABC, Operator):
    """ A class for representing a binary operator.
        A binary operator has its symbol, and two expression elements. """

    def __init__(self, operator_symbol, expression_1: ExpressionElement,
                 expression_2: ExpressionElement):

        super().__init__(operator_symbol)
        self.expression_1 = expression_1
        self.expression_2 = expression_2

    def __str__(self) -> str:
        """ A string representation. """
        return f"({self.operand1} {self.operator_symbol} {self.operand2})"

class UnaryOperator(ABC, Operator):
    """ A class for representing a unary operator."""

    def __init__(self, operator_symbol, expression: ExpressionElement):
        super().__init__(operator_symbol)
        self.expression = expression

    def __str__(self) -> str:
        """ A string representation. """
        return f"({self.operand1} {self.operator_symbol} {self.operand2})"

