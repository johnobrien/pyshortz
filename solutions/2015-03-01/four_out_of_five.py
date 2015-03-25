#!/usr/bin/python3.4.2
"""
Created on Mar 3, 2015
Rearrange the letters in a four-letter word 
and a five-letter word to get a pair of synonyms. 
For example, given 'time' and 'night,' you would say 'item' and 'thing.'
"""
# imports
import nltk
from nltk.corpus import wordnet
import requests
import shelve


class main:
    def __init__(self
                ,DEBUG=False):
        # For reference http://www.velvetcache.org/2010/03/01/looking-up-words-in-a-dictionary-using-python for reference
        nltk.download('wordnet')
        self.DEBUG = DEBUG
        
        d = shelve.open("four_out_of_five.db")
        print("Loading list of all english words...")
        if "words" in d and "hashed_words" in d:
            self.words = d["words"]
            self.hashed_words = d["hashed_words"]
        else:
            print("Stored list not found.\n")
            print("Downloading a list of all words in the english language...\n")
            r = requests.get('http://www-personal.umich.edu/~jlawler/wordlist', timeout=10)
            self.words = r.text.split("\r\n")
            self.hashed_words = {}
            for word in self.words:
                # Should create or append each word to the hashified version
                # of that word, so we have a dictionary where the keys are the
                # hashed versions of words, and the values are a list of 
                # every word which hashes to the same thing.
                self.hashed_words.setdefault(self.hashify(word), []).append(word)
            print("Storing for later use...")
            d["words"] = self.words
            d["hashed_words"] = self.hashed_words
            d.close()

    def debug_print(self, text):
        if(DEBUG == TRUE):
            print(text)
        return

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
        winners = []
        
        for word in self.words:
            # print("Trying {0}".format(word))
            synsets =  wordnet.synsets(word)
            # print("Number of synsets for {0} is {1}.".format(word, len(synsets)))
            for synset in synsets:
                # print("Seeing how many synonyms for first usage of {0}".format(synset.name()))
                if len(synset.lemma_names()) > 1:
                    # print("{0} has synonyms! \n".format(word))
                    syns = synset.lemma_names()
                    for syn1 in syns:
                        # print("Checking first synonym {0}...\n".format(syn1))
                        if len(syn1) == 4:
                            # The first synonym is four letters long!
                            for syn2 in syns:
                                if len(syn2) == 5:
                                    # The second synonym is five letters long!
                                            hashed_syn1 = self.hashify(syn1)
                                            hashed_syn2 = self.hashify(syn2)
                                            if hashed_syn1 in self.hashed_words and hashed_syn2 in self.hashed_words:
                                                    
                                                if len(self.hashed_words[self.hashify(syn1)]) > 1 and \
                                                   len(self.hashed_words[self.hashify(syn2)]) > 1:
                                                    winner = [syn1, syn2]
                                                    winners.append(winner) 
                                                    # print("We have a winner!")
                                                    # print("Synonym 1:{0}\n".format(syn1))
                                                    # print("Synonym 2:{0}\n".format(syn2))

        for winner in winners:
            print("A winner is {0} and {1}".format(winner[0], winner[1]))
            hashed_winner1 = self.hashify(winner[0])
            hashed_winner2 = self.hashify(winner[1])
            print("Alternates are {0} and {1}".format(self.hashed_words[hashed_winner1], \
                                                      self.hashed_words[hashed_winner2]) )
        print("Done.")
        return()

if __name__ == "__main__":
    m = main(DEBUG=True)
    m.solve()
