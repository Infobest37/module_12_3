import unittest
from Test_Runner import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = True
    def setUp(self):
        print('setUp')

    @classmethod
    def tearDownClass(cls):
        print('setUpClass')
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_wallk(self):

        runner = Runner('wallk')

        for _ in range(10):
            runner.walk()
        self.assertEqual(50, runner.distance)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner('run')

        for _ in range(10):
            runner.run()
        self.assertEqual(100, runner.distance)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self ):
        runner1 = Runner('challenge')
        runner2 = Runner('challenge2')
        for _ in range(10):
            runner1.walk()
        for _ in range(10):
            runner2.run()
        self.assertNotEquals(runner2.distance, runner1.distance)


if __name__ == '__main__':
    unittest.main()

