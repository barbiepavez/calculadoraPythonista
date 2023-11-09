import math
import unittest

# Función que calcula la tangente de un ángulo utilizando math.tan
def tangent(a):
    return math.tan(a)

# Define una clase de prueba para la función 'tangent'
class TestTangentFunction(unittest.TestCase):

    def test_tangent_positive(self):
        result = tangent(0.5)  # Calcular la tangente de 0.5 radianes
        expected = math.tan(0.5)  # Calcular el valor esperado utilizando math.tan
        self.assertAlmostEqual(result, expected, places=5)

    def test_tangent_negative(self):
        result = tangent(-0.5)  # Calcular la tangente de -0.5 radianes
        expected = math.tan(-0.5)  # Calcular el valor esperado utilizando math.tan
        self.assertAlmostEqual(result, expected, places=5)

    def test_tangent_zero(self):
        result = tangent(0)  # Calcular la tangente de 0 radianes
        expected = math.tan(0)  # La tangente de 0 radianes debe ser 0
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
