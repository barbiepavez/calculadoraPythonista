import unittest  # Importa el módulo unittest para realizar pruebas unitarias.
from funcionesbasicas import remainder  # Importa la función 'remainder' desde el módulo 'funcionesbasicas'.

# Define una clase llamada 'TestFuncionesBasicas' que hereda de 'unittest.TestCase'.
class TestFuncionesBasicas(unittest.TestCase):
    
    # Define un método de prueba llamado 'test_resto_entero' para probar la función 'remainder' con argumentos 10 y 3.
    def test_resto_entero(self):
        self.assertEqual(remainder(10, 3), 1)  # Comprueba si remainder(10, 3) devuelve el resto 1.

    # Define un método de prueba 'test_resto_por_cero' para probar el manejo de excepciones cuando se intenta
    # encontrar el resto de una división por cero.
    def test_resto_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            remainder(5, 0)  # Debe lanzar una excepción ZeroDivisionError cuando se intenta dividir por cero.

# Verifica si el script se ejecuta como el programa principal.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase 'TestFuncionesBasicas'.
