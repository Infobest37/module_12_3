import unittest
import Test_calc
import new_test_calc
calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_calc.TestCalc))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(new_test_calc.NewCalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)
