'''
Created on May 27, 2015

@author: john.obrien
'''
import unittest
from solver import char_filter, search_brown, google_search, ghits


class TestCharFilter(unittest.TestCase):
    '''
    Unit tests for char_filter function.
    '''

    def test_simple(self):
        '''
        Tests to run char_filter
        through it's paces.
        '''
        self.assertEqual('bc', char_filter('abc', 'a'))
        self.assertEqual('bca', char_filter('abca', 'a', 1))
        self.assertEqual('aaaaccccc', char_filter('aabababbbbbbbccbcbcc', 'b'))
        self.assertEqual('aabcdef', char_filter('aabbcdef', 'b', 1))

    def test_vowels(self):
        vowels = "aeiou"
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
        vowels = "aeiou"
        self.assertEqual(char_filter("basement", vowels, 1), "bsment")


class TestSearchBrown(unittest.TestCase):
    '''
    Unit tests for search_brown function.
    '''

    def test_search_brown(self):
        '''
        Tests to run see if searching
        brown returns consistent results.
        '''
        self.assertEqual(67, search_brown("jury"))
        self.assertEqual(1, search_brown("roast chicken"))
        self.assertEqual(1, search_brown("relative handful"))


class TestGoogleSearch(unittest.TestCase):
    '''
    Unit tests for GoogleSearch function.
    '''

    def test_ghits(self):
        '''
        Tests to run see if searching
        google returns any result.
        '''
        content = google_search("hits")
        self.assertEqual(2500000000, ghits(content))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
