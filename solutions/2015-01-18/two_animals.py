'''
Created on Jan 24, 2015
Name two animals, both mammals, one domestic, the other wild, 
put their letters together and rearrange to spell another 
mammal, this one wild and not seen in North America.
@author: John
'''


class main:
    wild_mammals = set(
                  ['bison',
                   'fox',
                   'wolf',
                   'buffalo',
                   'hare',
                   'rabbit',
                   'squirrel',
                   'camel',
                   'moose',
                   'soomewoc' #ringer moose + cow = soomewoc
                   ])
    domestic_mammals = set(
                       ['cow',
                        'cat',
                        'dog',
                        'pig',
                        'sheep',
                        'llama'
                        ])
    
    def __init__(self, DEBUG):
        self.DEBUG = DEBUG
        # self.combine_and_compare()
    
    def combine_and_compare(self):
        alpha = ["".join(sorted(animal)) for animal in self.wild_mammals]
        if self.DEBUG: print(alpha)
        candidate_list = [] #contains tuples (wild_mammal, domestic_mammal, correlated alpha)
        for wild_mammal in list(self.wild_mammals):
            for domestic_mammal in list(self.domestic_mammals):
                candidate = "".join(sorted(wild_mammal + domestic_mammal))
                if self.DEBUG: print(wild_mammal, ":", domestic_mammal, ":", candidate)
                if candidate in alpha:
                    candidate_list.append((wild_mammal, domestic_mammal, list(self.wild_mammals)[alpha.index(candidate)]))
                    print("candidate:")
                    print("    %s" % wild_mammal)
                    print("    %s" % domestic_mammal)
                    print("    %s" % list(self.wild_mammals)[alpha.index(candidate)])
        print("Done.")
    
    def add_wild(self, wild_list):
        for mammal in wild_list:
            self.wild_mammals.add(mammal)
    
    def add_domestic(self, domestic_list):
        for mammal in domestic_list:
            self.domestic_mammals.add(mammal)

if __name__ == '__main__':
    m = main(DEBUG=False)
    wild = ['monkey'
           ,'ape'
           ,'lion'
           ,'tiger'
           ,'bear'
           ,'oposum'
           ,'raccoon'
           ,'weasel'
           ,'beaver'
           ]
    domestic = ['goat'
               ,'sheep'
               ,'dog'
               ,'cat'
               ,'llama'
               ]
    m.add_wild(wild)
    m.add_domestic(domestic)
    m.combine_and_compare()
