import pytest
from app.calc import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(5, 2) == 7

    def test_multiply_success(self):
        assert self.calc.multiply(6,6) == 36

    def test_division_success(self):
        assert self.calc.division(48,6) == 8

    def test_subtraction_success(self):
        assert self.calc.subtraction(100,6) == 94


