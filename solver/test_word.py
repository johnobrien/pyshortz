'''
Created on May 10, 2015

@authors: john o'brien, leiran biton
'''
import unittest
from word import Word, char_filter


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

        def test_vowels(self):
            self.assertEqual(char_filter("christmas", vowels), "chrstms")
        def test_butterfly(self):
            self.assertEqual(char_filter("butterfly", "t"), "buerfly")
        def test_single_filter(self):
            self.assertEqual(char_filter("butterstick", "t", 1), "buterstick")
            self.assertEqual(char_filter("butterstick", "t", 2), "buerstick")
            self.assertEqual(char_filter("butterstick", "t", 3), "buersick")
        def test_multiple_filter(self):
            self.assertEqual(char_filter("mississippi", "is"), "mpp")
            self.assertEqual(char_filter("mississippi", "is", 1), "msissippi")
            self.assertEqual(char_filter("mississippi", "is", 2), "mssippi")
            self.assertEqual(char_filter("mississippi", "is", 3), "msppi")
        def test_count(self):
            self.assertEqual(char_filter("basement", vowels, 1), "bsment")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()