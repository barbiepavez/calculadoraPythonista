import unittest  # Importa el módulo unittest para realizar pruebas unitarias.
from funcionesbasicas import add  # Importa la función 'add' desde el módulo 'funcionesbasicas'.

# Define una clase llamada 'TestFuncionesBasicas' que hereda de 'unittest.TestCase'.
class TestFuncionesBasicas(unittest.TestCase):
    
    # Define un método de prueba llamado 'test_suma' para probar la función 'add' con argumentos 2 y 3.
    def test_suma(self):
        self.assertEqual(add(2, 3), 5)  # Comprueba si add(2, 3) es igual a 5.

    # Define otro método de prueba 'test_suma' para probar la función 'add' con argumentos -5 y -7.
    def test_suma(self):
        self.assertEqual(add(-5, -7), -12)  # Comprueba si add(-5, -7) es igual a -12.

    # Define otro método de prueba 'test_suma' para probar la función 'add' con argumentos 10 y -4.
    def test_suma(self):
        self.assertEqual(add(10, -4), 6)  # Comprueba si add(10, -4) es igual a 6.

    # Define otro método de prueba 'test_suma' para probar la función 'add' con argumentos -12 y 5.
    def test_suma(self):
        self.assertEqual(add(-12, 5), -7)  # Comprueba si add(-12, 5) es igual a -7.

# Verifica si el script se ejecuta como el programa principal.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase 'TestFuncionesBasicas'.