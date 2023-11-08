import unittest
from funcionesbasicas import root

class TestFuncionesBasicas(unittest.TestCase):
    def test_raiz_entera(self):
        result = root(16, 2)
        self.assertEqual(result, 4)

    def test_raiz_decimal(self):
        result = root(81, 2)
        self.assertAlmostEqual(result, 9.0, places=5)

    def test_raiz_base_cero(self):
        result = root(0, 3)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()