'''
Created on May 27, 2015

@author: john.obrien
'''
import unittest
from solver import char_filter, search_brown


class TestSolver(unittest.TestCase):
    '''
    Unit tests for the solver.py file.
    '''

    def test_char_filter(self):
        '''
        Tests to run char_filter
        through it's paces.
        '''
        self.assertEqual('bc', char_filter('abc', 'a'))
        self.assertEqual('bca', char_filter('abca', 'a', 1))
        self.assertEqual('aaaaccccc', char_filter('aabababbbbbbbccbcbcc', 'b'))
        self.assertEqual('aabcdef', char_filter('aabbcdef', 'b', 1))

    def test_search_brown(self):
        '''
        Tests to run see if searching
        brown returns consistent results.
        '''
        self.assertEqual(67, search_brown("jury"))
        self.assertEqual(1, search_brown("roast chicken"))
        self.assertEqual(1, search_brown("relative handful"))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
