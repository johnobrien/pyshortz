import unittest
from politicians import solution

class TestSolution(unittest.TestCase):

    def test_two_names(self):
        names = ("Euh", "Mlb")
        s = solution(names)
        self.assertEqual(s.candidates, [("Euh", "Mlb", "humble")], "'Euh' and 'Mlb' did not generate 'humble'.")
        
    def test_three_names(self):
        names = ("Euh", "Mlb", "Parsley")
        s = solution(names)
        self.assertEqual(s.candidates, [("Euh", "Mlb", "humble")], "'Euh', 'Mlb' and 'Parsley' did not generate 'humble'.")

    def test_four_names(self):
        names = ("Euh", "Mlb", "Parsley", "Esquire")
        s = solution(names)
        self.assertEqual(s.candidates, [("Euh", "Mlb", "humble")], "'Euh', 'Mlb', 'Parsley', 'Esquire' did not generate 'humble'.")

    def test_many_names(self):
        names = ('N', 'Ben', 'Frances', 'Hillary', 'Bacon', 'Newheart', 'Guoy')
        switched = [('Guoy', 'N', 'young')]
        s = solution(names, verbose=True)
        self.assertEqual(s.candidates, switched)

if __name__ == "__main__":
    unittest.main()
