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

        for word in words.words():
            if len(word) == 5:
                w = Word(word)
                syllable_flag = {}
                for number in (1, 2, 3):
                    syllable_flag[number] = False

                for anagram in w.anagrams:
                    a = Word(anagram)
                    for num_syl in (1,2,3):
                        if num_syl in a.syllables:
                            syllable_flag[num_syl] = True

                if all([syllable_flag[1]
                       ,syllable_flag[2]
                       ,syllable_flag[3]
                       ]):
                    self.candidates.add(a)

if __name__ == '__main__':
    s = MySolver(p)
    s.solve()
    if s.candidates:
        for candidate in s.candidates:
            print("Candidate:{0}".format(candidate.anagrams))
    else:
        print("No candidates were found.")
