'''
Created on May 10, 2015

@author: johno_000
'''

class Solver(object):
    '''
    classdocs
    '''


    def __init__(self, puzzle_text):
        '''
        Constructor
        '''
        self.p = puzzle_text

    def hash(self, t):
        return("".join(sorted(t)))
