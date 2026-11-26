__author__ = "Nadav"

""" A module for exceptions. """


class InvalidBinaryExpression(Exception):
    def __init__(self, message:str=""):
        self.message = message

    def __str__(self) -> str:
        f"""Invalid Binary Expression {': ' + self.message if self.message else ''}"""


class InvalidUnaryExpression(Exception):
    def __init__(self, message:str=""):
        self.message = message

    def __str__(self) -> str:
        f"""Invalid Unary Expression {': ' + self.message if self.message else ''}"""
