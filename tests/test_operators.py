import unittest

from operators import add, subtract, multiply, divide


class TestOperators(unittest.TestCase):
	"""Tests unitaires pour les fonctions du module operators.py"""

	def test_add_positive(self):
		self.assertEqual(add(2, 3), 5)

	def test_add_negative(self):
		self.assertEqual(add(-1, -1), -2)

	def test_subtract_positive(self):
		self.assertEqual(subtract(5, 3), 2)

	def test_subtract_negative(self):
		self.assertEqual(subtract(-1, -2), 1)

	def test_multiply_positive(self):
		self.assertEqual(multiply(2, 3), 6)

	def test_multiply_by_zero(self):
		self.assertEqual(multiply(5, 0), 0)

	def test_multiply_negative(self):
		self.assertEqual(multiply(-2, -3), 6)

	def test_divide_positive(self):
		self.assertEqual(divide(7, 2), 3.5)

	def test_divide_negative(self):
		self.assertEqual(divide(-9, -3), 3.0)

	def test_divide_by_zero(self):
		with self.assertRaises(ZeroDivisionError):
			divide(1, 0)

if __name__ == "__main__":
    unittest.main()