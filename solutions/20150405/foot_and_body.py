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

import sys
from string import ascii_lowercase as alphabet
from nltk.corpus import words, wordnet

'''
search
parameters:
1. a list of keywords which we are trying to find
in the definitions of the words

returns:
a list of words for which any of the keywords searched for
were found in the definitions
'''


def search(kws, stype=all, word_type="noun"):
    """
kws   - list of keywords to be searched for
stype - either all or any (default = all)
word_type - part of speech (default = 'noun')
"""
    if stype not in (all, any): 
        return TypeError("Invalid stype argument supplied. stype must be 'any' or 'all' functions.")
    matches = []
    # check kws against all defs in wordnets list of words
    for word in words.words():
        synset = wordnet.synsets(word)
        for syn in synset:
            if stype([kw.lower() in syn.definition().lower() for kw in kws]) and \
               syn.lexname().startswith(word_type):
                matches.append(word.lower())
    return matches

def build_candidates(footwear, upperwear):
    candidates = []
    for word in footwear:
        for offset, letter in enumerate(word):
            for new_letter in list(set(alphabet).difference(letter)):
                new_word = word[:offset] + new_letter + word[offset+1:]
                if new_word in upperwear:
                    candidates.append((word, new_word))
    return candidates
    
if __name__ == "__main__":
    print("Test Run...")
    footwear   = ["boot", "shoe"]
    upperwear  = ["coot", "tshirt"]
    candidates = build_candidates(footwear, upperwear)
    for word, new_word in candidates:
        print("    Footwear: {0}-> Upperwear: {1}".format(word, new_word))
    
    print("Real run...")
    footwear   = search(["foot", "worn"], stype=all) 
    footwear.extend(search(["feet", "worn"], stype=all))
    footwear.extend(search(["foot", "wear"], stype=all))
    footwear.extend(search(["feet", "wear"], stype=all))
    footwear.extend(search(["shoe", "sock", "boot"], stype=any))
    footwear = list(set(footwear)) # remove duplicates
    print("Footwear: {0}".format(footwear))
    
    upperwear      = search(["upper", "wear"], stype=all)
    upperwear.extend(search(["arm", "worn"], stype=all))
    upperwear.extend(search(["torso", "worn"], stype=all))
    upperwear.extend(search(["shoulder", "worn"], stype=all))
    upperwear.extend(search(["chest", "worn"], stype=all))
    upperwear.extend(search(["back", "worn"], stype=all))
    upperwear.extend(search(["top", "worn"], stype=all))
    upperwear.extend(search(["upper", "wear"], stype=all))
    upperwear.extend(search(["arm", "wear"], stype=all))
    upperwear.extend(search(["torso", "wear"], stype=all))
    upperwear.extend(search(["shoulder", "wear"], stype=all))
    upperwear.extend(search(["chest", "wear"], stype=all))
    upperwear.extend(search(["back", "wear"], stype=all))
    upperwear.extend(search(["top", "wear"], stype=all))
    upperwear.extend(search(["coat", "shirt", "jacket", "necklace", "sweater"], stype=any))
    upperwear = list(set(upperwear)) # remove duplicates
    print("Upperwear: {0}".format(upperwear))
    candidates = build_candidates(footwear, upperwear)
    if len(candidates) is 0:
        print("No candidates found.")
    else:
        for word, new_word in candidates:
            print("    Footwear: {0}-> Upperwear: {1}".format(word, new_word))
