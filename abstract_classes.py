__author__ = "Nadav"

""" A module for the abstract classes. """

from abc import ABC, abstractmethod
from numbers import Number
from calc_config import *


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



class Operator(ExpressionElement):
    """ An Abstract class for representing an operator. """

    def __init__(self, operator_symbol: str, priority: int):
        self.operator_symbol = operator_symbol
        self.priority = priority


class BinaryOperator(Operator):
    """ A class for representing a binary operator.
        A binary operator has its symbol, and two expression elements. """

    def __init__(self, operator_symbol, priority: int,
                 expression_1: ExpressionElement,
                 expression_2: ExpressionElement):
        super().__init__(operator_symbol, priority)
        self.expression_1 = expression_1
        self.expression_2 = expression_2

    def __str__(self) -> str:
        """ A string representation. """
        return f"({self.expression_1} {self.operator_symbol} {self.expression_2})"


class UnaryOperator(Operator):
    """ A class for representing a unary operator."""

    def __init__(self, operator_symbol, expression: ExpressionElement,
                 has_right_expression: bool, has_left_expression: bool):
        super().__init__(operator_symbol)
        self.expression = expression

    def __str__(self) -> str:
        """ A string representation. """
        ...
