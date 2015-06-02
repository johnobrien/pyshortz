'''
Created on May 31, 2015

@authors: leiran biton, john o'brien
'''

import shelve
from solver.solver import Solver, get_all_words, char_filter, ghits
from string import ascii_lowercase, punctuation


class ChickenSolver(Solver):
    '''
    The solver for the 5/31/2015 puzzle.
    '''
    def solve(self, words):
        '''
        Solve method.
        '''
        with shelve.open("chickens.db") as d:

            candidates = self.get_or_rebuild(words, d)
            hits = []
            if "hits" in d:
                hits = d["hits"]
            else:
                for candidate in candidates:
                    hits1 = ghits(" ".join([candidate[0], "chicken"]))
                    hits2 = ghits(" ".join(["chicken", candidate[1]]))
                    total = hits1 + hits2
                    print("Total:{0} for {1} chicken, chicken {2}".format(total,
                                                                          candidate[0],
                                                                          candidate[1]))
                    hits.append((total, candidate, hits1, hits2))
                    hits.sort(key=lambda x: x[0])
                    d["hits"] = hits
            print(hits)

    def get_or_rebuild(self, words, d):
        if self.__dict__.get("rebuild", False) or "candidates" not in d:
            print("Rebuilding candidates...")
            candidates = self.rebuild_candidates(words)
            d["candidates"] = candidates
        else:
            print("Retrieving candidates from shelf...")
            candidates = d["candidates"]

        return candidates

    def rebuild_candidates(self, words, word_len=5, position=2):
        candidates = set()
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
                    candidates.add((word, new_word))
                    candidates.add((new_word, word))
                    if self.__dict__.get("verbose", False):
                        print("Added {0} and {1}".format(word, new_word))

        return candidates

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
