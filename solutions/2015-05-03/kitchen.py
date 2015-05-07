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
    allwords = words.words()
    
    # methods
    def __init__(self
                ,verbose=False
                ,DEBUG=False
                ):
        self.verbose = verbose
        self.DEBUG   = DEBUG
        if self.verbose:
            print(self.problem)
        
    def word_check(self
                  ,word
                  ,larger_word
                  ):
        """checks whether the leftover portion of a word after a subword is removed is a word.
        
        args:
        
        word, larger_word"""
        word_index = larger_word.find(word)
        word_len   = len(word)
        leftover_word = larger_word[:word_index] + larger_word[word_index + word_len:]
        if leftover_word in self.allwords and len(leftover_word) > 2:
            syns = self.wordnet.synsets(leftover_word)
            for syn in syns: 
                if syn.name().split(".")[0] == leftover_word:
                    return leftover_word
        return None
    
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
        for word in self.allwords:
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
        for word in self.allwords:
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
                if (food.startswith(k_item) or food.endswith(k_item)) \
                                                    and k_item != food:
                    other_word = self.word_check(k_item, food)
                    if other_word:
                        self.candidates.add((k_item, other_word, food))
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
            ,"appliance"
            ,"implement"
            ,"dish"
            ,"dishes"
            ,"fixture"
            ,"cupboard"
            ,"food"
            ]
    f_kws = ["food"
            ,"meat"
            ,"cheese"
            ,"bread"
            ,"vegetable"
            ,"fruit"
            ,"dish"
            ,"recipe"
            ,"meal"
            ,"breakfast"
            ,"lunch"
            ,"sandwich"
            ,"dinner"
            ,"loaf"
            ,"croquette"
            ,"bean"
            ,"beans"
            ,"appetizer"
            ,"dessert"
            ]
    s = Solution(DEBUG=True, verbose=True)
    s.populate_kitchen_items(k_kws)
    s.populate_food(f_kws)
    s.build_candidates()
    for k_item, other_word, food in s.candidates:
        print("{0} + {1} -> {2}".format(k_item, other_word, food))
    
# found 18 possible partial solutions (pan fish)

# found 105 possible partial solutions <-- removed 1-2 letter words
# found 86 possible partial solutions
# cook + book -> cookbook
# bean + feast -> beanfeast
# bread + stuff -> breadstuff
# spice + all -> allspice
# fish + wolf -> wolffish
# pick + tooth -> toothpick
# pie + pot -> potpie
# meal + time -> mealtime
# bread + basket -> breadbasket
# fish + dollar -> dollarfish
# ling + dump -> dumpling
# meat + horse -> horsemeat
# meat + less -> meatless
# fast + break -> breakfast
# ware + oven -> ovenware
# board + cheese -> cheeseboard
# board + bread -> breadboard
# oven + ware -> ovenware
# washer + dish -> dishwasher
# sweet + sop -> sweetsop
# dish + pan -> dishpan
# pan + dish -> dishpan
# sago + sap -> sapsago
# fish + pork -> porkfish
# oat + meal -> oatmeal
# frog + bit -> frogbit
# fish + cat -> catfish
# black + berry -> blackberry
# stick + chop -> chopstick
# mess + mate -> messmate
# bread + fruit -> breadfruit
# grocer + green -> greengrocer
# bean + stalk -> beanstalk
# cheese + cake -> cheesecake
# sop + sweet -> sweetsop
# spoon + dessert -> dessertspoon
# mars + ala -> marsala
# ware + table -> tableware
# egg + cup -> eggcup
# milk + shake -> milkshake
# mince + meat -> mincemeat
# fish + sword -> swordfish
# dishonor + able -> dishonorable
# dish + washer -> dishwasher
# ware + dinner -> dinnerware
# ware + china -> chinaware
# dish + rag -> dishrag
# sop + sour -> soursop
# pan + try -> pantry
# fish + shell -> shellfish
# serve + con -> conserve
# egg + plant -> eggplant
# eat + age -> eatage
# pan + fish -> panfish
# fish + weak -> weakfish
# fish + dolphin -> dolphinfish
# fish + spade -> spadefish
# spoon + table -> tablespoon
# meat + mince -> mincemeat
# bird + oil -> oilbird
# can + ape -> canape
# pea + cow -> cowpea
# cheese + board -> cheeseboard
# fish + tile -> tilefish
# fish + rock -> rockfish
# dish + water -> dishwater
# fish + blue -> bluefish
# fish + white -> whitefish
# bread + board -> breadboard
# ling + green -> greenling
# digest + ion -> digestion
# copper + head -> copperhead
# cheese + head -> headcheese
# fish + pan -> panfish
# fish + king -> kingfish
# oat + cake -> oatcake
# black + thorn -> blackthorn
# cook + out -> cookout
# bean + bag -> beanbag
# pea + cock -> peacock
# seed + moon -> moonseed
# pen + elope -> penelope
# sup + ping -> supping
# fish + butter -> butterfish
# meal + oat -> oatmeal
# dessert + spoon -> dessertspoon

# of these 18 partial solutions, "panfish" seems promising. 
#    fish pan --> panfish is a legitimate solution.
# not sure where to go from here.