"""Pruebas unitarias de la calculadora."""
import unittest

from aritmeticas import division, multiplicacion, resta, suma
from porcentaje import porcentaje


class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(10, 4), 6)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 4), 12)

    def test_division(self):
        self.assertEqual(division(9, 3), 3)

    def test_division_entre_cero(self):
        with self.assertRaises(ValueError):
            division(5, 0)

    def test_porcentaje(self):
        self.assertEqual(porcentaje(200, 15), 30)


if __name__ == "__main__":
    unittest.main()
