import unittest
import Module_12_2
calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2.Tournament1))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)