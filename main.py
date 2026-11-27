__author__ = "Nadav"
""" A main module. """
from operators import Add, Operand
from parser import *

if __name__ == "__main__":
    parser = ExpressionParser("3.23+5*2")
    print(parser.parse_to_expression())
