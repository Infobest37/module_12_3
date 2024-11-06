import random
import unittest
import Calc
import random


class TestCalc(unittest.TestCase):
    @unittest.skip("Not good")
    def test_add(self):
        self.assertEqual(Calc.add(1, 2), 3)
    @unittest.skipIf(random.randint(0, 2), "Welcome")
    def test_subtract(self):
        self.assertEqual(Calc.subtract(1, 2), -1)
    def test_multiply(self):
        self.assertEqual(Calc.multiply(1, 2), 2)
    def test_divide(self):
        self.assertEqual(Calc.divide(1, 2), 0.5)
    # def test_square(self):
    #     self.assertEqual(Calc.square(1))
