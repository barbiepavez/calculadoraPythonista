import unittest  # Importa el módulo unittest para realizar pruebas unitarias.
from funcionesbasicas import subtract  # Importa la función 'subtract' desde el módulo 'funcionesbasicas'.

# Define una clase llamada 'TestFuncionesBasicas' que hereda de 'unittest.TestCase'.
class TestFuncionesBasicas(unittest.TestCase):
    
    # Define un método de prueba llamado 'test_suma' para probar la función 'subtract' con argumentos 7 y 3.
    def test_suma(self):
        self.assertEqual(subtract(7, 3), 4)  # Comprueba si subtract(7, 3) es igual a 4.

    # Define otro método de prueba 'test_suma' para probar la función 'subtract' con argumentos -15 y 8.
    def test_suma(self):
        self.assertEqual(subtract(-15, 8), -7)  # Comprueba si subtract(-15, 8) es igual a -7.

    # Define otro método de prueba 'test_suma' para probar la función 'subtract' con argumentos -7 y -4.
    def test_suma(self):
        self.assertEqual(subtract(-7, -4), -3)  # Comprueba si subtract(-7, -4) es igual a -3.

    # Define otro método de prueba 'test_suma' para probar la función 'subtract' con argumentos 12 y 19.
    def test_suma(self):
        self.assertEqual(subtract(12, 19), -7)  # Comprueba si subtract(12, 19) es igual a -7.

# Verifica si el script se ejecuta como el programa principal.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase 'TestFuncionesBasicas'.
