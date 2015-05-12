'''
Created on May 10, 2015

@author: johno_000
'''

'''
Let's build a list of all anagrams!
'''
import nltk
from nltk.corpus import words, cmudict
import shelve

d = cmudict.dict()

def nsyl(word):
    """Counts the number of syllables in a word.

    Keyword arguments:
    word -- a text string, which is intended to be a single word
    """
    # From http://www.onebloke.com/2011/06/counting-syllables-accurately-in-python-on-google-app-engine/
    syllable_count = 0
    if word.lower() in d:
        for x in d[word.lower()]:
            for y in x:
                if y[-1].isdigit():
                    syllable_count += 1

    return syllable_count


def alphabetize(word):
    """Rearranges the letters in a word to place them in alphabetical order.

    Keyword arguments:
    word -- a text string, which is intended to be a single word
    """
    return("".join(sorted(word)).lower())

"""
Anagrams database.

Since anagrams are computationally intensive to calculate,
we calculate it once, and then store it.

For future calls, we load the database use it to get anagrams
for words.

The database is loaded into a dictionary called "anagrams".

The keys for "anagrams" are the alphabetized, lower cased
version of a word. The value in each database entry is the set
of all words which have the same alphabetized version, and are
therefore anagrams of each other.
"""


s = shelve.open("solver.db")

# Check if anagrams already exists in the database.
if "anagrams" in s:
    # The anagrams object was found in the solver.db!
    anagrams = s["anagrams"]
else:
    # The anagrams object was NOT found in the solver.db!
    # So let's create it!
    anagrams = {}
    for word in words.words():
        alpha = alphabetize(word)
        if alpha in anagrams:
            # We already have an anagram for this word
            # so add the current word to the set of anagrams
            anagrams[alpha].add(word)
        else:
            # We do NOT already have an anagram for this word
            # so let's create a new set object, starting with this word
            anagrams[alpha] = set([word])
    # Add the anagrams object to the database.
    s["anagrams"] = anagrams
# Close the database.
s.close()


class Word(str):
    """
    Word class which set's a bunch of useful attributes.
    """

    def __init__(self, t):
        self.t = t
        self.anagrams = anagrams[alphabetize(self.t)]
        self.reversed = self.t[::-1]
        self.alphabetized = alphabetize(self.t)
        self.syllables = nsyl(self.t)
        # self.synonyms = list of synonyms
        # self.antonyms = list of antonyms
        super().__init__()


class Solver(object):
    '''
    classdocs
    '''

    def __init__(self, puzzle_text):
        '''
        Constructor
        '''
        self.p = puzzle_text
        self.candidates = []

    def dummy_method(self):
        '''
        To test that my import is working.
        '''
        return "It's working!"
