__author__ = "Nadav"
""" A main module. """

from calculator import Calculator

if __name__ == "__main__":
    calculator = Calculator("1+2*2/4+5-2*3")
    print(f"{calculator.exercise} = {calculator.calculate()}")
