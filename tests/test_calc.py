import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_seccess(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_removal_seccess(self):
        assert self.calc.subtraction(self, 10, 4) == 6

    def test_multiple_seccess(self):
        assert self.calc.multiply(self, 3, 4) == 12

    def test_power_seccess(self):
        assert self.calc.power(self, 5, 2) == 25

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)


    def teardown(self):  # Используется для обозначения конца работы функции и перехода к следующей
        print("Выполняю teardown")
