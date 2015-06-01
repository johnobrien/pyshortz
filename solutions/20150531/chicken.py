'''
Created on May 31, 2015

@authors: leiran biton, john o'brien
'''

import re
import locale
import shelve
from nltk.corpus import words
from solver.solver import Solver, ghits

class ChickenSolver(Solver):
    '''
    The solver for the 5/31/2015 puzzle.
    '''
    def solve(self, words):
        '''
        Solve method.
        '''

        hits = []
        candidates = self.get_or_rebuild(words)
        for candidate in candidates:
            tmp = {}
            tmp["word1_hits"] = ghits(" ".join([candidate["word1"], "chicken"]))
            tmp["word2_hits"] = ghits(" ".join(["chicken", candidate["word2"]]))
            tmp["total_hits"] = tmp["word1_hits"] + tmp["word2_hits"]
            tmp["word1"] = candidate["word1"]
            tmp["word2"] = candidate["word2"]
            hits.append(tmp)

        hits.sort(key= lambda l: l["total_hits"])

        return hits

    def get_or_rebuild(self, words):
        d = shelve.open("chickens.db")
        if self.rebuild or "candidates" not in d:
            print("Rebuilding candidates...")
            candidates = self.rebuild_candidates(words) 
            d["candidates"] = candidates
        else:
            print("Retrieving candidates from shelf...")
            candidates = d["candidates"]
        d.close()
        return candidates

    def rebuild_candidates(self, words):            
        WORD_LEN = 5
        candidates = []
        for n, word1 in enumerate(words):
            # The following bit of code creates a regex
            # whose "match" method can be used to check
            # whether the first two and last two letters
            # of word2 equal word1.
            # I still hate regex.
            ex = word1[:2] + "." + word1[3:5] + ""
            regex = re.compile(ex, re.IGNORECASE)
            if len(word1) == WORD_LEN:
                for word2 in words:
                    if len(word2) == WORD_LEN and word2 != word1:
                        # print("Checking #{0} out of {1}: {2} against {3}".format(n, len(words), word1, word2))
                        if regex.match(word2):
                            tmp = {}
                            tmp["word1"] = word1
                            tmp["word2"] = word2
                            candidates.append(tmp)
                            print("Added {0} and {1}".format(word1, word2)) 
    
        return candidates

if __name__ == '__main__':
    p = """
 take a five letter word that precedes 'chicken' in a common 2 word phrase. 
 change the middle letter to form a word the comes after 'chicken' in 
 a common 2 word phrase. what are the 2 words?
"""
    # To rebuild the shelve, call s.solve with w and rebuild=True
    # s = ChickenSolver(p, rebuild=True)
    s = ChickenSolver(p, rebuild=False)
    w = words.words()
    hits = s.solve(w)
    for hit in hits:
       print("Total:{0} {1} chicken, chicken {2}".format(hit["total_hits"], hit["word1"],  hit["word2"]))
