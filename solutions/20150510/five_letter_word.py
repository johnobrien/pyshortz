'''
Created on May 10, 2015

@author: johno_000
'''

from nltk.corpus import words
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


class MySolver(Solver):
    '''
    MySolver is an example solver
    which is a child of the solver class.
    '''

    def solve(self):
        '''
        the main new method
        which I figure each MySolver
        will create,
        which solves the particular problem
        for each particular week.
        '''

        for word in words:
            if word.len == 5:
                w = Word(word)
                syllable_flag = []
                syllable_flag[1] = False
                syllable_flag[2] = False
                syllable_flag[3] = False

                for anagram in w.anagrams:
                    a = Word(anagram)
                    syllable_flag[a.syllables] = True

                if syllable_flag[1] == True and\
                   syllable_flag[2] == True and\
                   syllable_flag[3] == True:
                    self.candidates.append(word)


if __name__ == '__main__':
    s = MySolver(p)
    if s.candidates:
        for candidate in s.candidates:
            print("{0}".format(candidate))
    else:
        print("No candidates were found.")
