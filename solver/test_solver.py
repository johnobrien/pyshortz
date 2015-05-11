'''
Created on May 10, 2015

@authors: john o'brien, leiran biton
'''
import unittest
from solver import Word

class TestWord(unittest.TestCase):


    def setUp(self):
        pass

    def test_how(self):
        w = Word("how")
        self.assertEqual(w.t, "how")
        self.assertEqual(w.anagrams, {"how", "who"})
        self.assertEqual(w.reversed, "woh")
        self.assertEqual(w.alphabetized, "how")
        self.assertEqual(w.syllables, [1])

    def tearDown(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()