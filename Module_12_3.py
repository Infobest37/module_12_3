import unittest
import Module_12_2
import Unut_Test_Runner
calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2.Tournament1))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(Unut_Test_Runner.RunnerTest))



runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)