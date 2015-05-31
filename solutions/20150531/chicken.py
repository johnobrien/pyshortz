'''
Created on May 31, 2015

@authors: leiran biton, john o'brien
'''

import re
from nltk.corpus import words
from solver.solver import Solver, ghits

class ChickenSolver(Solver):
    '''
    The solver for the 5/31/2015 puzzle.
    '''
    pass
    
    def solve(self, words):
        WORDLEN = 5

        candidates = []
        for word1 in words:
            if len(word1) == WORDLEN:
                for word2 in words:
                    if len(word2) == WORDLEN and word2 != word1:
                        # The following bit of code creates a regex
                        # whose "match" method can be used to check
                        # whether the first two and last two letters
                        # of word2 equal word1.
                        ex = word1[:2] + "{2}.}" + word1[3:5] + "{2}"
                        regex = re.compile(ex)
                        # I still hate regex.
                        if regex.match(word2):
                            candidates.append((word1, word2))

        hits = []
        for candidate in candidates:
            word1_hits = ghits(" ".join([candidate[0], "chicken"]))
            word2_hits = ghits(" ".join(["chicken", candidate[1]]))
            total_hits = word1_hits + word2_hits
            hits.append((total_hits, word1_hits, word1, word2_hits, word2))
            
        hits.sort(key= lambda tup: tup[0])
        
        return(hits)


if __name__ == '__main__':
    p = "text"
    s = ChickenSolver(p)
    w = words.words()
    hits = s.solve(w)
    for hit in hits:
        print("Total:{0} {1} chicken, chicken {2}".format(hit[0], hit[2], hit[4]))
