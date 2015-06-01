'''
Created on May 31, 2015

@authors: leiran biton, john o'brien
'''
import unittest
from chicken import ChickenSolver

class TestChicken(unittest.TestCase):


    def test_simple(self):
        words = {"bacon",
                 "friendly",
                 "fresh",
                 "frosh"}
        s = ChickenSolver("Simple Test", rebuild=True)
        hits = s.solve(words)
        for hit in hits:
            print("Total:{0} {1} chicken, chicken {2}".format(hit[0], hit[2], hit[4]))



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()