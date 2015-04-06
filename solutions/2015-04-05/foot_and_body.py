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
from string import join

alphabet = "ABCDEFGHIJLKMNOPQRSTUVWXYZ"

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


def search(d, kws):
    matches = []
    for key, value in d.items():
        # JO: Leiran, I can't think of a better approach
        # then this matched flag, but I feel like there
        # must be something better?
        matched = True
        for kw in kws:
            if kw not in value:
                matched = False
        if matched is True:
            matches.append(key)
    return matches

with open ("dictionary.json", "r") as fp:
    wd = json.load(fp)


footwear = search(wd, ["worn", "foot"])
upperwear = search(wd, ["worn", "upper"])

candidates = []
for word in footwear:
    for offset in range(0, len(word)):
        for letter in alphabet:
            changed_word = join([word[0:offset], letter, word[offset+1:len(word)]],"")
            if letter != word[offset] and changed_word in upperwear:
                candidates.append((word, changed_word))

print("Candidates: {0}".format(candidates))