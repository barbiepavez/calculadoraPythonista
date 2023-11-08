import unittest  # Importa el módulo unittest para realizar pruebas unitarias.
from funcionesbasicas import multiply  # Importa la función 'multiply' desde el módulo 'funcionesbasicas'.

# Define una clase llamada 'TestFuncionesBasicas' que hereda de 'unittest.TestCase'.
class TestFuncionesBasicas(unittest.TestCase):
    
    # Define un método de prueba llamado 'test_multiply' para probar la función 'multiply' con argumentos 2 y 3.
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)  # Comprueba si multiply(2, 3) es igual a 6.

    # Define otro método de prueba 'test_multiply' para probar la función 'multiply' con argumentos -8 y 4.
    def test_multiply(self):
        self.assertEqual(multiply(-8, 4), -32)  # Comprueba si multiply(-8, 4) es igual a -32.

    # Define otro método de prueba 'test_multiply' para probar la función 'multiply' con argumentos -7 y -3.
    def test_multiply(self):
        self.assertEqual(multiply(-7, -3), 21)  # Comprueba si multiply(-7, -3) es igual a 21.

# Verifica si el script se ejecuta como el programa principal.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase 'TestFuncionesBasicas'.
