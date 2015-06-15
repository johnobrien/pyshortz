'''
Created on June 15, 2015

@authors: leiran biton, john o'brien
'''
import unittest
from shampoo import ShampooSolver

class TestShampoo(unittest.TestCase):

    def test_simple(self):
        adjectives = {"soapy", "slimy", "smelly"}
        shampoos   = {"head and shoulders", "pert"}
        musicians  = {"R.E.M.", "The Carolina Chocolate Drops", "soap ypert"}
        s = ShampooSolver("Simple Test")
        s.solve(adjectives=adjectives, shampoos=shampoos, musicians=musicians)
        s.print_candidates()
    
    def test_punctuation(self):
        adjectives = {"soapy", "slimy", "smelly", "re"}
        shampoos   = {"head and shoulders", "pert", "M"}
        musicians  = {"R.E.M.", "The Carolina Chocolate Drops"}
        s = ShampooSolver("Punctuation Test")
        s.solve(adjectives=adjectives, shampoos=shampoos, musicians=musicians)
        s.print_candidates()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()