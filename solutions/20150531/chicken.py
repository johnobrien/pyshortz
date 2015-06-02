'''
Created on May 31, 2015

@authors: leiran biton, john o'brien
'''

import shelve
from solver.solver import Solver, search_brown, get_all_words, char_filter
from string import ascii_lowercase, punctuation


class ChickenSolver(Solver):
    '''
    The solver for the 5/31/2015 puzzle.
    '''
    def solve(self, words, threshold=100):
        '''
        Solve method.
        '''

        self.get_or_rebuild(words)
        print("searching the brown corpus. this may take a while.", flush=True)
        for word1, word2 in self.candidates:
            if search_brown([word1, "chicken"]) and search_brown(["chicken", word2]):
                print("One answer could be {0} chicken, chicken {1}".format(word1, word2))

    def get_or_rebuild(self, words):
        d = shelve.open("chickens.db")
        if self.__dict__.get("rebuild", False) or "candidates" not in d:
            print("Rebuilding candidates...")
            self.rebuild_candidates(words)
            d["candidates"] = self.candidates
        else:
            print("Retrieving candidates from shelf...")
            self.candidates = d["candidates"]
        d.close()

    def rebuild_candidates(self, words, word_len=5, position=2):
        self.candidates = set()
        valid_words = set()
        for word in words:
            if len(char_filter(word, " "+punctuation)) == word_len:
                valid_words.add(char_filter(word, " "+punctuation))
        for word in valid_words:
            # JOB- I removed the regex. We both hate it and it's 
            #      difficult to follow. I also parameterized a bit with options. -LB
            new_words = [word[:position]+letter+word[position+1:] \
                         for letter in ascii_lowercase]
            for new_word in new_words:
                if (new_word in valid_words) and (new_word != word):
                    self.candidates.add((word, new_word))
                    self.candidates.add((new_word, word))
                    if self.__dict__.get("verbose", False): 
                        print("Added {0} and {1}".format(word, new_word)) 

if __name__ == '__main__':
    p = """
 take a five letter word that precedes 'chicken' in a common 2 word phrase. 
 change the middle letter to form a word the comes after 'chicken' in 
 a common 2 word phrase. what are the 2 words?
"""
    # To rebuild the shelve, call s.solve with w and rebuild=True
    # s = ChickenSolver(p, rebuild=True)
    s = ChickenSolver(p, rebuild=True, verbose=False)
    w = get_all_words()
    # w = ["green", "groen", "groot"]
    # s.get_or_rebuild(w)
    # print("number of candidates:", len(s.candidates))
    s.solve(w)
