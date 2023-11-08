import unittest  # Importa el módulo unittest para realizar pruebas unitarias.
from funcionesbasicas import root  # Importa la función 'root' desde el módulo 'funcionesbasicas'.

# Define una clase llamada 'TestFuncionesBasicas' que hereda de 'unittest.TestCase'.
class TestFuncionesBasicas(unittest.TestCase):
    
    # Define un método de prueba llamado 'test_raiz_entera' que prueba la función 'root' con raíces enteras.
    def test_raiz_entera(self):
        result = root(16, 2)  # Calcula la raíz cuadrada de 16.
        self.assertEqual(result, 4)  # Comprueba si el resultado es igual a 4.

    # Define un método de prueba llamado 'test_raiz_decimal' que prueba la función 'root' con raíces decimales.
    def test_raiz_decimal(self):
        result = root(81, 2)  # Calcula la raíz cuadrada de 81.
        self.assertAlmostEqual(result, 9.0, places=5)  # Comprueba si el resultado es aproximadamente igual a 9.0 con 5 decimales de precisión.

    # Define un método de prueba llamado 'test_raiz_base_cero' que prueba la función 'root' con una base igual a cero.
    def test_raiz_base_cero(self):
        result = root(0, 3)  # La raíz de 0 en cualquier índice es igual a 0.
        self.assertEqual(result, 0)  # Comprueba si el resultado es igual a 0.

# Verifica si el script se ejecuta como el programa principal.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase 'TestFuncionesBasicas'.
