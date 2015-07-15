'''
Created on May 24, 2015

@author: john o'brien and leiran biton
'''

import csv
from nltk.corpus import words
from solver.solver import Solver, char_filter
from solver.word import alphabetize, build_anagrams
from string import punctuation

class MySolver(Solver):
    '''
    MySolver is an example solver
    which is a child of the solver class.
    '''
    
    def loadwords(self, wordlist):
        self.words = wordlist
    
    def loadjobs(self, joblist):
        self.jobs = joblist
    
    def process(self, job):
        job_stripped = job.remove(" "+punctuation)
        if len(job_stripped) < 4:
            return ""
        else:
            return job_stripped[0] + job_stripped[4:]
        
    
    def solver(self):
        for job in self.jobs:
            
    
    def try_list(self, list_name, jobs):
        '''
        Takes a list job titles,
        and trys to find whether any of them together
        match merchant raider alphabetized.
        '''
        if self.__dict__.get("verbose", False): 
            print("generating anagrams")
        self.anagrams = build_anagrams(jobs)
        for job in jobs:
            try:
                remaining_letters = alphabetize(char_filter(self.word, job, 1))
                if remaining_letters in self.anagrams:
                    for second_job in self.anagrams[remaining_letters]:
                        if ((job, second_job) not in self.candidates and (second_job, job) not in self.candidates):
                            self.candidates.add((job, second_job))
            except AssertionError:
                pass
        if self.__dict__.get("verbose", False): self.get_candidates()

    def get_candidates(self):
        """prints the current list of candidates"""
        print("current candidates:")
        for job1, job2 in self.candidates:
            print("    {0} {1}".format(job1, job2))


if __name__ == '__main__':

    p = '''Name an occupation starting with the letter B.
Remove the second, third and fourth letters. The
remaining letters in order will name something you might
experience in the presence of someone who has this
occupation. What is it?'''

    # quiet testing
    s = MySolver(p, word="blosserfakers", verbose=False)
    s.try_list("testing", ["baker", "flosser", "flossers", "bakers"])

    #Try NLTK
    s = MySolver(p, word="merchantraider", verbose=False)
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
    unfiltered_wordnet_jobs = s.get_words(kws)
    wordnet_jobs = [char_filter(job, punctuation+" ") for job in unfiltered_wordnet_jobs]
    job_dict = dict(zip(wordnet_jobs, unfiltered_wordnet_jobs))
    print("retrieved {0} potential entries".format(len(wordnet_jobs)))
    s.try_list("wordnet", wordnet_jobs)
    for job1, job2 in s.candidates:
        print(job_dict[job1], job_dict[job2])
