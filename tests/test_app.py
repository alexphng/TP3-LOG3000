import unittest
from app import calculate

class TestCalculate(unittest.TestCase):
    """Tests unitaires pour la fonction calculate du module app.py"""

    def test_addition(self):
        """Vérifie que l'addition donne le bon résultat"""
        self.assertEqual(calculate("3+2"), 5)

    def test_subtraction(self):
        """Vérifie que la soustraction donne le bon résultat"""
        self.assertEqual(calculate("10-4"), 6)

    def test_multiplication(self):
        """Vérifie que la multiplication renvoie le bon résultat."""
        self.assertEqual(calculate("3*3"), 9)

    def test_division(self):
        """Vérifie que la division renvoie le bon résultat avec des nombres réels."""
        self.assertEqual(calculate("9/2"), 4.5)

    def test_invalid_expression_format(self):
        """Vérifie qu'une expression mal formée (ex: +3) déclenche une erreur."""
        with self.assertRaises(ValueError):
            calculate("+3")

    def test_multiple_operators(self):
        """Vérifie qu'une expression avec plusieurs opérateurs déclenche une erreur."""
        with self.assertRaises(ValueError):
            calculate("3+2-1")

    def test_invalid_number(self):
        """Vérifie qu'une expression avec des caractères non numériques déclenche une erreur."""
        with self.assertRaises(ValueError):
            calculate("a+3")

if __name__ == "__main__":
    unittest.main()