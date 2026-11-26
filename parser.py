__author__ = "Nadav"

from abstract_classes import ExpressionElement, Operator, UnaryOperator
from operators import *
from calc_config import *


class ExpressionParser:
    """
    A binary expression parser. A binary expression is an expression
    which is written with parentheses '()'.
    A class for parsing a string into a binary expression
    For example: '2+3*5' would become Add(2, Multiply(3, 5))
    """

    def __init__(self, exercise: str):
        self.exercise = exercise
        self.lst_exercise = []

    def parse_to_expression(self) -> ExpressionElement:
        """ Returns the parsed expression """

        # Starting from left to right

        while len(self.exercise) > 1:
            highest_priority_place = self.get_idx_of_highest_operator()

        return self.exercise[0]

    def get_idx_of_highest_operator(self) -> int:
        """ Returns the index of the highest priority symbol in exercise """
        for priority, symbols in self.sort_priority_of_symbols():
            for symbol in symbols:
                if symbol in self.exercise:
                    return priority

    def sort_priority_of_symbols(self):
        items = set(Operator.priority_of_symbols.values()).copy()
        items = list(items)
        items.sort(key=Operator.priority_of_symbols.keys(), reverse=True)

    def create_expression_by_symbol(self, symbol: str, index_of_symbol: int) -> ExpressionElement:
        """ Singleton to create an expression by symbol """
        cls = elements_by_symbol[symbol]

        if issubclass(cls, BinaryOperator):
            expression_1 = self.lst_exercise[index_of_symbol - 1]
            expression_2 = self.lst_exercise[index_of_symbol + 1]

            self.remove_expressions_from_exercise(cls, index_of_symbol)

            return cls(expression_1, expression_2)

        if issubclass(cls, UnaryOperator):

            if cls.has_right_expression():
                expression_1 = self.lst_exercise[index_of_symbol + 1]
                return cls(expression_1)
            else:
                expression_1 = self.lst_exercise[index_of_symbol - 1]
                return cls(expression_1)

        return None


def remove_expressions_from_exercise(self, cls, index_of_symbol: int):
    if issubclass(cls, BinaryOperator):
        del self.lst_exercise[index_of_symbol]
        del self.lst_exercise[index_of_symbol]
        del self.lst_exercise[index_of_symbol]


def func(self):
    # dict:
    # (symbol, priority) : [relative_expression_indexes]
    self.relative_expression_indexes = {
        (Add.symbol, Add.priority): Add.relative_expression_indexes,
        (Subtract.symbol, Subtract.priority): Subtract.relative_expression_indexes,
        (Multiply.symbol, Multiply.priority): Multiply.relative_expression_indexes,
        (Divide.symbol, Divide.priority): Divide.relative_expression_indexes}
