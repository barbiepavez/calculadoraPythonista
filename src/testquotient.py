import unittest  # Importa el módulo unittest para realizar pruebas unitarias.
from funcionesbasicas import quotient  # Importa la función 'quotient' desde el módulo 'funcionesbasicas'.

# Define una clase llamada 'TestFuncionesBasicas' que hereda de 'unittest.TestCase'.
class TestFuncionesBasicas(unittest.TestCase):
    
    # Define un método de prueba llamado 'test_quotient' para probar la función 'quotient' con argumentos 7 y 3.
    def test_quotient(self):
        self.assertEqual(quotient(7, 3), 2)  # Comprueba si quotient(7, 3) es igual a 2.

    # Define otro método de prueba 'test_quotient' para probar la función 'quotient' con argumentos 10 y 2.
    def test_quotient(self):
        self.assertEqual(quotient(10, 2), 5)  # Comprueba si quotient(10, 2) es igual a 5.

    # Define un método de prueba llamado 'test_cuociente_por_cero' para probar el manejo de excepciones
    # cuando se intenta dividir por cero.
    def test_cuociente_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            quotient(5, 0)  # Debe lanzar una excepción ZeroDivisionError cuando se intenta dividir por cero.

# Verifica si el script se ejecuta como el programa principal.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase 'TestFuncionesBasicas'.
