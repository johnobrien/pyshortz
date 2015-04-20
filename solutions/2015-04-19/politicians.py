#!/usr/local/bin/env python
"""solution to the 4-19-2015 NPR puzzle for pyshortz blog."""

problem = """Problem:
Take the first names of two politicians in the news. 
Switch the first letters of their names and read the
result backward to name something that each of these 
politicians is not.
"""

class solution:
    
    def switch_letters(self, name1, name2):     
        "input two names. returns those names with their first letters switched."
        return (name2[0]+name1[1:]).lower(), (name1[0]+name2[1:]).lower()

    def read_backward(self, name):
        "returns the string input, backward."
        return name[::-1]

    def process_names(self, name1, name2):
        "process the names through switch_letters and read_backward"
        word1, word2 = [self.read_backward(name) for name in \
                        self.switch_letters(name1, name2)]
        return (word1, word2) if word1 in self.match_against and word2 in self.match_against else None
    
    def __init__(self, *names):
        from nltk.corpus import words
        self.match_against = words.words()
        self.candidates = []
        for i, name1 in enumerate(names):
            for j, name2 in enumerate(names):
                if i < j:
                    word1, word2 = self.process_names(name1, name2)
                    self.candidates.append((name1, name2, word1, word2))
        
if __name__ == "__main__":
    print("\n"+problem)
    
    # test set
    names = ("Hlbmuh", "Ecuoc")
    switched = ("humble", "couch")
    s = solution(*names)
    candidates = s.candidates
    print("candidates:")
    for name1, name2, word1, word2 in candidates:
        print(name1, name2, "-->", word1, word2)
    print("expected  :")
    for name1, name2, word1, word2 in [names+switched]:
        print(name1, name2, "-->", word1, word2)
    print("correct results?", candidates == [names + switched], "\n")
    
    # hand-made list
    