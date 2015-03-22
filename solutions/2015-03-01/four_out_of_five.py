"""
Created on Mar 3, 2015
Rearrange the letters in a four-letter word 
and a five-letter word to get a pair of synonyms. 
For example, given 'time' and 'night,' you would say 'item' and 'thing.'
"""
# imports
from nltk.corpus import wordnet
import requests



class main:
    def __init__(self
                ,DEBUG=False):
        # We should write something so that if
        # Wordnet has not already been downloaded,
        # wordnet is downloaded on first use...
        # http://www.velvetcache.org/2010/03/01/looking-up-words-in-a-dictionary-using-python for reference
        
        self.DEBUG = DEBUG
        r = requests.get('http://www-personal.umich.edu/~jlawler/wordlist', timeout=10)
        self.words = r.text.split("\n")
        self.hashed_words = [self.hashify(word) for word in self.words] 

    def synonyms(self
                ,word
                ,DEBUG=False):
        return wn.synsets(word)
    
    # Hashify takes a word and reorders the letters in alphabetical order
    # useful when you are checking to see whether a rearranged form of a word
    # is the same as another set of words in a list.
    def hashify(self, word):
        return("".join(sorted(word)))
    
    def solve(self):
        
        # We loop through each word in the english language, looking for ones that
        # have synonyms
        for word in self.words:
            synsets =  wordnet.synsets(word)
            if len(synsets) > 1:
                # This words has synonyms!
                for syn1 in synset:
                    if len(syn1) == 4:
                        # The first synonym is four letters long!
                        for syn2 in synset:
                            if len(syn2) == 5:
                                # The second synonym is five letters long!
                                hash_syn1 = self.hashify(syn1)
                                hash_syn2 = self.hashify(syn2)
                                if hash_syn1 in self.hashed_words and hash_syn2 in self.hashed_words:
                                    if syn1 != hashed_syn1 and syn2 != hashed_syn2:
                                        print("We have a winner!")
                                        print("Synonym 1:{0}\n").format(syn1)
                                        print("Synonym 2:{0}\n").format(syn2)
        return()
    
if __name__ == "__main__":
    m = main(DEBUG=True)
    m.solve()
