import unittest  # Importa el módulo unittest para realizar pruebas unitarias.
from funcionesbasicas import power  # Importa la función 'power' desde el módulo 'funcionesbasicas'.

# Define una función llamada 'test_potencia_entera' que prueba la función 'power' con argumentos enteros.
def test_potencia_entera(self):
    result = power(2, 3)  # Calcula 2 elevado a la 3a potencia.
    self.assertEqual(result, 8)  # Comprueba si el resultado es igual a 8.

# Define una función llamada 'test_potencia_decimal' que prueba la función 'power' con exponentes decimales.
def test_potencia_decimal(self):
    result = power(2, 0.5)  # Calcula 2 elevado a la raíz cuadrada de 2.
    self.assertAlmostEqual(result, 1.414213, places=5)  # Comprueba si el resultado es aproximadamente igual a 1.414213 con 5 decimales de precisión.

# Define una función llamada 'test_potencia_base_cero' que prueba la función 'power' con base igual a cero.
def test_potencia_base_cero(self):
    result = power(0, 3)  # Cualquier número elevado a la potencia 0 es igual a 1.
    self.assertEqual(result, 0)  # Comprueba si el resultado es igual a 0.

# Define una función llamada 'test_potencia_exponente_cero' que prueba la función 'power' con exponente igual a cero.
def test_potencia_exponente_cero(self):
    result = power(5, 0)  # Cualquier número elevado a la potencia 0 es igual a 1.
    self.assertEqual(result, 1)  # Comprueba si el resultado es igual a 1.

# Verifica si el script se ejecuta como el programa principal.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en las funciones de prueba.
