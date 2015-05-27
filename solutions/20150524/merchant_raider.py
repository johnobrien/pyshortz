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

    p = '''Take the phrase "merchant raider." A merchant raider was a vessel in
World War I and World War II that targeted enemy merchant ships. Rearrange the
letters of "merchant raider" to get two well-known professions. What are
they?'''

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
#     s.clear_candidates()
#     
#     print("populating list of words with letters that appear in 'merchant traider':")
#     words = words.words()
#     try_words = set()
#     for word in words:
#         try:
#             remaining_word = char_filter(s.word, word, 1)
#             try_words.add(word)
#         except AssertionError:
#             pass
#     print("retrieved {0} potential entries".format(len(try_words)))
#     s.try_list("all words with right letters", try_words)
#     
#     # try BLM list
#     filename = "jobs.csv"
#     with open(filename, 'r') as f:
#         reader = csv.reader(f)
#         csv_jobs = [job[0] for job in list(reader)]
#         print("retrieved {0} potential entries".format(len(csv_jobs)))
#         s.try_list("User supplied job list", csv_jobs)
