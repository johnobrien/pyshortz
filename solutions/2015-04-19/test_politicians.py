import unittest
from politicians import solution

class TestSolution(unittest.TestCase):
    def test_two_names(self):
        names = ("Hlbmuh", "Ecuoc")
        switched = ("humble", "couch")
        s = solution(*names)
        self.assertEqual(s.candidates, [names + switched], "Hlbmuh and Ecuoc did not generate humble and couch.")

    def test_three_names(self):
        pass

if __name__ == "__main__":
    unittest.main()
