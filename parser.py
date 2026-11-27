__author__ = "Nadav"

import sys
from typing import Tuple

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

    def parse_to_expression(self) -> list[ExpressionElement]:
        """ Returns the parsed expression """

        separated = self.separate_exercise_by_symbols()

        return separated

    def separate_exercise_by_symbols(self) -> list:
        """ Returns a list of the exercises separated by symbols
            for example: 3+5*2 will result
            [Operand(3),'+',Operand(5),'*',Operand(2)]"""

        buffer = ''
        separated = []
        symbols = ExpressionParser.get_all_symbols()

        for ch in self.exercise:
            if ch not in symbols:
                buffer += ch
            else:
                separated.append(Operand(buffer))
                separated.append(ch)
                buffer = ''

        if buffer != '':
            separated.append(Operand(buffer))

        return separated


    @staticmethod
    def get_all_symbols():
        symbols = []
        for values in priorities.values():
            for value in values:
                symbols.append(value)

        return symbols

    def parse_exercise_to_list_of_elements(self):
        ...

    def parse_exercise_by_symbol(self, symbol: str, index_of_symbol: int) -> list:
        ...

    def find_index_of_closest_symbol(self, index: int = -1, start_search_from_right: bool = True):
        """ Returns a the index of closet symbols.
            to check from After the symbol -> search from right = True,
            to check from Before the symbol -> search from right = False.
            if not found a symbol returns None.
            """

        # Gathering the symbols

        symbols = ExpressionParser.get_all_symbols()

        closest_index = -1
        end = len(self.exercise) if start_search_from_right else 0
        step = 1 if start_search_from_right else -1
        for i in range(index, end, step):
            if i != index and self.exercise[i] in symbols:
                return i

        return None

    def find_highest_priority_operator(self):
        """ Returns the index of the highest priority symbol in exercise """

        priorities_keys = sorted(list(priorities.keys()), reverse=True)

        for priority in priorities_keys:  # From highest Priority to lowest
            symbol, idx = ExpressionParser.symbol_from_list_in_exercise(self.exercise, priorities[priority])
            if symbol != '':
                pass

        return None

    @staticmethod
    def symbol_from_list_in_exercise(exercise: str, symbols_list: list) -> Tuple[str, int]:
        """ Gets a list of symbols, returns the symbol and its index in the exercise """
        for symbol in symbols_list:
            if symbol in exercise:
                return symbol, exercise.index(symbol)

        return '', -1

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
