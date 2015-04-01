#!/usr/bin/python3.4.2
'''
Created on Mar 25, 2015

Take the word "die." Think of two synonyms 
for this word that are themselves exact opposites 
of each other. 

What two words are these? A hint: they have the same number of letters.

@author: john.obrien, leiran.biton
'''

from nltk.corpus import wordnet

# For reference http://www.velvetcache.org/2010/03/01/looking-up-words-in-a-dictionary-using-python for reference

synsets = wordnet.synsets('die')

die_synonyms = set()
die_antonyms = set()

# Print the information
for synset in synsets:
    for lemma in synset.lemmas():
        die_synonyms.add(lemma.name())
        for antonym in lemma.antonyms():
            die_antonyms.add(antonym)
            
    overlap = die_synonyms and die_antonyms
   
    dsl = list(die_synonyms)
    dsl.sort(key=lambda s: len(s))

for s in dsl:
    print("Synonym: {0}".format(s))
for a in die_antonyms:
    print("Synonym: {0}".format(a))

    print("Overlapping synonyms and antonyms are {0}".format(overlap))
