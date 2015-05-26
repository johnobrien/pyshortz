'''
Created on May 24, 2015

@author: johno_000
'''


from solver.solver import Solver
from solver.word import alphabetize
import csv


class MySolver(Solver):
    '''
    MySolver is an example solver
    which is a child of the solver class.
    '''

    def solve(self, kws):
        '''
        Solving the puzzle for this week.
        '''

        wordnet_jobs = self.get_words(kws)
        self.try_list("wordnet", wordnet_jobs)
        with open('jobs.csv', 'r') as f:
            reader = csv.reader(f)
            bls_jobs = list(reader)
            self.try_list("BLS Job Titles", bls_jobs)

    def try_list(self, list_name, jobs):
        '''
        Takes a list job titles,
        and trys to find whether any of them together
        match merchant raider
        alphabetized.
        '''

        anagrams = dict()
        for job1 in jobs:
            for job2 in jobs:
                anagrams[alphabetize(job1+job2)] = [job1, job2]
        try:
            print("Jobs are {0} and {1}".format(anagrams[alphabetize("merchantraider")][0],
                                                anagrams[alphabetize("merchantraider")][1]))
        except:
            print("{0} list do not find a match.".format(list_name))

        return
        

if __name__ == '__main__':

    kws = ["occupation",
           "job",
           "someone",
           "person",
           "a man",
           "a woman",
           "duty",
           "duties"
           ]

    p = '''Take the phrase "merchant raider." A merchant raider was a vessel in
World War I and World War II that targeted enemy merchant ships. Rearrange the
letters of "merchant raider" to get two well-known professions. What are
they?'''

    s = MySolver(p)
    s.solve(kws)
