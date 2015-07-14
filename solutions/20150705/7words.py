'''
Created on Jul 9, 2015

@author: john.obrien
'''
from solver.word import Word

s = "Ira saw three emigrants restock large wands"
words = s.split()

for word in words:
    w = Word(word.lower())
    print(w.anagrams)