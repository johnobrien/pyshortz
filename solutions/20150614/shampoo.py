'''
Created on June 15, 2015

@authors: leiran biton, john o'brien
'''

from string import ascii_lowercase, punctuation
from nltk.corpus import wordnet
from solver.solver import Solver, get_all_words, char_filter

class ShampooSolver(Solver):
    '''
    The solver for the 6/14/2015 puzzle.
    '''
    def clear_candidates(self):
        """a method to clear the candidates list"""
        self.candidates = list()
    
    def solve(self, adjectives, shampoos, musicians):
        '''
        Solve method.
        '''
        self.clear_candidates()
        for musician in musicians:
            for shampoo in shampoos:
                musician_str = char_filter(musician, punctuation + " ").lower()
                shampoo_str  = char_filter(shampoo , punctuation + " ").lower()
                if musician_str.endswith(shampoo_str):
                    adjective = musician_str[:len(musician_str)-len(shampoo_str)]
                    if adjective in adjectives:
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
    print("Getting all words...")
    allwords = get_all_words()
    print("Filtering for adjectives...")
    adjectives = set()
    for word in allwords:
        word_synsets = wordnet.synsets(word)
        for synset in synsets:
            if synset.lexname().startswith("adj"):
                adjectives.add(word)
    adjectives = tuple(adjectives)
    print("Found {0} adjectives".format(len(adjectives)))
    print("Importing shampoo list from shampoos.txt")
    with open("shampoos.txt", "r") as f:
        shampoos = set([shampoo.strip() for shampoo in f.readlines()])
    print("Retrieved {0} shampoo brands".format(len(shampoos)))
    print("Importing musician list from musicians_list.txt. This might take a while.")
    with open("musicians_list.txt", "r") as f:
        musicians = set([musician.strip() for musician in f.readlines()])
    print("Retrieved {0} musician names".format(len(musicians)))
    print("Starting solver...")
    s = ShampooSolver()
    print("Solving... (this may take a while)")
    s.solve(adjectives, shampoos, musicians)
    print("Solving complete. Results:")
    s.print_candidates()