import unittest
from random import randint
from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_binary_to_integer(self):
        self.assertEqual(Calculator.binary_to_integer("0"), 0)
        self.assertEqual(Calculator.binary_to_integer("11"), 3)
        self.assertEqual(Calculator.binary_to_integer("1101"), 13)
        self.assertEqual(Calculator.binary_to_integer("100001"), 33)

    def test_calculate_sum_area(self):
        calc = Calculator(3)
        calc.calculate_sum_area()
        self.assertEqual(calc.serializer.sum_areas, 12)

        calc = Calculator(13)
        calc.calculate_sum_area()
        self.assertEqual(calc.serializer.sum_areas, 230)

        calc = Calculator(33)
        calc.calculate_sum_area()
        self.assertEqual(calc.serializer.sum_areas, 1482)

    def test_update_figures(self):
        calc = Calculator(5)
        self.assertEqual(calc.serializer.sum_areas, 0)

        calc.update_figures(2)
        self.assertEqual(calc.serializer.sum_areas, 0)

        calc.calculate_sum_area()
        self.assertEqual(calc.serializer.sum_areas, 5)

        calc.update_figures(10)
        self.assertEqual(calc.serializer.sum_areas, 136)

    def test_restore(self):
        calc = Calculator(randint(0, 100))
        calc.calculate_sum_area()
        start_value = calc.serializer.sum_areas
        calc.save()
        calc.update_figures(randint(0, 100))
        calc.restore()
        self.assertEqual(start_value, calc.serializer.sum_areas)


if __name__ == "__main__":
    unittest.main()
