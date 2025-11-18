import math
import unittest

from calculator.core import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2, places=7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertAlmostEqual(self.calc.modulo(10.5, 3), 1.5, places=7)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)

    def test_sin(self):
        self.assertAlmostEqual(self.calc.sin(0), 0, places=7)
        self.assertAlmostEqual(self.calc.sin(90), 1, places=7)
        self.assertAlmostEqual(self.calc.sin(30), 0.5, places=7)

    def test_cos(self):
        self.assertAlmostEqual(self.calc.cos(0), 1, places=7)
        self.assertAlmostEqual(self.calc.cos(90), 0, places=7)
        self.assertAlmostEqual(self.calc.cos(60), 0.5, places=7)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(2, -2), 0.25)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(0), 0)
        self.assertEqual(self.calc.sqrt(6.25), 2.5)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            self.calc.sqrt(-9)

    def test_floor(self):
        self.assertEqual(self.calc.floor(3.7), 3)
        self.assertEqual(self.calc.floor(-3.7), -4)
        self.assertEqual(self.calc.floor(5), 5)

    def test_ceil(self):
        self.assertEqual(self.calc.ceil(3.2), 4)
        self.assertEqual(self.calc.ceil(-3.2), -3)
        self.assertEqual(self.calc.ceil(5), 5)


if __name__ == "__main__":
    unittest.main()