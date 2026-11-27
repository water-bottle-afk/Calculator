__author__ = "Nadav"

""" A module for exceptions. """

class InvalidExpressionError(Exception):
    def __init__(self, message: str = ""):
        self.message = message

    def __str__(self) -> str:
        f"""Invalid Expression!"""
