__author__ = "Nadav"

import sys
from typing import Tuple

from abstract_classes import ExpressionElement, Operator, UnaryOperator
from operators import *
from calc_config import *
from exceptions import *


class ExpressionParser:
    """
    A binary expression parser. A binary expression is an expression
    which is written with parentheses '()'.
    A class for parsing a string into a binary expression
    For example: '2+3*5' would become Add(2, Multiply(3, 5))
    """

    def __init__(self, exercise: str):
        self.exercise = exercise
        self.separated_by_symbols = []

        self.classes_symbols = {
            Add: ADD_SYMBOL,
            Subtract: SUBTRACT_SYMBOL,
            Multiply: MULTIPLY_SYMBOL,
            Divide: DIVIDE_PRIORITY
        }

    def get_all_symbols(self) -> list:
        """ Returns a list of all of the symbols """
        symbols = []
        return list(set(list(self.classes_symbols.values())))

    def parse_to_expression(self) -> ExpressionElement:
        """ Returns the parsed expression """

        self.separated_by_symbols = self.separate_exercise_by_symbols()

        while len(self.separated_by_symbols) > 1:
            # find highest priority operator
            symbol, index = self.find_highest_priority_operator()
            if symbol is None:
                raise InvalidExpressionError('No symbol found')

            # create a new expression
            new_element_expression = self.create_operator_by_symbol(symbol, index)
            if new_element_expression is None:
                raise InvalidExpressionError('No expression found')

            # replace it with the current elements
            self.replace_elements_with_an_operator(new_element_expression, index)

        return self.separated_by_symbols[0]

    def create_operator_by_symbol(self, symbol: str, index: int) -> Operator:
        """ Singleton for creating the expression element by symbol"""

        for cls, cls_symbol in self.classes_symbols.items():
            if symbol == cls_symbol:
                relative_expression_elements_index = cls.relative_expression_indexes
                elements = [self.separated_by_symbols[index + relative_index]
                            for relative_index in relative_expression_elements_index]
                return cls(*elements)

        return None

    def replace_elements_with_an_operator(self,
                                          new_expression: Operator,
                                          symbol_index: int):

        """ Replaces the elements in the separated list with the new expression element """
        elements_poped = 0
        self.separated_by_symbols[symbol_index] = new_expression
        for relative_index in type(new_expression).relative_expression_indexes:
            self.separated_by_symbols.pop(symbol_index+relative_index)
            elements_poped += 1


    def separate_exercise_by_symbols(self) -> list:
        """ Returns a list of the exercises separated by symbols
            for example: 3+5*2 will result
            [Operand(3),'+',Operand(5),'*',Operand(2)]"""

        buffer = ''
        separated = []
        symbols = self.get_all_symbols()

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

    def find_highest_priority_operator(self):
        """ Returns the index of the highest priority symbol in exercise """

        priority_values = sorted(list(priorities.keys()), reverse=True)

        for priority in priority_values:  # From highest Priority to lowest
            symbol, index = self.symbol_from_list_in_exercise(priorities[priority])
            if symbol != '':
                return symbol, index

        return None, None

    def symbol_from_list_in_exercise(self, symbols_list: list) -> Tuple[str, int]:
        """ Gets a list of symbols, returns the symbol and its index in the exercise """
        for symbol in symbols_list:
            if symbol in self.separated_by_symbols:
                return symbol, self.separated_by_symbols.index(symbol)

        return '', -1
