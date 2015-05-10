'''
Created on May 10, 2015

@author: johno_000
'''

from solver.solver import Solver

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




class MySolver(Solver):
    pass



if __name__ == '__main__':
    s = MySolver(p)
    print("{0}".format(s.hash("cargo")))
