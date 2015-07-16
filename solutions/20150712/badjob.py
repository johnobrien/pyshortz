'''
Created on May 24, 2015

@author: john o'brien and leiran biton
'''

import csv
from nltk.corpus import words
from solver.solver import Solver, char_filter, get_all_words
from string import punctuation

class JobSolver(Solver):
    '''
    MySolver is an example solver
    which is a child of the solver class.
    '''
    
    def loadwords(self, wordlist):
        self.words = wordlist
    
    def loadjobs(self, joblist):
        jobs_oneword = {}
        for job in joblist:
            if job.startswith("b"):
                job_stripped = char_filter(job, " "+punctuation)
                if job_stripped in jobs_oneword:
                    jobs_oneword[job_stripped].add(job)
                else:
                    jobs_oneword[job_stripped] = set([job])
            self.jobs = jobs_oneword
    
    def process(self, job):
        job_stripped = char_filter(job, " "+punctuation)
        if len(job_stripped) < 4:
            return ""
        else:
            return job_stripped[0] + job_stripped[4:]
    
    def solve(self, threshold=1):
        for job in self.jobs.keys():
            processed = self.process(job)
            if processed in self.words and len(processed >= threshold):
                for val in self.jobs[job]:
                    self.candidates.add((val, processed))
    
    def get_candidates(self):
        """prints the current list of candidates"""
        print("current candidates:")
        for job, word in self.candidates:
            print("    {0} --> {1}".format(job, word))

if __name__ == '__main__':

    p = '''Name an occupation starting with the letter B.
Remove the second, third and fourth letters. The
remaining letters in order will name something you might
experience in the presence of someone who has this
occupation. What is it?'''

    s = JobSolver(p)
    print("accessing nltk with keyword list:")
    kws = ["occupation",
           "job",
           "someone",
           "person",
           "a man",
           "a woman",
           "duty",
           "duties",
           "officer",
           "exuctive",
           "operator",
           "employee",
           "who",
           "official",
           "writer",
           "a female"
           ]
    for kw in kws:
        print("    {0}".format(kw))
    wordnet_jobs = s.get_words(kws)
    s.loadjobs(wordnet_jobs)
    s.loadwords(get_all_words())
    s.solve(threshold=3)
    s.get_candidates()
    
