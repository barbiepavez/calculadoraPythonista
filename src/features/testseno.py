import unittest
import math  # Importa el módulo math para utilizar la función math.sin.
from trig_log import sine  # Importa la función 'sine' desde el módulo 'trig_log'.
import unittest  # Importa el módulo unittest para realizar pruebas unitarias.

# Define una clase llamada 'TestTrigLog' que hereda de 'unittest.TestCase' para realizar pruebas de la función 'sine'.
class TestTrigLog(unittest.TestCase):

    # Define un método de prueba llamado 'test_sine_positive' para probar la función 'sine' con un ángulo positivo.
    def test_sine_positive(self):
        result = sine(0.5)  # Calcula el seno de 0.5 radianes utilizando la función 'sine'.
        expected = math.sin(0.5)  # Calcula el valor esperado utilizando la función 'math.sin'.
        self.assertAlmostEqual(result, expected, places=5)  # Comprueba si el resultado y el valor esperado son aproximadamente iguales con 5 decimales de precisión.

    # Define un método de prueba llamado 'test_sine_negative' para probar la función 'sine' con un ángulo negativo.
    def test_sine_negative(self):
        result = sine(-0.5)  # Calcula el seno de -0.5 radianes utilizando la función 'sine'.
        expected = math.sin(-0.5)  # Calcula el valor esperado utilizando la función 'math.sin'.
        self.assertAlmostEqual(result, expected, places=5)  # Comprueba si el resultado y el valor esperado son aproximadamente iguales con 5 decimales de precisión.

    # Define un método de prueba llamado 'test_sine_zero' para probar la función 'sine' con un ángulo de 0 radianes.
    def test_sine_zero(self):
        result = sine(0)  # Calcula el seno de 0 radianes utilizando la función 'sine'.
        expected = math.sin(0)  # El seno de 0 radianes debe ser 0, calculado con la función 'math.sin'.
        self.assertEqual(result, expected)  # Comprueba si el resultado es igual al valor esperado.

# Verifica si el script se ejecuta como el programa principal.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase 'TestTrigLog'.
