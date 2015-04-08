#!/usr/bin/python3.4.2
'''
Created on Apr 6, 2015

Name something that might be worn on the foot. 

Change one letter in it without changing the 
order of the other letters. The result 
will name something one might wear on the 
upper part of the body. What is it? 

Here's a hint: The thing on the upper part 
of the body is a two-word phrase.

@author: john.obrien, leiran.biton
'''


import json
from string import ascii_lowercase as alphabet
from nltk.corpus import words, wordnet
import nltk

'''
search
parameters:
1. a dictionary where the keys are words
in English and the values are the definitions
of words
2. a list of keywords which we are trying to find
in the definitions of the words

returns:
a list of words for which the keywords searched for
were found in the definitions
'''


def search(kws):
    matches = []
    # check kws against all defs in wordnets list of words
    for word in str(words.words()):
            synset = wordnet.synsets(word)
            for syn in synset:
                if all([kw.lower() in syn.definition().lower() for kw in kws]):
                            matches.append(word.lower())
    return matches

def build_candidates(footwear, upperwear):
    print("Candidates-")
    candidates = []
    for word in footwear:
        for offset, letter in enumerate(word):
            for new_letter in list(set(alphabet).difference(letter)):
                new_word = word[:offset] + new_letter + word[offset+1:]
                if new_word in upperwear:
                    candidates.append((word, new_word))
                    print("    Original Word: {0}-> Changed Word:{1}".format(word, new_word))
    return candidates
    
if __name__ == "__main__":
    nltk.download('wordnet')
    nltk.download('words')
#    print("Running test case...")
#    wd = {"boot": "worn Foot",
#         "Coot": "worn upper"}
#    footwear   = search(wd, ["worn", "foot"])
#    upperwear  = search(wd, ["worn", "upper"])
#    candidates = build_candidates(footwear, upperwear)
#    library = "dictionary.json"
#    print("Running with library {0}".format(library))
#    with open (library, "r") as fp:
#        wd = json.load(fp)
    footwear   = search(["worn", "foot"])
    upperwear  = search(["worn", "upper"])
    candidates = build_candidates(footwear, upperwear)
