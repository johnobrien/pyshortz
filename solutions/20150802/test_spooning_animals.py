import unittest

from spooning_animals import SpooningAnimalsSolver


class TestAnimals(unittest.TestCase):

    def test_simple(self):
        '''Test to switch first consonant letters'''
        animals = ["cat", "dog", "cog dat", "moose"]
        correct_solution = ["cat", "dog", "cog dat"]
        s = SpooningAnimalsSolver("Simple Test", verbose=False)
        self.assertEqual(correct_solution,
                         s.solve(animals=animals))

    def test_hard(self):
        '''Test to switch first sounds'''
        animals = ["phoenix", "squirrel", "phuirrel sqoenix", "horse"]
        correct_solution = ["phoenix", "squirrel", "phuirrel sqoenix"]
        s = SpooningAnimalsSolver("Hard Test", verbose=False)
        self.assertEqual(correct_solution,
                         s.solve(animals=animals))

if __name__ == "__main__":
    unittest.main()
