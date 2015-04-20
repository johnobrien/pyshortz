import unittest
from politicians import solution

class TestSolution(unittest.TestCase):
    def test_two_names(self):
        names = ("Hlbmuh", "Ecuoc")
        s = solution(*names)
        self.assertEqual(s.candidates, [("Hlbmuh", "Ecuoc", "humble", "couch")], "Hlbmuh and Ecuoc did not generate humble and couch.")

    def test_three_names(self):
        names = ("Hlbmuh", "Ecuoc", "Parsley")
        s = solution(*names)
        self.assertEqual(s.candidates, [("Hlbmuh", "Ecuoc", "humble", "couch")], "Hlbmuh and Ecuoc did not generate humble and couch.")

    def test_four_names(self):
        names = ("Ben", "Ted", "Tim", "Don")
        switched = [('Ben', 'Ted', 'net', 'deb'),
                    ('Ben', 'Tim', 'net', 'mib'),
                    ('Tim', 'Don', 'mid', 'not')]
        s = solution(*names)
        self.assertEqual(s.candidates, switched, "Hlbmuh and Ecuoc did not generate humble and couch.")

if __name__ == "__main__":
    unittest.main()
