'''
Created on July 15, 2015

@authors: leiran biton, john o'brien
'''
import unittest
from badjob import JobSolver

class TestJob(unittest.TestCase):


    def test_simple(self):
        jobs = {"bartender",
                "baker",
                "candlestick maker",
                "faker"}
        words = ["bender", "fender"]
        s = JobSolver("Simple Test")
        s.loadwords(words)
        s.loadjobs(jobs)
        s.solve()
        for (job, quality) in s.candidates:
            print("Total:{0} --> {1}".format(job, quality))
        self.assertEqual([("bartender", "bender")], list(s.candidates))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()