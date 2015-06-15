'''
Created on June 15, 2015

@authors: leiran biton, john o'brien
'''

from string import ascii_lowercase, punctuation
from solver.solver import Solver, get_all_words, char_filter

class ShampooSolver(Solver):
    '''
    The solver for the 6/14/2015 puzzle.
    '''
    def compare(self, adjective, shampoo, musician):
        '''
        compare one element per the puzzle instructions. returns True or False
        '''
        return char_filter(adjective + shampoo, punctuation + " ").lower() == \
               char_filter(musician           , punctuation + " ").lower()
    
    def clear_candidates(self):
        """a method to clear the candidates list"""
        self.candidates = list()
    
    def solve(self, adjectives, shampoos, musicians):
        '''
        Solve method.
        '''
        self.clear_candidates()
        for adjective in adjectives:
            for shampoo in shampoos:
                for musician in musicians:
                    if self.compare(adjective, shampoo, musician):
                        self.candidates.append({"adjective": adjective,
                                                "shampoo": shampoo,
                                                "musician": musician
                                               })
        
    def print_candidates(self):
        """prints the current list of valid candidates"""
        print("current candidates:")
        for candidate in self.candidates:
            print("    {0} + {1} = {2}".format(candidate["adjective"], 
                                               candidate["shampoo"],
                                               candidate["musician"]))
    

if __name__ == '__main__':
    p = """
Think of an adjective that describes many shampoos. Add the
brand name of a shampoo in its basic form. The result,
reading the letters in order from left to right, will name a
famous musician. Who is it?
"""
    
