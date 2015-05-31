'''
Created on May 31, 2015

@authors: leiran biton, john o'brien
'''

import re
import locale
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
        WORD_LEN = 5
        
        
        candidates = []
        for n, word1 in enumerate(words):
            # The following bit of code creates a regex
            # whose "match" method can be used to check
            # whether the first two and last two letters
            # of word2 equal word1.
            # I still hate regex.
            ex = word1[:2] + "{2}." + word1[3:5] + "{2}"
            regex = re.compile(ex, re.IGNORECASE)
            if len(word1) == WORD_LEN:
                for word2 in words:
                    if len(word2) == WORD_LEN and word2 != word1:
                        print("Checking #{0} out of {1}: {2} against {3}".format(n, len(words), word1, word2))
                        if regex.match(word2):
                            tmp = {}
                            tmp["word1"] = word1
                            tmp["word2"] = word2
                            candidates.append(tmp)
                            print("Added {0} and {2}".format(word1, word2)) 
        hits = []
        for candidate in candidates:
            word1_hits = ghits(" ".join([candidate["word1"], "chicken"]))
            word2_hits = ghits(" ".join(["chicken", candidate["word2"]]))
            total_hits = word1_hits + word2_hits
            hits.append((total_hits, word1_hits, word1, word2_hits, word2))
            
        hits.sort(key= lambda tup: tup[0])
        
        return(hits)


if __name__ == '__main__':
    p = """
 take a five letter word that precedes 'chicken' in a common 2 word phrase. 
 change the middle letter to form a word the comes after 'chicken' in 
 a common 2 word phrase. what are the 2 words?
"""
    s = ChickenSolver(p)
    w = words.words()
    hits = s.solve(w)
    for hit in hits:
        print("Total:{0} {1} chicken, chicken {2}".format(hit[0], hit[2], hit[4]))
