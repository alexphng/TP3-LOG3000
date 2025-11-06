import unittest
from app import calculate

class TestCalculate(unittest.TestCase):
    """Tests unitaires pour la fonction calculate du module app.py"""

    def test_addition(self):
        self.assertEqual(calculate("3+2"), 5)

    def test_subtraction(self):
        self.assertEqual(calculate("10-4"), 6)

    def test_multiplication(self):
        self.assertEqual(calculate("3*3"), 9)

    def test_division(self):
        self.assertEqual(calculate("9/2"), 4.5)

    def test_invalid_expression_format(self):
        with self.assertRaises(ValueError):
            calculate("+3")

    def test_multiple_operators(self):
        with self.assertRaises(ValueError):
            calculate("3+2-1")

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            calculate("a+3")

if __name__ == "__main__":
    unittest.main()