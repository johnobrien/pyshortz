'''
Created on May 24, 2015

@author: johno_000
'''

import csv
from nltk.corpus import words
from solver.solver import Solver, char_filter
from solver.word import alphabetize


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
        print("generating anagrams")
        anagrams = dict()
        for job1 in jobs:
            for job2 in jobs:
                anagrams[alphabetize(job1+job2)] = [job1, job2]
        if alphabetize("merchantraider") in anagrams:
            print("Jobs are {0} and {1}".format(anagrams[alphabetize("merchantraider")][0],
                                                anagrams[alphabetize("merchantraider")][1]))
        else:
            print("{0} list do not find a match.".format(list_name))

        return
        
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

    kws = ["occupation",
           "job",
           "someone",
           "person",
           "a man",
           "a woman",
           "duty",
           "duties" ,
           "officer" ,
           "exuctive" ,
           "operator" ,
           "employee" ,
           "who" ,
           "official" ,
           "writer" ,
           "a female" 
           ]

    p = '''Take the phrase "merchant raider." A merchant raider was a vessel in
World War I and World War II that targeted enemy merchant ships. Rearrange the
letters of "merchant raider" to get two well-known professions. What are
they?'''

    s = MySolver(p, word="merchantraider")
#     #Try NLTK
#     print("accessing nltk with keyword list:")
#     for keyword in kws:
#         print("    {0}".format(keyword))
#     wordnet_jobs = s.get_words(kws)
#     print("retrieved {0} potential entries".format(len(wordnet_jobs)))
#     s.try_list("wordnet", wordnet_jobs)
#     #Try user supplied list
#     with open(filename, 'r') as f:
#         reader = csv.reader(f)
#         csv_jobs = list(reader)
#         print("retrieved {0} potential entries".format(len(csv_jobs)))
#         s.try_list("User supplied job list", csv_jobs)
#     #Try with both
#     print("Trying with both")
#     s.try_list("both lists", wordnet_jobs + csv_jobs)
#     #Try using all wordnet words
    words = words.words()
    words.append("trader")
    words.append("teacher")
    s.try_wordy_words(words)
