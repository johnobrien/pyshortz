import unittest
from politicians import solution

class TestSolution(unittest.TestCase):

    def test_two_names(self):
        names = ("Euh", "Mlb")
        s = solution(names)
        self.assertEqual(s.candidates, [("Euh", "Mlb", "humble")], "Hlbmuh and Ecuoc did not generate humble and couch.")
        
    def test_three_names(self):
        names = ("Euh", "Mlb", "Parsley")
        s = solution(names)
        self.assertEqual(s.candidates, [("Euh", "Mlb", "humble", "blehum")], "Hlbmuh, Ecuoc and Parsley did not generate humble and couch.")

    def test_four_names(self):
        names = ("Ben", "Ted", "Tim", "Don")
        switched = [('Ben', 'Ted', 'net', 'deb'),
                    ('Ben', 'Tim', 'net', 'mib'),
                    ('Tim', 'Don', 'mid', 'not')]
        s = solution(names)
        self.assertEqual(s.candidates, switched)

    def test_many_names(self):
        names = ('Gen', 'Ben', 'Frances', 'Hillary', 'Bacon', 'Newheart', 'Wnuoy')
        switched = [('Gen', 'Wnuoy', 'new', 'young')]
        s = solution(names)
        self.assertEqual(s.candidates, switched)

if __name__ == "__main__":
    unittest.main()
