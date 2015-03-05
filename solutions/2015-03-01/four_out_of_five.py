"""
Created on Mar 3, 2015
Rearrange the letters in a four-letter word 
and a five-letter word to get a pair of synonyms. 
For example, given 'time' and 'night,' you would say 'item' and 'thing.'
"""

# imports
from nltk.corpus import wordnet

class main:
    def __init__(self
                ,DEBUG=False):

        self.DEBUG = DEBUG
    
    def synonyms(self
                ,word
                ,DEBUG=False):
        return wn.synsets(word)
    
if __name__ == "__main__":
    m = main(DEBUG=True)
    

# List of words in English
# http://www-personal.umich.edu/~jlawler/wordlist
