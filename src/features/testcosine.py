import unittest
import math  # Importa el módulo math para utilizar la función math.sin.
from trig_log import cosine  # Importa la función 'sine' desde el módulo 'trig_log'.

# Define una clase llamada 'TestTrigLog' que hereda de 'unittest.TestCase' para realizar pruebas de la función 'sine'.
class TestTrigLog(unittest.TestCase):

    # Define un método de prueba llamado 'test_cosine_positive' para probar la función 'cosine' con un ángulo positivo.
    def test_cosine_positive(self):
        result = cosine(0.5)  # Calcula el coseno de 0.5 radianes utilizando la función 'cosine'.
        expected = math.cos(0.5)  # Calcula el valor esperado utilizando la función 'math.cos'.
        self.assertAlmostEqual(result, expected, places=5)  # Comprueba si el resultado y el valor esperado son aproximadamente iguales con 5 decimales de precisión.

    # Define un método de prueba llamado 'test_cosine_negative' para probar la función 'cosine' con un ángulo negativo.
    def test_cosine_negative(self):
        result = cosine(-0.5)  # Calcula el coseno de -0.5 radianes utilizando la función 'cosine'.
        expected = math.cos(-0.5)  # Calcula el valor esperado utilizando la función 'math.cos'.
        self.assertAlmostEqual(result, expected, places=5)  # Comprueba si el resultado y el valor esperado son aproximadamente iguales con 5 decimales de precisión.

    # Define un método de prueba llamado 'test_cosine_zero' para probar la función 'cosine' con un ángulo de 0 radianes.
    def test_cosine_zero(self):
        result = cosine(0)  # Calcula el coseno de 0 radianes utilizando la función 'cosine'.
        expected = math.cos(0)  # El coseno de 0 radianes debe ser 1, calculado con la función 'math.cos'.
        self.assertEqual(result, expected)  # Comprueba si el resultado es igual al valor esperado.

# Verifica si el script se ejecuta como el programa principal.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase 'TestTrigLog'.
