import unittest
from funcionesbasicas import divide

class TestFuncionesBasicas(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(8, 2), 4 )
    def test_divide(self):
        self.assertEqual(divide(7, 2), 3.5 )
    def test_divide(self):
        self.assertEqual(divide(-10, 5), -2 )
    def def test_divide(self):
        self.assertEqual(divide(8, 0), Error )

    

if __name__ == '__main__':
    unittest.main()