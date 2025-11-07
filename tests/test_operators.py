import unittest

from operators import add, subtract, multiply, divide


class TestOperators(unittest.TestCase):
	"""Tests unitaires pour les fonctions du module operators.py"""

	def test_add_positive(self):
		"""Vérifie que l'addition de deux nombres positifs renvoie le bon résultat."""
		self.assertEqual(add(2, 3), 5)

	def test_add_negative(self):
		"""Vérifie que l'addition de deux nombres négatifs renvoie le bon résultat."""
		self.assertEqual(add(-1, -1), -2)

	def test_subtract_positive(self):
		"""Vérifie que la soustraction entre deux nombres positifs renvoie le bon résultat."""
		self.assertEqual(subtract(5, 3), 2)

	def test_subtract_negative(self):
		"""Vérifie que la soustraction entre deux nombres négatifs renvoie le bon résultat."""
		self.assertEqual(subtract(-1, -2), 1)

	def test_multiply_positive(self):
		"""Vérifie que la multiplication de deux nombres positifs est correcte."""
		self.assertEqual(multiply(2, 3), 6)

	def test_multiply_by_zero(self):
		"""Vérifie que toute multiplication par zéro renvoie zéro."""
		self.assertEqual(multiply(5, 0), 0)

	def test_multiply_negative(self):
		"""Vérifie que la multiplication de deux nombres négatifs renvoie un résultat positif."""
		self.assertEqual(multiply(-2, -3), 6)

	def test_divide_positive(self):
		"""Vérifie que la division entre deux nombres positifs renvoie le bon quotient."""
		self.assertEqual(divide(7, 2), 3.5)

	def test_divide_negative(self):
		"""Vérifie que la division entre deux nombres négatifs renvoie un résultat positif."""
		self.assertEqual(divide(-9, -3), 3.0)

	def test_divide_by_zero(self):
		"""Vérifie qu'une division par zéro lève une erreur ZeroDivisionError."""
		with self.assertRaises(ZeroDivisionError):
			divide(1, 0)

if __name__ == "__main__":
    unittest.main()