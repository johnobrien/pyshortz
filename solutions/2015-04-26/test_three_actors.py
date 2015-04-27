#!/usr/local/bin/env python

'''
Created on Apr 26, 2015

@authors: Leiran Biton, John O'Brien
'''
"""Problem:
Name a famous actor whose first and last names both are 
seven letters long. Change the first three letters of 
the actor's last name to three new letters and you'll 
name another famous actor. They share the same first 
name. Add the three letters you changed in the first 
actor's last name plus the three letters you changed 
to get the second actor's name, and you'll spell the 
last name of a third famous actor. 

Who are these three Hollywood stars?
"""

import unittest
from three_actors import Solution

class TestSolution(unittest.TestCase):
    
    def test_first_actor(self):
        actor = "Earnest Fleming"
        s = Solution(None)
        self.assertTrue(s.first_actor("Earnest Fleming"))

    def test_second_actor(self):
        actor1 = "Earnest Fleming"
        actor2 = "Earnest Troming"
        s = Solution(None)
        self.assertTrue(s.second_actor(actor1, actor2))

    def test_third_actor(self):
        actor1 = "Earnest Fleming"
        actor2 = "Earnest Troming"
        actor3 = "Killing Fletro"
        s = Solution(None)
        self.assertTrue(s.third_actor(actor1, actor2, actor3))



    def test_three_actors(self):
        actors = {"Earnest Fleming",
                  "Earnest Troming",
                  "Killing Fletro"}
        possible_answers = {("Earnest Fleming",
                                 "Earnest Troming",
                                 "Killing Fletro")}
        s = Solution(actors)
        self.assertEqual(possible_answers, s.possible_answers)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()