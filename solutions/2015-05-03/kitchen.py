#!/usr/local/bin/python
"""Solution to the 05-03-2015 NPR puzzle for pyshortz blog.

@authors: Leiran Biton, John O'Brien

"""
from test.test_getargs2 import Keywords_TestCase

class Solution(object):
    """Solution engine for the week's problem."""
    # imports
    from nltk.corpus import words, wordnet
    
    # attributes
    problem = """Think of a common two word phrase for something 
you might see in a kitchen. Reverse the words--that is, put 
the second word in front of the first--and you'll name a food, 
in one word, that you might prepare in a kitchen.

What is it?
"""
    
    # methods
    def __init__(self
                ,verbose=False
                ,DEBUG=False
                ):
        self.verbose = verbose
        self.DEBUG   = DEBUG
        if self.verbose:
            print(self.problem)
        
    def word_switch(self
                   ,phrase
                   ):
        """Returns a string with the words reversed and spaces removed.
        
        args:
        
        phrase - a phrase of any length"""
        return "".join(reversed(phrase.split()))
    
    def populate_kitchen_items(self
                              ,keywords=[]
                              ):
        """method to run nltk and match against a set of user-supplied keywords
adds a list of words that contain one of the keywords in their definition
to the parent object."""
        self.kitchen_items = []
        if self.verbose:
            print("populating kitchen_items list using nltk...")
        for word in self.words.words():
            synset = self.wordnet.synsets(word)
            for syn in synset:
                if any([kw.lower() in syn.definition().lower() for kw in keywords]):
                    self.kitchen_items.append(syn.name().split(".")[0].lower())
                    if self.verbose: print(".", end="", flush=True)
        if self.verbose:
            print("\n...added %i words to kitchen_items" % len(self.kitchen_items))
        # remove duplicates
        self.kitchen_items = list(set(self.kitchen_items))
        
    def populate_food(self, keywords):
        """method to run nltk and match against a set of user-supplied keywords
adds a list of words that contain one of the keywords in their definition
to the parent object."""
        self.food = []
        if self.verbose:
            print("populating food list using nltk...")
        for word in self.words.words():
            synset = self.wordnet.synsets(word)
            for syn in synset:
                if any([kw.lower() in syn.definition().lower() for kw in keywords]):
                    self.food.append(syn.name().split(".")[0].lower())
                    if self.verbose: print(".", end="", flush=True)
        if self.verbose:
            print("\n...added %i words to food" % len(self.food))
        # remove duplicates
        self.food = list(set(self.food))
    
    def build_candidates(self):
        "compare food list against kitchen list"
        self.candidates = set()
        for k_item in self.kitchen_items:
            for food in self.food:
                if k_item in food and k_item != food:
                    self.candidates.add((k_item, food))
        if self.verbose: print("found %i possible partial solutions" % len(self.candidates))
        
if __name__ == "__main__":
    
    k_kws = ["kitchen"
            ,"utensil"
            ,"cabinet"
            ,"knife"
            ,"cupboard"
            ,"cutlery"
            ,"flatware"
            ,"silverware"
            ,"chef"
            ]
    f_kws = ["food"
            ,"meat"
            ,"cheese"
            ,"bread"
            ,"vegetable"
            ,"dish"
            ,"recipe"
            ]
    s = Solution(DEBUG=True, verbose=True)
    s.populate_kitchen_items(k_kws)
    s.populate_food(f_kws)
    s.build_candidates()
    for k_item, food in s.candidates:
        print(k_item, "->", food)
    
# found 18 possible partial solutions
# ware -> chinaware
# parer -> sparerib
# cutler -> cutlery
# oven -> ovenware
# pan -> dishpan
# grid -> griddle
# beefwood -> scrub_beefwood
# pan -> trepang
# pan -> panfish
# pan -> pompano
# pan -> kalumpang
# pan -> frying_pan
# set -> russet
# pan -> pantry
# pan -> lesser_panda
# ware -> ovenware
# ware -> tableware
# server -> preserver

# of these 18 partial solutions, "panfish" seems promising. 
#    fish pan --> panfish is a legitimate solution.
# not sure where to go from here.