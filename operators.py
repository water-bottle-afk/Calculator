__author__ = "Nadav"

from abstract_classes import BinaryOperator, ExpressionElement

class Add(BinaryOperator):
    """ An Add operator (+).
        It's a binary operator with two operands.
        For Example: Add(3,5) represents 3+5."""

    symbol = "+"

    def __init__(self, expression_1:ExpressionElement , expression_2:ExpressionElement):
        super().__init__(Add.symbol, expression_1, expression_2)


    def evaluate(self):
        """ Returns the evaluation of this operator """
        return self.expression_1.evalue() + self.expression_2.evalue()


class Subtract(BinaryOperator):
    """ A Subtract operator (-).
        It's a binary operator with two operands.
        For Example: Subtract(3,5) represents 3-5."""

    symbol = "-"

    def __init__(self, expression_1:ExpressionElement , expression_2:ExpressionElement):
        super().__init__(Add.symbol, expression_1, expression_2)


    def evaluate(self):
        """ Returns the evaluation of this operator """
        return self.expression_1.evalue() - self.expression_2.evalue()


class Multiply(BinaryOperator):
    """ A Multiply operator (*).
        It's a binary operator with two operands.
        For Example: Multiply(3,5) represents 3*5."""

    symbol = "*"

    def __init__(self, expression_1:ExpressionElement , expression_2:ExpressionElement):
        super().__init__(Add.symbol, expression_1, expression_2)


    def evaluate(self):
        """ Returns the evaluation of this operator """
        return self.expression_1.evalue() * self.expression_2.evalue()


class Divide(BinaryOperator):
    """ A Divide operator (/).
        It's a binary operator with two operands.
        For Example: Divide(3,5) represents 3/5."""

    symbol = "/"

    def __init__(self, expression_1:ExpressionElement , expression_2:ExpressionElement):
        super().__init__(Add.symbol, expression_1, expression_2)


    def evaluate(self):
        """ Returns the evaluation of this operator """
        return self.expression_1.evalue() / self.expression_2.evalue()

