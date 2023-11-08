import unittest  # Importa el módulo unittest para realizar pruebas unitarias.
from funcionesbasicas import divide  # Importa la función 'divide' desde el módulo 'funcionesbasicas'.

# Define una clase llamada 'TestFuncionesBasicas' que hereda de 'unittest.TestCase'.
class TestFuncionesBasicas(unittest.TestCase):
    
    # Define un método de prueba llamado 'test_divide' para probar la función 'divide' con argumentos 8 y 2.
    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)  # Comprueba si divide(8, 2) es igual a 4.

    # Define otro método de prueba 'test_divide' para probar la función 'divide' con argumentos 7 y 2.
    def test_divide(self):
        self.assertEqual(divide(7, 2), 3.5)  # Comprueba si divide(7, 2) es igual a 3.5.

    # Define otro método de prueba 'test_divide' para probar la función 'divide' con argumentos -10 y 5.
    def test_divide(self):
        self.assertEqual(divide(-10, 5), -2)  # Comprueba si divide(-10, 5) es igual a -2.

    # Define un método de prueba 'test_divide' que intenta dividir por cero.
    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)  # Debe lanzar una excepción ZeroDivisionError cuando se intenta dividir por cero.

# Verifica si el script se ejecuta como el programa principal.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase 'TestFuncionesBasicas'.
