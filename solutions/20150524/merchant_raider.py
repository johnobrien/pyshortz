'''
Created on May 24, 2015

@author: johno_000
'''

from solver.word import Word

class MySolver(Solver):
    '''
    MySolver is an example solver
    which is a child of the solver class.
    '''
    from nltk.corpus import words, wordnet
    
    def __init__(self, kws=[]):
        self.jobs = []
        for word in words.words():
            synset = wordnet.synsets(word)
            for syn in synset:
                if any([kw.lower() in syn.definition().lower() for kw in kws]):
                    jobs.append(syn.name().split(".")[0].lower())



p = ''' Take the phrase "merchant raider." A merchant raider was a vessel in
World War I and World War II that targeted enemy merchant ships. Rearrange the
letters of "merchant raider" to get two well-known professions. What are
they?'''


if __name__ == '__main__':

    kws = ["occupation"
              ,"job"
              ,"someone"
              ,"person"
              ,"a man"
              ,"a woman"
              ,"duty"
              ,"duties"
              ]
    
    w = Word("merchantraider")
    print(w.anagrams)
