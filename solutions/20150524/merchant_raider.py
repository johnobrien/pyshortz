'''
Created on May 24, 2015

@author: johno_000
'''


from solver.solver import Solver
from solver.word import alphabetize


class MySolver(Solver):
    '''
    MySolver is an example solver
    which is a child of the solver class.
    '''

    def solve(self, kws):
        '''
        Solving the puzzle for this week.
        '''

        jobs = self.get_words(kws)
        anagrams = dict()
        for job1 in jobs:
            for job2 in jobs:
                anagrams[alphabetize(job1+job2)] = [job1, job2]

        print("Jobs are {0} and {1}".format(anagrams[alphabetize("merchantraider")][0],
                                            anagrams[alphabetize("merchantraider")][1]))

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
