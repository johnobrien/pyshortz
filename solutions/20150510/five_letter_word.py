'''
Created on May 10, 2015

@author: johno_000
'''

from nltk.corpus import words, wordnet
from solver.solver import Solver, Word

p = '''
Think of a common one-syllable, 
five-letter word whose letters can 
be rearranged to spell a common 
two-syllable word - and then rearranged 
again to spell a common three-syllable 
word. I have two different answers in 
mind, and it's possible there are others, 
but you only have to think of one.
'''

# Where to look for syllables: http://h6o6.com/2013/03/using-python-and-the-nltk-to-find-haikus-in-the-public-twitter-stream/
# Also, http://www.onebloke.com/2011/06/counting-syllables-accurately-in-python-on-google-app-engine/

class MySolver(Solver):
        
    def Solve(self):
        for word in words:
            if word.len == 5:
                w = Word(word)
                syllable_flag = []
                syllable_flag[1] = False
                for anagram in w.anagrams:
                    syllable_flag[anagram.syllables] = True

                if syllable_flag[1] == True and\
                   syllable_flag[2] == True and\
                   syllable_flag[3] == True:
                    self.candidates.append(word)
                
                

                    
if __name__ == '__main__':
    s = MySolver(p)
    for candidate in s.candidates:
        print("{0}".format(candidate))
