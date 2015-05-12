'''
Created on May 10, 2015

@authors: john o'brien, leiran biton
'''
import unittest
from solver import Word


class TestWord(unittest.TestCase):
    def test_how(self):
        w = Word("how")
        self.assertEqual(w.t, "how")
        self.assertEqual(w.anagrams, {"how", "who"})
        self.assertEqual(w.reversed, "woh")
        self.assertEqual(w.alphabetized, "how")
        self.assertEqual(w.syllables, {1})

    def test_listen(self):
        w = Word("listen")
        self.assertEqual(w.t, "listen")
        self.assertEqual(w.anagrams, {"listen", "silent", "enlist", "tinsel"})
        self.assertEqual(w.reversed, "netsil")
        self.assertEqual(w.alphabetized, "eilnst")
        self.assertEqual(w.syllables, {2})

    def test_dictionary(self):
        w = Word("dictionary")
        self.assertEqual(w.t, "dictionary")
        self.assertEqual(w.anagrams, {"dictionary", "indicatory"})
        self.assertEqual(w.reversed, "yranoitcid")
        self.assertEqual(w.alphabetized, "acdiinorty")
        self.assertEqual(w.syllables, {4})

    def test_project(self):
        w = Word("project")
        self.assertEqual(w.t, "project")
        self.assertEqual(w.anagrams, {"project"})
        self.assertEqual(w.reversed, "tcejorp")
        self.assertEqual(w.alphabetized, "cejoprt")
        self.assertEqual(w.syllables, {2})


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()