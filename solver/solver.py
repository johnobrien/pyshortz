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
    return [len(list(y for y in x if y.isdigit(y[-1]))) for x in d[word.lower()]]

def alphabetize(t):
    return("".join(sorted(t)))


s = shelve.open("words.db")
if "anagrams" in s:
    anagrams = s["anagrams"]
else:
    anagrams = {}
    nltk.download('wordnet')
    for word in words.words():
        alpha = alphabetize(word)
        if alpha in anagrams:
            anagrams[alpha].update(word)
        else:
            anagrams[alpha] = set(word)
    s["anagrams"] = anagrams
s.close()

class Word(str):
    def __init__(self, t):
        self.t = t
        self.anagrams = anagrams[alphabetize[self.t]]
        self.reversed = self.t[::-1]
        self.alphabetized = alphabetize(self.t)
        self.syllabes = nsyl(self.t)

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
    
    def hash(self, t):
        return("".join(sorted(t)))
