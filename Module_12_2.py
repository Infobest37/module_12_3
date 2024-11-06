import unittest
from Test_runn import Runner,Tournament

class Tournament1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.user_1 = f"Бегун по имени {self.runner1.name}, со скоростью {self.runner1.speed}"
        self.runner2 = Runner("Андрей",  9)
        self.user_2 = f"Бегун по имени {self.runner2.name}, со скоростью {self.runner2.speed}"
        self.runner3 = Runner("Nik",  3)
        self.user_3 = f"Бегун по имени {self.runner3.name}, со скоростью {self.runner3.speed}"

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_1(self):
        # Забег между Усэйном и Ником

        tournament = Tournament(90, self.runner1, self.runner3)

        result = tournament.start()
        # Сохраняем результат в all_result
        Tournament1.all_results["Усэйн & Nik"] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())] == self.runner3)

    def test_2(self):
        # Забег Андреем и Ником
        tournament = Tournament(90,  self.runner2, self.runner3)
        result = tournament.start()
        # Сохраняем результат в all_results
        Tournament1.all_results['Andrey & Nick'] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())] == self.runner3)
    def test_3(self):
        # Забег между Усэйном, Андреем и Ником
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        # Сохраняем результат в all_results
        Tournament1.all_results['Usain, Andrey & Nick'] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())] == self.runner3)


if __name__ == '__main__':
    unittest.main()

