__author__ = "Nadav"

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

    def get_priority(self) -> int:
        """ Returns the priority of the operator. """

        for priority, symbols in priority_of_symbols.items():
            if self.operator_symbol in symbols:
                return priority

        return 0 # TODO check if its ok to leave it or should handle here Invalid Input.



    def is_prior_to(self, other: Operator) -> bool:
        return priority_of_symbols[self.operator_symbol] > \
                priority_of_symbols[other.operator_symbol]


class BinaryOperator(ABC, Operator):
    """ A class for representing a binary operator.
        A binary operator has its symbol, and two expression elements. """

    def __init__(self, operator_symbol, expression_1: ExpressionElement,
                 expression_2: ExpressionElement):

        super().__init__(operator_symbol)
        self.expression_1 = expression_1
        self.expression_2 = expression_2

        self.has_right_expression = True
        self.has_left_expression = True

    def __str__(self) -> str:
        """ A string representation. """
        return f"({self.operand1} {self.operator_symbol} {self.operand2})"

class UnaryOperator(ABC, Operator):
    """ A class for representing a unary operator."""

    def __init__(self, operator_symbol, expression: ExpressionElement,
                 has_right_expression: bool, has_left_expression: bool):

        super().__init__(operator_symbol)
        self.expression = expression
        self.has_right_expression = has_right_expression
        self.has_left_expression = has_left_expression


    def __str__(self) -> str:
        """ A string representation. """
        if self.has_right_expression:
            return f"({self.operator_symbol} {self.expression})"

        return f"({self.expression} {self.operator_symbol})"

