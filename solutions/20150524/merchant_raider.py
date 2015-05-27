'''
Created on May 24, 2015

@author: john o'brien and leiran biton
'''

import csv
from nltk.corpus import words
from solver.solver import Solver, char_filter
from solver.word import alphabetize, build_anagrams


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
    
    def try_wordy_words(self, words):
        '''
        For all words, first remove one word from
        merchant raider, and then see if
        the alphbetized version of what remains
        matches any other word.
        '''
        for word1 in words:
            if len(word1) >= 2:
                mr = self.word
                word1_in_mr = True
                for letter in word1:
                    if letter in mr:
                        # remove the letter we found
                        mr = char_filter(mr, letter, 1)
                    else:
                        # we didn't find this letter, so we don't have a match
                        word1_in_mr = False
                
                if word1_in_mr:
                    for word2 in words:
                        if len(word2) >= 2:
                            remainder = mr
                            word2_in_remainder = True
                            for letter in word2:
                                if letter in remainder:
                                    # remove the letter we found
                                    remainder = char_filter(remainder, letter, 1)
                                else:
                                    word2_in_remainder = False
                            
                            if word2_in_remainder and remainder == "":
                                print("One possible match is {0} and {1}".format(word1, word2))


                    

if __name__ == '__main__':

    # Really? Leiran, I appreciate that you like ,"blah" more than "blah",
    # But is there a specific benefit? Because if not, Pydev throws up all
    # this and it triggers a dozen or so format warning errors.
    
    # Format errors about what? 
    # PyDev doesn't like __name__ == __main__? Or something else?
    # I like __name__ == __main__ for testing, but I think we should probably
    # move away from it for actual results generation.
    kws = ["occupation"
          ,"job"
          ,"someone"
          ,"person"
          ,"a man"
          ,"a woman"
          ,"duty"
          ,"duties"
          ,"officer"
          ,"exuctive"
          ,"operator"
          ,"employee"
          ,"who"
          ,"official"
          ,"writer"
          ,"a female" 
           ]

    p = '''Take the phrase "merchant raider." A merchant raider was a vessel in
World War I and World War II that targeted enemy merchant ships. Rearrange the
letters of "merchant raider" to get two well-known professions. What are
they?'''

    s = MySolver(p, word="blosserfakers", verbose=False)
    s.try_list("testing", ["baker", "flosser", "flossers", "bakers"])

    s = MySolver(p, word="merchantraider", verbose=True)
    #Try NLTK
    print("accessing nltk with keyword list:")
    for keyword in kws:
        print("    {0}".format(keyword))
    wordnet_jobs = s.get_words(kws)
    print("retrieved {0} potential entries".format(len(wordnet_jobs)))
    s.try_list("wordnet", wordnet_jobs)
#     s.clear_candidates()
#     #Try user supplied list
#     filename = "jobs.csv"
#     with open(filename, 'r') as f:
#         reader = csv.reader(f)
#         csv_jobs = [job[0] for job in list(reader)]
#         print("retrieved {0} potential entries".format(len(csv_jobs)))
#         s.try_list("User supplied job list", csv_jobs)
#     #Try with both
#     print("Trying with both")
#     s.try_list("both lists", wordnet_jobs + csv_jobs)
#     #Try using all wordnet words
#     words = words.words()
#     words.append("trader")
#     words.append("teacher")
#     s.try_wordy_words(words)
