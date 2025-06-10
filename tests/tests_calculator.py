import unittest
from src.calculator import suma, resta

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(suma(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(resta(10, 5), 5)


    
