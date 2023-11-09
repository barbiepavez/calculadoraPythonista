import math
import unittest

# Función que calcula el logaritmo de un número 'a' en base 'b' utilizando math.log
def logarithm(a, b):
    return math.log(a, b)

# Define una clase de prueba para la función 'logarithm'
class TestLogarithmFunction(unittest.TestCase):

    def test_logarithm_base_10(self):
        result = logarithm(100, 10)  # Calcular el logaritmo de 100 en base 10
        expected = 2.0  # El logaritmo de 100 en base 10 es 2
        self.assertAlmostEqual(result, expected, places=5)

    def test_logarithm_base_e(self):
        result = logarithm(math.e, math.e)  # Calcular el logaritmo de 'e' en base 'e'
        expected = 1.0  # El logaritmo de 'e' en base 'e' es 1
        self.assertAlmostEqual(result, expected, places=5)

    def test_logarithm_negative_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 2)  # Debe lanzar una excepción ValueError cuando se toma el logaritmo de un número negativo.

if __name__ == '__main__':
    unittest.main()
