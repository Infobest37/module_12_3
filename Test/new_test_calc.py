import unittest
import Calc

class NewCalcTest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(Calc.sqrt(4), 2)
    def test_pow(self):
        self.assertEqual(Calc.power(3, 3), 27)
