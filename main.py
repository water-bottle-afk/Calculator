__author__ = "Nadav"
""" A main module. """

from parser import *

if __name__ == "__main__":
    parser = ExpressionParser("1+2*2/4+5-2*3")
    expression = parser.parse_to_expression()
    print(f"{parser.exercise} = {expression.evaluate()}")
